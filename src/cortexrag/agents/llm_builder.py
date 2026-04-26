from langchain_core.language_models.chat_models import BaseChatModel
from langgraph.types import Send


from pyrag.state import Topik, WorkerInput, ResearchData
from pyrag.tools import create_md



class LLM:
    def __init__(self, model: BaseChatModel):
        self.model = model

    def __call__(self, message):
        return self.model.invoke(message).content


class ModelFactory:
    def __init__(self):
        pass

    def __call__(self, models: tuple[BaseChatModel]) -> list[LLM]:
        return [LLM(x) for x in models]


class Manager:
    def __init__(self, models: tuple[BaseChatModel], topic_prompt):
        factory = ModelFactory()
        self.models: list[LLM] = factory(models)
        self.action: dict = {}
        self.iter = 0
        self.topic_prompt = topic_prompt

        self._distribution_role()


    def _distribution_role(self) -> dict:
        if len(self.models) == 0:
            raise ValueError('The list of models is empty')

        match len(self.models):
            case 1:
                self.action['topic'] = self.models[0]
                self.action['research'] = [self.models[0]]
            case 2:
                self.action['topic'] = self.models[0]
                self.action['research'] = [self.models[1]]

            case _:
                self.action['topic'] = self.models[0]
                self.action['research'] = [self.model[i] for i in range(1, len(self.models))]
        del self.models


    def topic(self, call_num: int):
        def topic_first(state: Topik):
            topics = self.action['topic'](self.topic_prompt + state.input).split(',')
            return {'main_topics': topics}

        def topic(state: WorkerInput):
            return {'current_topics': [self.action['topic'](self.topic_prompt + state.get('topic')).split(',')]}

        if call_num == 1:
            return topic_first
        else:
            return topic


    def research(self, state: ResearchData):
        input_topic = state.get('topic')
        name = state.get('name_dir')
        if self.iter == len(self.action['research']) - 1:
            response = self.action['research'][self.iter](input_topic)
            self.iter == 0
        else:
            response = self.action['research'][self.iter](input_topic)
            self.iter += 1
        create_md(f'{name}/{input_topic}.md', response)


    @staticmethod
    def route_llm(state: Topik) -> list:
        return [Send('retopic', {'topic': x}) for x in state.main_topics]

    @staticmethod
    def start_research(state: Topik) -> list:
        return [Send('research', {'topic': x,
                                          'name_dir': state.main_topics[i]
                                          }) for i in range(len(state.current_topics)) for x in state.current_topics[i]]


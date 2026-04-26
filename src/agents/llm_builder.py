from langchain_core.language_models.chat_models import BaseChatModel

class LLM:
    def __init__(self, model: BaseChatModel):
        self.model = model

    def __call__(self, message):
        return self.model.invoke(message)


class ModelFactory:
    def __init__(self):
        pass

    def __call__(self, models: tuple[BaseChatModel]) -> list[LLM]:
        return [LLM(x) for x in models]


class Manager:
    def __init__(self, models: tuple[BaseChatModel]):
        factory = ModelFactory()
        self.models: list[LLM] = factory(models)
        self.action: dict = {}
        self.iter = 0

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


    def topic(self, message: str):
        return self.action['topic'](message)


    def research(self, message: str):
        if self.iter - 1 == len(self.action['research']):
            response = self.action['research'][iter](message)
            self.iter == 0
        else:
            response = self.action['research'][iter](message)
            self.iter += 1
        return response

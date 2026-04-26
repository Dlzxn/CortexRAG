from langgraph.graph import StateGraph, START, END

from cortexrag.prompts import get_topik_prompt
from cortexrag.agents import Manager
from cortexrag.tools import make_all_dir
from cortexrag.state import Topik


class TopicsGraph:
    def __init__(self, models: tuple, topic: str, lang: str = 'en'):
        self.topic_prompt = get_topik_prompt(lang, topic)
        self.graph = StateGraph(Topik)
        self.manager = Manager(models, self.topic_prompt)

    def _build_graph(self):
        self.graph.add_node('main_topic', self.manager.topic(1))
        self.graph.add_node('retopic', self.manager.topic(2))
        self.graph.add_node('mkdir', make_all_dir)
        self.graph.add_node('research', self.manager.research)

        self.graph.add_edge(START, 'main_topic')
        self.graph.add_conditional_edges('main_topic', self.manager.route_llm)
        self.graph.add_edge('retopic', 'mkdir')
        self.graph.add_conditional_edges('mkdir', self.manager.start_research)
        self.graph.add_edge('research', END)

        return self.graph.compile()


    def invoke(self, data):
        return self._build_graph().invoke(data)
from typing import Iterable

from pyrag.core import EngineAbstract
from pyrag.graph import TopicsGraph


class Engine(EngineAbstract):
    def __init__(self, topic: str | Iterable[str], models: tuple, lang: str = 'en'):
        self.topic = topic
        self.models = models
        self.lang = lang
        self.topic_graphs = None
        self._parse_topic()

    def _parse_topic(self):
        try:
            if type(self.topic) == str:
                self.topic_graphs = [TopicsGraph(
                models=self.models,
                topic=self.topic,
                lang=self.lang
            )]
                self.topic = [self.topic]
            else:
                self.topic_graphs = [TopicsGraph(
                    models=self.models,
                    topic=topic,
                    lang=self.lang
                ) for topic in self.topic]
        except Exception as e:
            raise ValueError('param::topic must be string or iter')


    def build(self):
        for i, graph in enumerate(self.topic_graphs):
            graph.invoke({'input': self.topic[i]})
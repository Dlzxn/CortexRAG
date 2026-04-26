from abc import ABC, abstractmethod


class EngineAbstract(ABC):
    def __init__(self, topic: str, models: tuple, lang: str):
        '''
        :param topic: research topic
        :param models: tuple from LLM
        :param lang: en or ru language
        '''
        pass

    @abstractmethod
    def _parse_topic(self):
        pass

    @abstractmethod
    def build(self):
        pass
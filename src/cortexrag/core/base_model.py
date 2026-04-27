from abc import ABC, abstractmethod



class BaseChatModel(ABC):
    @abstractmethod
    def generate(self, message: str):
        pass
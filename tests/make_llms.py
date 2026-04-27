from cortexrag.integration import BaseChatModel


class Model(BaseChatModel):
    def __init__(self):
        pass
    def generate(self, message: str):
        return 'retry,animal,invoke'
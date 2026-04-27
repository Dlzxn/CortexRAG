try:
    import anthropic
except Exception as e:
    raise ImportError('To use anthropic models, type: pip install anthropic')


from cortexrag.core import BaseChatModel



class ClaudeModel(BaseChatModel):
    def __init__(self,
                 client: anthropic.Anthropic,
                 model_name: str
                 ):
        self.client: anthropic.Anthropic = client
        self.model: str = model_name

    def generate(self, message: str):
        response = self.client.messages.create(
            model = self.model,
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ]
        )
        return response.content[0].text

try:
    from chatgpt import OpenAI
except Exception as e:
    raise ImportError(
        'To use OpenAI models, type: pip install openai'
    )


from cortexrag.core import BaseChatModel


class OpenAIModel(BaseChatModel):
    def __init__(self, client: OpenAI, model_name: str):
        self.client: OpenAI = client
        self.model: str = model_name

    def generate(self, message: str):
        response = self.client.chat.completions.create(
            model = self.model,
            messages= [
                {'role': 'user', 'content': message},
            ],
            temperature=0.3
        )
        return response.choices[0].message.content

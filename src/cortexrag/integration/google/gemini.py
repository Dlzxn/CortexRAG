try:
    from google import genai
except Exception as e:
    raise ImportError(
        'To use Google models, type: pip install google-genai'
    )


from cortexrag.core import BaseChatModel



class GeminiModel(BaseChatModel):
    def __init__(self, client: genai.Client, model_name: str):
        self.client = client
        self.model = model_name

    def generate(self, message: str):
        print(type(message))
        response = self.client.models.generate_content(
            model=self.model,
            contents=message
        )
        return response.text

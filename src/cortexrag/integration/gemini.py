from google import genai


from cortexrag.core import BaseChatModel



class GeminiModel(BaseChatModel):
    def __init__(self, client: genai.Client, model_name: str):
        self.client = client
        self.model = model_name

    def generate(self, message: str):
        response = self.client.generate_content(
            model=self.model,
            content=message
        )
        return response.text

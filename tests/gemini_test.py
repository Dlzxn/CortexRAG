from google import genai
from cortexrag.integration.google import GeminiModel
from cortexrag import Engine
import os
import dotenv

dotenv.load_dotenv()

API_KEY = os.getenv('GEMINI_API')
print(API_KEY)



def gemini_int():
    client = genai.Client(
        api_key=API_KEY,
    )

    model = GeminiModel(client, 'gemini-3-flash-preview')
    engine = Engine(
        topic='Автомобили',
        models=(model, model),
        lang='ru'
    )
    engine.build()

if __name__ == '__main__':
    gemini_int()

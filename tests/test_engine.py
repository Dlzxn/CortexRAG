from src.cortexrag import Engine
from tests.make_llms import LLM_topic, LLM_research


def test_topics():
    model = LLM_topic()
    model_research = LLM_research()
    topic = 'weather'
    engine = Engine(topic, (model, model_research))
    engine.build()
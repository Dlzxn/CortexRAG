from src.graph import TopicsGraph
from tests.make_llms import LLM_topic, LLM_research


def test_topics():
    model = LLM_topic()
    model_research = LLM_research()
    topics = TopicsGraph((model, model_research), 'Hello World')
    topics.invoke({'input': 'Hello World'})
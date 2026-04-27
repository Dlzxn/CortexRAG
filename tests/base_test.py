from cortexrag import Engine
from tests.make_llms import Model


def test_main_func():
    model = Model()
    model_research = Model()
    topic='animals'

    engine = Engine(
        topic,
        (model, model_research)
    )
    engine.build()


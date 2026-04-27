import os
import shutil
from pathlib import Path

import pytest
from cortexrag import Engine
from cortexrag.graph import TopicsGraph
from tests.make_llms import Model


@pytest.fixture
def temp_dir():
    temp_dir = Path("temp_test_dir")
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    temp_dir.mkdir()
    os.chdir(temp_dir)
    yield
    os.chdir("..")
    shutil.rmtree(temp_dir)


@pytest.fixture
def models():
    return Model(), Model()


def test_engine_with_string_topic(models, temp_dir):
    topic = "weather"
    engine = Engine(topic, models)
    assert engine.topic == [topic]
    assert len(engine.topic_graphs) == 1
    assert isinstance(engine.topic_graphs[0], TopicsGraph)
    engine.build()


def test_engine_with_iterable_topic(models, temp_dir):
    topic = ("weather", "animals")
    engine = Engine(topic, models)

    assert engine.topic == tuple(topic)
    assert len(engine.topic_graphs) == 2
    assert all(isinstance(g, TopicsGraph) for g in engine.topic_graphs)
    engine.build()


def test_engine_invalid_topic(models):
    with pytest.raises(ValueError):
        Engine(123, models)

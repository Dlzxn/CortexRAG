import operator
from typing import Annotated, List
from pydantic import BaseModel, Field


class Topik(BaseModel):
    input: str = Field(..., description='Query')
    main_topics: list = Field(default_factory=list, description='main dir topics')
    current_topics: Annotated[List[List], operator.add] = Field(default_factory=list)
    data: Annotated[list[dict[str, str]], operator.add]


class WorkerInput(BaseModel):
    topic: str


class TopikList(BaseModel):
    topics: list[str]
    name_dir: str


class ResearchData(BaseModel):
    topics: str
    name_dir: str

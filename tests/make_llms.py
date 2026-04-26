from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage, BaseMessage
from langchain_core.outputs import ChatResult, ChatGeneration
from typing import Any, List, Optional


class LLM_topic(BaseChatModel):
    def _generate(
            self,
            messages: List[Any],
            stop: Optional[List[str]] = None,
            run_manager: Optional[Any] = None,
            **kwargs: Any,
    ) -> ChatResult:
        content = "machine, scroll, amazing"

        message = AIMessage(content=content)
        generation = ChatGeneration(message=message)
        return ChatResult(generations=[generation])

    @property
    def _llm_type(self) -> str:
        return "mock-topic"

class LLM_research(BaseChatModel):
    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> ChatResult:
        message = AIMessage(content='detailed research data')
        generation = ChatGeneration(message=message)
        return ChatResult(generations=[generation])

    @property
    def _llm_type(self) -> str:
        return "mock_research"
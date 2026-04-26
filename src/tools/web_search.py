from langgraph.graph import StateGraph, MessagesState, START, END

def mock_llm(state: MessagesState):
    return {"messages": [{"role": "ai", "content": "hello world"}]}

graph = StateGraph(MessagesState)
graph.add_node('mock', mock_llm)
graph.add_edge(START, "mock")
graph.add_edge("mock", END)
graph = graph.compile()

print(graph.invoke({"messages": [{"role": "user", "content": "hi!"}]}))
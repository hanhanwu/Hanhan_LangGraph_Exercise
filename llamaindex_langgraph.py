# pip install llama-index-langgraph
from llama_index import LlamaIndex
from langgraph import LangGraph

knowledge_graph = LlamaIndex.create_knowledge_graph(documents)
rag_model = LangGraph.integrate_with_knowledge_graph(knowledge_graph)
response = rag_model.query("Your query here")
print(response)


# Explore RAG Chatbot Solutions
## Agentic RAGs
* [Retrieve or Not RAG][2]
  * <b>Adaptive Retriever</b>: it decides which retriever to use based on the number of documents
  * <b>Retrieval Relevancy Check & Query Rewrite</b>: it checks overall retrieval relevancy, if not relevant, update the query and startover
  * `model.bind_tools(tools)` is crucial, it allows LLm to decide whether to retrieve when answering the questions
  * The code here also shows <b>how to use ToolNode and tools_condition</b>
* [Corrective RAG][1]
  * <b>Adaptive Retriever</b>: it decides which retriever to use based on the number of documents
  * <b>Retrieval Relevancy Check</b>: it checks the relevancy of each retrieved document
  * <b>Query Rewrite & Web Search</b>: when there's at least 1 irrelevant retrieved document, the query will be re-written to search web resources, selected web resources will be added into relevant document list to generate the final answer
 
## RAG Chatbots
* [Basic Agentic RAG Chatbot][4]
  * Added memory to the graph, so that chatbot understands user's input
  * Retrieve or Not RAG, it allows LLm to decide whether to retrieve when answering the questions
  * Single thread, not concurrent
 
## Performance Evaluaton
* [Performance Monitoring & Comparison with LangSmith][3]


[1]:https://github.com/hanhanwu/Hanhan_LangGraph_Exercise/blob/main/RAG_Chatbot/try_corrective_rag.ipynb
[2]:https://github.com/hanhanwu/Hanhan_LangGraph_Exercise/blob/main/RAG_Chatbot/try_langgraph_agentic_rag.ipynb
[3]:https://github.com/hanhanwu/Hanhan_LangGraph_Exercise/blob/main/RAG_Chatbot/try_langsmith_model_comparison.ipynb
[4]:https://github.com/hanhanwu/Hanhan_LangGraph_Exercise/blob/main/RAG_Chatbot/rag_chatbot_with_memory.ipynb

# Explore RAG Chatbot Solutions

## Agentic RAGs
* [Basic Agentic RAG][2]
  * Adaptive Retriever: it decides which retriever to use based on the number of documents
  * Retrieval Relevancy Check & Query Rewrite: it checks overall retrieval relevancy, if not relevant, update the query and startover
  * The code here also shows how to use ToolNode and tools_condition
* [Corrective RAG][1]
  * Adaptive Retriever: it decides which retriever to use based on the number of documents
  * Retrieval Relevancy Check: it checks the relevancy of each retrieved document
  * Query Rewrite & Web Search: when there's at least 1 irrelevant retrieved document, the query will be written to search web resources, selected web resources will be added into relevant document list to generate the final answer


[1]:https://github.com/hanhanwu/Hanhan_LangGraph_Exercise/blob/main/RAG_Chatbot/try_corrective_rag.ipynb
[2]:https://github.com/hanhanwu/Hanhan_LangGraph_Exercise/blob/main/RAG_Chatbot/try_langgraph_agentic_rag.ipynb

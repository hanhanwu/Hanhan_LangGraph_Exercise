# Explore RAG Chatbot Solutions
## RAG Alternatives
* [CAG (Cache-augmented generation), a faster alternative for RAG][4]

## Agentic RAGs
* [Basic Agentic RAG][2]
  * <b>Adaptive Retriever</b>: it decides which retriever to use based on the number of documents
  * <b>Retrieval Relevancy Check & Query Rewrite</b>: it checks overall retrieval relevancy, if not relevant, update the query and startover
  * The code here also shows <b>how to use ToolNode and tools_condition</b>
* [Corrective RAG][1]
  * <b>Adaptive Retriever</b>: it decides which retriever to use based on the number of documents
  * <b>Retrieval Relevancy Check</b>: it checks the relevancy of each retrieved document
  * <b>Query Rewrite & Web Search</b>: when there's at least 1 irrelevant retrieved document, the query will be re-written to search web resources, selected web resources will be added into relevant document list to generate the final answer
 
## Performance Evaluaton
* [Performance Monitoring & Comparison with LangSmith][3]

[1]:https://github.com/hanhanwu/Hanhan_LangGraph_Exercise/blob/main/RAG_Chatbot/try_corrective_rag.ipynb
[2]:https://github.com/hanhanwu/Hanhan_LangGraph_Exercise/blob/main/RAG_Chatbot/try_langgraph_agentic_rag.ipynb
[3]:https://github.com/hanhanwu/Hanhan_LangGraph_Exercise/blob/main/RAG_Chatbot/try_langsmith_model_comparison.ipynb
[4]:https://medium.com/@ronantech/cache-augmented-generation-cag-in-llms-a-step-by-step-tutorial-6ac35d415eec

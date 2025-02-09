# AI for BI

* [SQL Agent with OpenAI][1]
  * This agent can write SQL, execute SQL, rewrite failed SQL, output results 
  * When SQL execution failed, LLM checks failed SQL and try to write a better one
  * There is SQL rewrite limit, so this agent knows when to give up 😉
  * When there's no data supports user's question, the agent won't waste time to write any SQL


[1]:https://github.com/hanhanwu/Hanhan_LangGraph_Exercise/blob/main/AI_for_BI/sql_agent_openai.ipynb

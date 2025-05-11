# AI for BI

* [How to Run DeepSeek R1 through vLLM][2]
  * On Google Colab, at least needs T4 GPU as runtime 

* [SQL Agent with OpenAI][1]
  * This agent can write SQL, execute SQL, rewrite failed SQL, output results 
  * When SQL execution failed, LLM checks failed SQL and try to write a better one
  * There is SQL rewrite limit, so this agent knows when to give up 😉
  * When there's no data supports user's question, the agent won't waste time to write any SQL
 
* [SQL Agdent with SQL Logic Validation][3]
  * Comparing with the above SQL agent, it has added SQL logic validation. But to be honest, I think the best way to validate SQL query is to execute it.
 
* <b>More Ideas</b>
  * Apply [TabGLM][4] on the tabular data
  * Inspirations got from paper [SoTA with Less: MCTS-Guided Sample Selection for Data-Efficient Visual Reasoning Self-Improvement][6]
    * Difficulty based data selection: choose dataset based on how many times a SQL had been successfully generated for the query
    * Modular Evaluation
      * If you're limited by labeled SQL data, use LLMs to synthesize high-difficulty examples
      * Break text-to-SQL task into sub-steps , such as intent-recognition, foreign-key join, sub-sql, etc., simulating these substeps and evaluate them step by step. Find steps that are more likely to fail
    * Feedback Loops for Self-Tuning: reinforced fine-tuning on samples that the model initially failed to answer well.
  * [Some lessons learned from Timescale][5]


[1]:https://github.com/hanhanwu/Hanhan_LangGraph_Exercise/blob/main/AI_for_BI/sql_agent_openai.ipynb
[2]:https://github.com/hanhanwu/Hanhan_LangGraph_Exercise/blob/main/AI_for_BI/run_deepseek_r1.ipynb
[3]:https://github.com/hanhanwu/Hanhan_LangGraph_Exercise/blob/main/AI_for_BI/sql_agent_with_validation.ipynb
[4]:https://blog-en.fltech.dev/entry/2025/02/28/AAAI-TabGLM-en
[5]:https://github.com/hanhanwu/Hanhan_Conference_Notes/blob/master/AI_Agent_Conference2025.md
[6]:https://arxiv.org/pdf/2504.07934

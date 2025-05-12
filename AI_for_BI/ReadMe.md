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
  * [Lamini has a very good webinar for text-to-sql][8]
    * Passcode: `1ki=KEnN`
    * [Create small datasets for extreme accuracy][9], [expand training datasets][10]
      * create concepts for embedding
      * add questions, concepts
    * [Lamini open source library][7] 
  * [Some lessons learned from Timescale][5]


[1]:https://github.com/hanhanwu/Hanhan_LangGraph_Exercise/blob/main/AI_for_BI/sql_agent_openai.ipynb
[2]:https://github.com/hanhanwu/Hanhan_LangGraph_Exercise/blob/main/AI_for_BI/run_deepseek_r1.ipynb
[3]:https://github.com/hanhanwu/Hanhan_LangGraph_Exercise/blob/main/AI_for_BI/sql_agent_with_validation.ipynb
[4]:https://blog-en.fltech.dev/entry/2025/02/28/AAAI-TabGLM-en
[5]:https://github.com/hanhanwu/Hanhan_Conference_Notes/blob/master/AI_Agent_Conference2025.md
[6]:https://arxiv.org/pdf/2504.07934
[7]:https://docs.lamini.ai/memory_experiments/txt2sql/#3-analyze-generated-data
[8]:https://zoom.us/rec/play/X4cPd5x6BdNbIJ8KiaKaenYgX6BLg9iLH37ci9pTTM7-l4IqaEh5y1fRu9NmvPC-xBADN2W5R8WskWkK.ifiHi6Slp99NHbCL?accessLevel=meeting&canPlayFromShare=true&from=share_recording_detail&startTime=1746032175000&componentName=rec-play&originRequestUrl=https%3A%2F%2Fzoom.us%2Frec%2Fshare%2FiUlhM7OoVtEn46dcTA7Ls7IFFQe-1-VUGyoPlF4uWo75zsHCwY7gtbtV7opqQUNM.BPjZ0DZ2_4mmBfv7%3FstartTime%3D1746032175000
[9]:https://github.com/hanhanwu/Hanhan_LangGraph_Exercise/blob/main/AI_for_BI/images/1.png
[10]:https://github.com/hanhanwu/Hanhan_LangGraph_Exercise/blob/main/AI_for_BI/images/2.png

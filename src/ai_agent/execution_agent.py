from langchain_openai import ChatOpenAI
from browser_use import Agent
from prompts import prompt
from dotenv import load_dotenv

load_dotenv()

llm_chatopenai_4o = ChatOpenAI(
                            model="gpt-4o"
                        )

agent_chatopenai_4o = Agent(
        task=prompt.prompt_text,
        llm=llm_chatopenai_4o
    )
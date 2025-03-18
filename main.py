from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import AgentExecutor, create_tool_calling_agent
import os
from tools import search_tool, wiki_tool, save_tool


load_dotenv()

# llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))

class Response(BaseModel):
    text: str
    summary: str
    source: list[str]
    tools_used: list[str]

llm2 = ChatAnthropic(model="claude-3-5-sonnet-20241022")
parser = PydanticOutputParser(pydantic_object=Response)
prompt = ChatPromptTemplate.from_messages(
    [
        (   "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query using necasswry tolls.
            Wrap the ouput in this format and provide no other text\n{format_instruction}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
]
).partial(format_instruction=parser.get_format_instructions())


tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm=llm2,
    prompt=prompt,
    tools=tools
)

agent_executer = AgentExecutor(agent=agent, tools=tools, verbose=True)
query = input("What research query do you have? ")
raw_response = agent_executer.invoke({"query": query})

try:
    structured_response = parser.parse(raw_response.get("output")[0]["text"])
    print(structured_response)
except Exception as e:
    print("Error parsing response", e, "Raw response:", raw_response)



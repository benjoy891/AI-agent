from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime


def save_to_file(data: str, filename: str = "research_paper.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    formattted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formattted_text)
    
    return f"Data saved to {filename}"

save_tool = Tool(
    name="save_text_to_file",
    function=save_to_file,
    description="Save the research to a file",
)


search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    function=search.run,
    description="Search the web for information",
)


api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

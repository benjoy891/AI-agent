# AI Research Assistant

This project implements an AI-powered research assistant that can search the web, query Wikipedia, and save research findings to a file. It leverages the LangChain framework, along with tools like DuckDuckGo and Wikipedia, to provide a flexible and powerful research capability. The project uses Anthropic's Claude 3.5 Sonnet model as the language model.

## Key Features

- **Web Search:** Uses DuckDuckGo to search the web for relevant information.
- **Wikipedia Integration:** Queries Wikipedia for concise summaries of topics.
- **File Saving:** Saves research output to a text file with timestamps.
- **Structured Output:** Formats the output into a structured format (text, summary, source, tools used).
- **Customizable Prompt:** Allows for easy modification of the agent's behavior through a customizable prompt.
- **Tool Calling Agent:** Uses the tool calling agent to utilize the defined tools.
- **Anthropic Claude 3.5 Sonnet:** Uses the Claude 3.5 Sonnet model as the language model.

## File Structure

- `.gitignore`: Specifies files and directories that should be ignored by Git (e.g., `.env`, `ai-agent`).
- `tools.py`: Contains the definitions for the tools used by the agent:
  - `save_to_file`: Saves text to a file.
  - `search_tool`: Web search using DuckDuckGo.
  - `wiki_tool`: Wikipedia query.
- `requirements.txt`: Lists the project's Python dependencies.
- `.env`: Stores environment variables, such as the Anthropic API key.
- `main.py`: The main script that orchestrates the agent, tools, and user interaction.

## Dependencies

The project relies on the following Python packages:

- `langchain`: The core LangChain library.
- `langchain-community`: Community tools for LangChain.
- `langchain-openai`: OpenAI integration for LangChain.
- `langchain-anthropic`: Anthropic integration for LangChain.
- `wikipedia`: For interacting with Wikipedia.
- `python-dotenv`: For loading environment variables from a `.env` file.
- `pydantic`: For data validation and parsing.
- `duckduckgo-search`: For web searching.

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd AI-Agent
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv ai-agent
    ```

3.  **Activate the virtual environment:**

    - **Windows:**

      ```bash
      ai-agent\Scripts\activate
      ```

    - **macOS/Linux:**

      ```bash
      source ai-agent/bin/activate
      ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Create a `.env` file:**

    - Create a file named `.env` in the project's root directory.
    - Add your Anthropic API key:

      ```properties
      ANTHROPIC_API_KEY="your_anthropic_api_key"
      ```

6.  **Run the project:**

    ```bash
    python main.py
    ```

## Code Highlights

- **Tools:** The `tools.py` file defines the tools that the agent can use. Each tool is wrapped in a `Tool` object from LangChain.
- **Agent:** The `main.py` file creates a `create_tool_calling_agent` that uses the Claude 3.5 Sonnet model and the defined tools.
- **Prompt:** A `ChatPromptTemplate` is used to define the agent's behavior. The prompt instructs the agent to act as a research assistant and provides formatting instructions.
- **Output Parsing:** A `PydanticOutputParser` is used to parse the agent's output into a structured `Response` object.
- **Agent Execution:** An `AgentExecutor` is used to run the agent with the tools.
- **Error handling:** The code has error handling for parsing the response.

## Usage

1.  Run `python main.py`.
2.  The script will prompt you to enter a research query.
3.  The agent will process the query, use the tools as needed, and return a structured response.
4.  The research output will also be saved to a file named `research_paper.txt` (or the name you specify in `save_to_file`).

## Potential Improvements

- **More Tools:** Add more tools to expand the agent's capabilities (e.g., code execution, database access, image generation).
- **Advanced Prompt Engineering:** Refine the prompt to improve the quality and relevance of the agent's responses.
- **Error Handling:** Implement more robust error handling to catch and handle various types of errors.
- **User Interface:** Create a user interface (e.g., web app) to make the research assistant more accessible.
- **More LLMs:** Add more LLMs to the project, allowing the user to choose which model to use.
- **Memory:** Add memory to the agent, so it can remember previous interactions.

## Conclusion

This project demonstrates how to build a powerful AI research assistant using LangChain and various tools. It provides a solid foundation for further development and customization.

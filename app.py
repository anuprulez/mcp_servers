import asyncio
import os
import dotenv
from dotenv import load_dotenv
from mcp_use import MCPAgent, MCPClient
from langchain_groq import ChatGroq

async def main():
    # Load environment variables
    load_dotenv()

    # Create MCPClient from configuration dictionary
    client = MCPClient.from_config_file(
        os.path.join("galaxy_mcp.json")
    )

    # Create LLM
    llm = ChatGroq(model="qwen-qwq-32b")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run the query
    result = await agent.run(
        "Get the login information of the logged in user from Galaxy MCP and also provide the details of the tool tabpfn"
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())
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
        os.path.join("browser_mcp.json")
    )

    # Create LLM
    llm = ChatGroq(model="qwen-qwq-32b")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run the query
    result = await agent.run(
        "Find the best restaurant in San Francisco",
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())
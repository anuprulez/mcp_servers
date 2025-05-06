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
        "Perform these tasks: \
         1. Create a history with name 'MCP_History'. \
         2. Use the above history 'MCP_History' and upload train dataset from '/home/anup/Downloads/classification_local_train_rows.tabular' and return dataset id \
         3. Use the above history 'MCP_History' and upload test data from '/home/anup/Downloads/classification_local_test_rows.tabular' and return dataset id"
         #3. Use train and test dataset IDs from the previous step and run the latest version of the TabPFN (tool_id tabpfn) tool on the uploaded train and test datasets in 'MCP_history' history ."
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())
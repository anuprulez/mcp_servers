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
        os.path.join("config/galaxy_mcp.json")
    )

    # Create LLM
    llm = ChatGroq(model="qwen-qwq-32b")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run the query
    '''result = await agent.run(
        "Please perform the following tasks in sequence:\n"
        "1. Create a new Galaxy history and name it 'MCP_History_new'.\n"
        "2. Upload the training dataset located at '/home/anup/Downloads/classification_local_train_rows.tsv' to the 'MCP_History_new'. After uploading, return the dataset ID as 'train_id'.\n"
        "3. Upload the testing dataset located at '/home/anup/Downloads/classification_local_test_rows.tsv' to the same 'MCP_History_new'. After uploading, return the dataset ID as 'test_id'.\n"
        "4. Use the tool with ID 'tabpfn' in its latest version. Run it in the 'MCP_History_new' using 'train_id' and 'test_id' as the inputs for training and testing, respectively. Return the job output ID."
    )'''

    result = await agent.run(
        "Fetch the logged in user information from the MCP server. Return the user ID and the user name."
    )

    print(f"\nResult: {result}")



if __name__ == "__main__":
    asyncio.run(main())
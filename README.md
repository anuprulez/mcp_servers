## Run 

### Step 1: Export Galaxy URL and API key

```bash
export GALAXY_URL=https://usegalaxy.eu/
export GALAXY_API_KEY=<galaxy_api_key>
```

### Step 2: Run Galaxy MCP server: https://github.com/galaxyproject/galaxy-mcp/tree/main

```
mcp run main.py
```

### Step 2: Run MCP client

`python app.py`


### Only when Cursor client is used:

`./Cursor-0.49.6-x86_64.AppImage --no-sandbox`
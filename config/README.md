# MCP client configuration templates

Both files describe the same `zabbix` server, just two ways to launch it:

| File           | Launcher                                 | Use when                                                                                             |
|---------------|-----------------------------------------|-----------------------------------------------------------------------------------------------------|
| `mcp.json`     | `uvx` (installs from git on the fly)     | the machine has `uv` and internet access — zero setup                                                |
| `mcp.venv.json`| venv `python` + `scripts/start_server.py`| no `uv`/docker or no internet at runtime — clone/kit + `pip install -r requirements.txt` into `.venv`|
Adapt `command`/`args` paths to your checkout (or offline kit) and fill in the
`env` block. For offline servers, put credentials in the `env` block rather
than a `.env` file — a client-spawned process does not guarantee the repo
directory as CWD.

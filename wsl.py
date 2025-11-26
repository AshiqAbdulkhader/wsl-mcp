from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import subprocess
# Initialize FastMCP server
mcp = FastMCP("wsl")


@mcp.tool()
def get_wsl_distros():
    """
    List all distros in WSL.
    """
    distros = subprocess.run(
        ["wsl", "--list", "--verbose"], capture_output=True, text=True, check=True)
    return distros.stdout


@mcp.tool()
def run_command(command: str):
    """Run a command in WSL.

    Args:
        command: The command string to execute.
    """
    result = subprocess.run(
        command, capture_output=True, text=True, check=True)
    return result.stdout


def main():
    mcp.run(transport='stdio')


if __name__ == "__main__":
    main()

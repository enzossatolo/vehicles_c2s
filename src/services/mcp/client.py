import asyncio
import os
import sys

from langchain_mcp_adapters.tools import load_mcp_tools
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from src.config.config import logger
from src.services.llm.agent import Agent

server_params = StdioServerParameters(
    command=sys.executable,
    args=["src/services/mcp/server.py"],
    env={"PYTHONPATH": os.getenv("PYTHONPATH")}
)


async def mcp_client():
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = Agent(tools=tools)
            logger.info("Iniciando chat. Digite 'sair' para encerrar.")
            while True:
                user_input = input("Você: ")
                if user_input.lower() in ["sair", "exit"]:
                    break
                response = await agent.async_run(user_input)
                content = response['messages'][-1].content
                logger.info(f"Agente: {content}")

if __name__ == "__main__":
    asyncio.run(mcp_client())

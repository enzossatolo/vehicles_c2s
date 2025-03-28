import asyncio
import os
import sys
import uuid

from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langgraph.checkpoint.memory import MemorySaver

from src.config.config import logger
from src.models.vehicles import Vehicle

server_params = StdioServerParameters(
    command=sys.executable,
    args=["src/services/mcp/server.py"],
    env={"PYTHONPATH": os.getenv("PYTHONPATH")}
)


async def mcp_client():
    model = ChatOpenAI(model="gpt-4o-mini")
    memory = MemorySaver()
    thread_id = uuid.uuid4()
    config = {"configurable": {"thread_id": thread_id}}
    prompt = (
        "You are an intelligent agent responsible for assisting users in searching for vehicles in a database. "
        "Conduct the conversation by asking the user about the desired vehicle's characteristics. "
        "The characteristics you can inquire about are: "
        f"{[col.name for col in Vehicle.__table__.columns]}"
    )
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(model, tools, prompt=prompt, checkpointer=memory)
            logger.info("Iniciando chat. Digite 'sair' para encerrar.")
            while True:
                user_input = input("Você: ")
                if user_input.lower() in ["sair", "exit"]:
                    break
                response = await agent.ainvoke({"messages": user_input}, config)
                content = response['messages'][-1].content
                logger.info(f"Agente: {content}")

if __name__ == "__main__":
    asyncio.run(mcp_client())

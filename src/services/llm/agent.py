import uuid

from langchain_core.tools.base import BaseTool
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent

from src.models.vehicles import Vehicle

class Agent:
    def __init__(
        self,
        model: str = None,
        prompt: str = None,
        tools: list[BaseTool] = []
    ):
        self.model = ChatOpenAI(model=(model or "gpt-4o-mini"))
        self.memory = MemorySaver()
        self.thread_id = uuid.uuid4()
        self.config = {"configurable": {"thread_id": self.thread_id}}
        self.prompt = (prompt or (
            "You are an intelligent agent responsible for assisting users in searching for vehicles in a database. "
            "Conduct the conversation by asking the user about the desired vehicle's characteristics. "
            "The characteristics you can inquire about are: "
            f"{[col.name for col in Vehicle.__table__.columns]}"
        ))
        self.agent = self._create(tools)

    def _create(self, tools):
        return create_react_agent(
            model=self.model,
            tools=tools,
            prompt=self.prompt,
            checkpointer=self.memory
        )
    
    async def async_run(self, user_input):
        return await self.agent.ainvoke({"messages": user_input}, self.config)
    
    def run(self, user_input):
        return self.agent.invoke({"messages": user_input}, self.config)

from abc import abstractmethod
from pydantic import BaseModel
try:
    import langchain_core.agents
except ImportError:
    langchain_core = None  # type: ignore[assignment]
from typing import Any, Union

class Action(BaseModel):

    name: str
    input: Any
    action: Any

    def is_skip(self):
        return self.name == "skip"

    def is_finish(self):
        return self.name=="finish"

    def get_finish(output, log):
        if langchain_core is not None:
            return Action(name="finish", input=None, action=langchain_core.agents.AgentFinish({"output": output}, log))
        return Action(name="finish", input=None, action={"output": output})

    def get_skip():
        return Action(name="skip", input=None, action=None)

    def from_langchain(action):
        if langchain_core is not None and isinstance(action, langchain_core.agents.AgentAction):
            return Action(name=action.tool, input=action.tool_input, action=action)
        elif langchain_core is not None and isinstance(action, langchain_core.agents.AgentFinish):
            return Action(name="finish", input=None, action=action)
        return Action(name=getattr(action, 'tool', 'unknown'), input=getattr(action, 'tool_input', None), action=action)
    
    def from_gym():
        pass
    
    # get the original action input
    def unwrap(self):
        return self.action

class ControlledAgent():

    @abstractmethod
    def plan():
        pass

    @abstractmethod
    def invoke():
        pass
    
class Tool():
    pass
from pydantic import BaseModel
from typing import Union, Optional, Any, List, Dict, Tuple

from agent import Action
try:
    from langchain.agents.agent import BaseMultiActionAgent, BaseSingleActionAgent
except (ImportError, ModuleNotFoundError):
    BaseMultiActionAgent = None
    BaseSingleActionAgent = None
try:
    from langchain_core.callbacks.base import Callbacks
except (ImportError, ModuleNotFoundError):
    pass

class RuleState(BaseModel):
    toolkit: str = ""
    action: Optional[Action] = None
    agent: Optional[Any] = None
    intermediate_steps: Any #todo: List[Tuple[AgentAction, str]]
    user_input: Optional[Union[str, Dict[str, Any]]] = None # task_prompt
    run_mannager: Optional[Any] = None
    merits: List[str] = []
    critiques: List[str] = [] 
    reflection_depth:int = 0

    def add_merit(self, m: str):
        self.merits.append(m) 

    def set_critique(self, c: str):
        self.critiques.append(c) 
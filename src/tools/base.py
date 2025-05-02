from abc import ABC, abstractmethod
from typing import Any, Dict
from pydantic import BaseModel

class BaseTool(ABC, BaseModel):
    """Base class for all tools."""
    
    name: str
    description: str
    
    @abstractmethod
    def run(self, **kwargs: Any) -> Any:
        """Execute the tool's main functionality."""
        pass
    
    def __call__(self, **kwargs: Any) -> Any:
        """Make the tool callable."""
        return self.run(**kwargs) 
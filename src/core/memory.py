from langchain_core.memory import BaseMemory
from langchain.memory import ConversationBufferMemory

class AgentMemory:
    """Memory management for the agent."""
    
    def __init__(self):
        self.memory: BaseMemory = ConversationBufferMemory(
            return_messages=True,
            memory_key="chat_history"
        )
    
    def add_memory(self, input_str: str, output_str: str) -> None:
        """Add a new memory entry."""
        self.memory.save_context(
            {"input": input_str},
            {"output": output_str}
        )
    
    def get_history(self) -> dict:
        """Retrieve memory contents."""
        return self.memory.load_memory_variables({}) 
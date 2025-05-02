from langchain_community.chat_models import ChatCloudflare
from langchain_core.language_models.base import BaseLanguageModel

def get_llm(model_name: str = "llama-2-7b-chat-int8") -> BaseLanguageModel:
    """Initialize and return the Cloudflare AI LLM instance."""
    return ChatCloudflare(
        model=model_name,
        cloudflare_api_token="{{CLOUDFLARE_API_TOKEN}}",
        cloudflare_account_id="{{CLOUDFLARE_ACCOUNT_ID}}"
    ) 
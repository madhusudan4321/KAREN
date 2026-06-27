import logging
import os

from dotenv import load_dotenv

from friday.config import config

from livekit.plugins import (
    google as lk_google,
    groq as lk_groq,
    openai as lk_openai,
)

load_dotenv()

logger = logging.getLogger("karen.providers.llm")


def build_llm():

    if config.LLM_PROVIDER == "groq":

        logger.info(
            "LLM → Groq (%s)",
            config.GROQ_LLM_MODEL,
        )

        return lk_groq.LLM(
            model=config.GROQ_LLM_MODEL,
            api_key=os.getenv("GROQ_API_KEY"),
        )

    elif config.LLM_PROVIDER == "gemini":

        logger.info(
            "LLM → Gemini (%s)",
            config.GEMINI_LLM_MODEL,
        )

        return lk_google.LLM(
            model=config.GEMINI_LLM_MODEL,
            api_key=os.getenv("GOOGLE_API_KEY"),
        )

    elif config.LLM_PROVIDER == "openai":

        logger.info(
            "LLM → OpenAI (%s)",
            config.OPENAI_LLM_MODEL,
        )

        return lk_openai.LLM(
            model=config.OPENAI_LLM_MODEL,
        )

    raise ValueError(
        f"Unknown LLM provider: {config.LLM_PROVIDER}"
    )
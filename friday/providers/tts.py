import logging

from friday.config import config
from livekit.plugins import openai as lk_openai
from livekit.plugins import sarvam

logger = logging.getLogger("karen.providers.tts")


def build_tts():

    if config.TTS_PROVIDER == "sarvam":

        logger.info("TTS → Sarvam")

        return sarvam.TTS(
            target_language_code=config.SARVAM_TTS_LANGUAGE,
            model="bulbul:v3",
            speaker=config.SARVAM_TTS_SPEAKER,
            pace=config.TTS_SPEED,
        )

    elif config.TTS_PROVIDER == "openai":

        logger.info("TTS → OpenAI")

        return lk_openai.TTS(
            model=config.OPENAI_TTS_MODEL,
            voice=config.OPENAI_TTS_VOICE,
            speed=config.TTS_SPEED,
        )

    raise ValueError(
        f"Unknown TTS provider: {config.TTS_PROVIDER}"
    )
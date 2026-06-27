import logging

from friday.config import config
from livekit.plugins import openai as lk_openai
from livekit.plugins import sarvam

logger = logging.getLogger("karen.providers.stt")


def build_stt():
    if config.STT_PROVIDER == "sarvam":
        logger.info("STT → Sarvam Saaras v3")

        return sarvam.STT(
            language="unknown",
            model="saaras:v3",
            mode="transcribe",
            flush_signal=True,
            sample_rate=16000,
        )

    elif config.STT_PROVIDER == "whisper":
        logger.info("STT → OpenAI Whisper")

        return lk_openai.STT(
            model="whisper-1"
        )

    raise ValueError(
        f"Unknown STT provider: {config.STT_PROVIDER}"
    )
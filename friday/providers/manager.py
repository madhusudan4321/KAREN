import logging

from friday.config import config

from friday.providers.llm import build_llm

logger = logging.getLogger("karen.providers.manager")


class ProviderManager:

    def __init__(self):

        self.llm = build_llm()

    def get_llm(self):
        return self.llm
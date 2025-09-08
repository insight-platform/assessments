import logging
from asyncio import Queue

from .config import Config

logger = logging.getLogger(__name__)


class Detector:
    def __init__(self, config: Config, queue: Queue):
        self._config = config
        self._data = queue

    async def run(self):
        pass

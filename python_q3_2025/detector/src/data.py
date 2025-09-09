from asyncio import Queue
from dataclasses import dataclass

from .config import Config


@dataclass
class Data:
    timestamp: int
    detected: bool


class DataProducer:
    def __init__(self, config: Config, queue: Queue):
        self._config = config
        self._queue = queue

    async def run(self):
        pass

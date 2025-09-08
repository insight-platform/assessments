from asyncio import Queue
from dataclasses import dataclass


@dataclass
class Data:
    timestamp: int
    detected: bool


class DataProducer:
    def __init__(self, queue: Queue):
        self._queue = queue

    async def run(self):
        pass

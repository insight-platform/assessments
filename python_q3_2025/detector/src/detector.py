import logging
from asyncio import Queue

from .alert import AlertManager
from .config import Config

logger = logging.getLogger(__name__)


class Detector:
    def __init__(self, config: Config, queue: Queue, alert_manager: AlertManager):
        self._config = config
        self._queue = queue
        self._alert_manager = alert_manager

    async def run(self):
        pass

import asyncio
import logging

from .alert import AlertManager
from .config import Configurator
from .data import DataProducer
from .detector import Detector

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level="INFO",
        format="%(asctime)s [%(levelname)s] [%(name)s] [%(threadName)s] %(message)s",
    )
    config = await Configurator().read()
    alert_manager = AlertManager()
    queue = asyncio.Queue()
    detector = Detector(config, queue, alert_manager)
    data_producer = DataProducer(config, queue)
    await asyncio.gather(
        asyncio.create_task(detector.run()), asyncio.create_task(data_producer.run())
    )


if __name__ == "__main__":
    asyncio.run(main())

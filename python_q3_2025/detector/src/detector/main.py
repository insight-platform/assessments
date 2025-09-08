import asyncio
import logging

from detector.src.detector.config import Configurator
from detector.src.detector.data import DataProducer
from detector.src.detector.detector import Detector

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level="INFO",
        format="%(asctime)s [%(levelname)s] [%(name)s] [%(threadName)s] %(message)s",
    )
    config = await Configurator().read()
    queue = asyncio.Queue()
    detector = Detector(config, queue)
    data_producer = DataProducer(queue)
    await asyncio.gather(
        asyncio.create_task(detector.run()), asyncio.create_task(data_producer.run())
    )


if __name__ == "__main__":
    asyncio.run(main())

import logging

logger = logging.getLogger(__name__)


class Alert:
    pass


class AlertManager:

    async def send(self, alert: Alert):
        pass

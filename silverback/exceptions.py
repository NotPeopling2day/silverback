from typing import Any

from ape.exceptions import ApeException
from ape.logging import logger


class ImportFromStringError(Exception):
    pass


class DuplicateHandler(Exception):
    def __init__(self, handler_type: str):
        super().__init__(f"Only one handler allowed for: {handler_type}")


class InvalidContainerType(Exception):
    def __init__(self, container: Any):
        super().__init__(f"Invalid container type: {container.__class__}")


class NoWebsocketAvailable(Exception):
    def __init__(self):
        super().__init__(
            "Attempted to a use WebsocketRunner without a websocket-compatible provider."
        )


class SilverbackException(ApeException):
    pass


class Halt(SilverbackException):
    def __init__(self):
        super().__init__("App halted, must restart manually")


class CircuitBreaker(SilverbackException):
    """Custom exception (created by user) that should trigger a shutdown."""

    def __init__(self, message: str):
        logger.error(message)
        super().__init__(message)

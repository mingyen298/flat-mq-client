from collections.abc import Callable
from .client_options import MqttClientOptions
from typing import Union

class IMqttClient:

    def __init__(self) -> None:
        self._options: MqttClientOptions = None
        self.on_connect: Callable = None
        self.on_disconnect: Callable = None
        self.on_msg: Callable[[str, bytes, int], None] = None

    @property
    def is_connected(self):
        return NotImplementedError

    async def startAsync(self, options: MqttClientOptions) -> None:
        return NotImplementedError

    async def stopAsync(self) -> None:
        return NotImplementedError

    def publish(self, topic: str, msg: Union[str,bytes], qos: int) -> None:
        return NotImplementedError

    def subscribe(self, topic: str, qos: int) -> None:
        return NotImplementedError

    def unsubscribe(self, topic: str) -> None:
        return NotImplementedError

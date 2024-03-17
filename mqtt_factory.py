from .i_client import IMqttClient
from .client import GMqttClient

class MqttFactory:
    def __init__(self) -> None:
        pass

    def createGMqttClient(self) -> IMqttClient:
        return GMqttClient()

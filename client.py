from .i_client import IMqttClient
from .client_options import MqttClientOptions
from gmqtt import Client
from typing import Union


class GMqttClient(IMqttClient):
    def __init__(self):
        self._client = None

    async def startAsync(self, options: MqttClientOptions = None) -> None:
        self._options = options
        if options is not None and not isinstance(options, MqttClientOptions):
            raise ValueError(
                "Invalid argument type. Expected 'MqttClientOptions'")
        if options.id == "":
            raise ValueError("MQTT client id cannot be empty.")
        self._client = Client(client_id=options.id,
                              clean_session=options.clean_session)

        self._client.on_connect = self.__onConnected
        self._client.on_message = self.__onMessageReceived
        self._client.on_disconnect = self.__onDisconnected
        if options.user_name != "" and options.password != "":
            self._client.set_auth_credentials(
                username=options.user_name, password=options.password)

        await self._client.connect(host=options.host,
                                   port=options.port,
                                   keepalive=options.keepalive
                                   )

    @property
    def is_connected(self):
        return self._client.is_connected

    async def stopAsync(self) -> None:
        await self._client.disconnect()

    def publish(self, topic: str, msg: Union[str, bytes]) -> None:
        self._client.publish(topic, payload=msg, qos=0)

    def subscribe(self, topic: str, qos: int = 0) -> None:
        self._client.subscribe(topic, qos=qos)

    def unsubscribe(self, topic: str) -> None:
        self._client.unsubscribe(topic)

    def _resubscribeAll(self) -> None:
        for subscription in self._client.subscriptions:
            self._client.resubscribe(subscription=subscription)

    def __onConnected(self, client, flags, rc, properties) -> None:
        self._resubscribeAll()
        if self.on_connect is not None:
            self.on_connect()

    async def __onMessageReceived(self, client, topic, payload, qos, properties) -> None:
        if self.on_msg is not None:
            self.on_msg(topic, payload, qos)

    def __onDisconnected(self, client, packet, exc=None) -> None:
        if self.on_disconnect is not None:
            self.on_disconnect()

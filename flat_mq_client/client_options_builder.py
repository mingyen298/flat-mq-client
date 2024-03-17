from .client_options import MqttClientOptions


class MqttClientOptionsBuilder:
    def __init__(self) -> None:
        self._options = MqttClientOptions()

    def withClientID(self, client_id: str = "") -> None:
        self._options.id = client_id

    def withTcpServer(self, host: str = "0.0.0.0", port: int = 1883) -> None:
        self._options.host = host
        self._options.port = port

    def withCredentials(self, user_name: str = "", password: str = "") -> None:
        self._options.user_name = user_name
        self._options.password = password

    def withKeepAlive(self, sec: int = 60) -> None:
        self._options.keepalive = sec

    def withCleanSession(self, clean: bool = True) -> None:
        self._options.clean_session = clean

    def build(self) -> MqttClientOptions:
        return self._options

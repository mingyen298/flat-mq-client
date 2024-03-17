from .client_options import MqttClientOptions


class MqttClientOptionsBuilder:
    def __init__(self) -> None:
        self._options = MqttClientOptions()

    def withClientID(self, client_id: str = "") -> None:
        self._options.id = client_id
        return self

    def withTcpServer(self, host: str = "0.0.0.0", port: int = 1883) -> None:
        self._options.host = host
        self._options.port = port
        return self

    def withCredentials(self, user_name: str = "", password: str = "") -> None:
        self._options.user_name = user_name
        self._options.password = password
        return self

    def withKeepAlive(self, sec: int = 60) -> None:
        self._options.keepalive = sec
        return self

    def withCleanSession(self, clean: bool = True) -> None:
        self._options.clean_session = clean
        return self

    def build(self) -> MqttClientOptions:
        return self._options

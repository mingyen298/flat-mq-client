from dataclasses import dataclass



class MqttClientOptions:
    def __init__(self) -> None:
        pass
        self.id: str = ""
        self.host: str = "0.0.0.0"
        self.port: int = 1883
        self.clean_session: bool = True
        self.user_name: str = ""
        self.password: str = ""
        self.keepalive: int = 60



import asyncio
import signal
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

from flat_mq_client.mqtt_factory import MqttFactory
from flat_mq_client.i_client import IMqttClient
from flat_mq_client.client_options_builder import MqttClientOptionsBuilder

STOP = asyncio.Event()


def ask_exit(*args):
    STOP.set()

def on_msg(topic,payload,qos):
    print("Received message: topic='{}', payload='{}'".format(topic, payload))

def on_connect():
    pass
def on_disconnect():
    pass

async def main():
    builder = MqttClientOptionsBuilder()
    builder.withClientID("aaa888")
    builder.withTcpServer(host="0.0.0.0",port=1883)
    builder.withCleanSession()
    builder.withKeepAlive(sec=10)
    options = builder.build()
    client:IMqttClient = MqttFactory().createGMqttClient()
    client.on_msg = on_msg
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    await client.startAsync(options=options)

    client.subscribe("/role/client/123", qos=0)

    await STOP.wait()
    await client.stopAsync()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.add_signal_handler(signal.SIGINT, ask_exit)
    loop.add_signal_handler(signal.SIGTERM, ask_exit)

    loop.run_until_complete(main())
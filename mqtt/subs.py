import paho.mqtt.client as mqtt
from config import *

def on_message(client, userdata, message):
    print("\n============================================================================")
    print(f"message received {message.payload.decode('utf-8')}")
    print(f"message topic is \'{message.topic}\'")
    print(f"message qos = {message.qos}")
    print(f"message retain flag = {message.retain}")

def get_client():
    client = mqtt.Client("client_temp")
    client.username_pw_set(username, password)
    client.connect(host, port)
    client.subscribe(topic)
    client.on_message = on_message

    return client
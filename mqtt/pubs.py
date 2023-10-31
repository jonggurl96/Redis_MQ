from config import *
import paho.mqtt.client as mqtt
import random, time

def publish():
    mqttc = mqtt.Client("Publisher")
    mqttc.username_pw_set(username, password)
    mqttc.connect(host, port)

    while True:
        message = str(random.randbytes)
        mqttc.publish(topic, message)
        print("\n============================================================================")
        print(f"Publish to {host}:{port}")
        print(f"Topic: {topic}")
        print(f"Message: {message}")
        time.sleep(1)

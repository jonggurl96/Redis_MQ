# Python 코드로 mqtt 통신하기
```shell
pip install paho-mqtt
```

## Subscriber
```python
import paho.mqtt.client as mqtt

#subscriber callback
def on_message(client, userdata, message):
	print(f"message received {message.payload.decode('utf-8')}")
	print(f"message topic = {message.topic}")
	print(f"message qos = {message.qos}")
	print(f"message retain flag = {message.retain}")

broker_address = "127.0.0.1"
client1 = mqtt.Client("client1")
client1.connect(broker_address)
client1.subscribe("topic")
client1.on_message = on_message
client1.loop_forever()
```

## Publisher
```python
import paho.mqtt.client as mqtt

mqttc = mqtt.Client("publisher name")
mqttc.connect("192.168.123.141", "8883")
mqttc.publish("topic", "message")
```
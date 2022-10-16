import paho.mqtt.client as mqtt
import time
import json
import sys


sid = 0

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def on_publish(client, userdata, result):
    print(client, userdata, result)
    print("data published")


client = mqtt.Client()
client.username_pw_set("iothookpublic", "iothookpublic")
client.on_connect = on_connect
client.on_publish = on_publish
client.connect("www.iothook.com", 1883, 60)

# "mese/iot/write/00000000001"; // firma_namespace/firma_grup_name/write/cihaz_id
MQTT_KOMUT_LED = '{"mese":{"iot":{"write":{"led":1}}}}}'
MQTT_KOMUT_LED1 = '{"mese":{"iot":{"write":{"led1":1}}}}}'
MQTT_KOMUT_LED2 = '{"mese":{"iot":{"write":{"led2":1}}}}}'
MQTT_KOMUT_LED3 = '{"mese":{"iot":{"write":{"led3":1}}}}}'
MQTT_KOMUT_LED4 = '{"mese":{"iot":{"write":{"led4":1}}}}}'

topic = "mese/iot/write/00000000001"
test_topic = "mese/iot/response"

for i in range(1000):
    result = client.publish(test_topic, MQTT_KOMUT_LED, qos=0)
    print("result", result)
    time.sleep(1)

import asyncio
import random
import time
from paho.mqtt import client as mqtt_client
from kasa import Discover


broker = '<MQTT IP>'
port = 1883 #MQTT port
topic = "python/mqtt"
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

#async def getRTWattage(ipaddress,name):
#    dev = await Discover.discover_single(str(ipaddress))  # Connect to the device
#    await dev.update()     #Wait until connected to the device
#    energy = dev.modules["Energy"]
#    RTWattageraw = energy.current_consumption
#    return ("{" + '"e":' + str(RTWattageraw) +',"n":'+ name + "}")

async def getRTWattage(ipaddress,name):
    dev = await Discover.discover_single(str(ipaddress))  # Connect to the device
    await dev.update()     #Wait until connected to the device
    energy = dev.modules["Energy"]
    RTWattageraw = round(energy.current_consumption)
    return ("{" + '"e":' + str(RTWattageraw) +',"n":'+ name + "}")

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client,message):
    msg_count = 1
    while True:
        time.sleep(1)
        result = client.publish(topic, message)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{message}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        break;

def query_Power_To_Publish_MQTT(ipaddress, device) :
    client = connect_mqtt()
    client.loop_start
    message = asyncio.run(getRTWattage(ipaddress, device))
#    print(message)
#    message = "strings"
    publish(client,message)
    client.loop_stop()


query_Power_To_Publish_MQTT("<KasaDevicIP>","<KasaDeviceName>")
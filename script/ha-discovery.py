# python 3.6

import random, json
import time

from paho.mqtt import client as mqtt_client



broker = '192.168.68.145'
port = 1883
topic = "python/mqtt"
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
username = 'mqtt'
password = 'mqtt'

client = None

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(topic, msg):
    global client
    result = client.publish(topic, msg)
    status = result[0]
    if status != 0:
        print(f"Failed to send message to topic {topic}")

if False:
    dataTopic = "growatt-zolder"
    uniqueIdentifier = "a248"
    baseData = {
        #"name": "PV2 power",
        "stat_t": f"{dataTopic}/data",
        #"unit_of_meas": "W",
        #"val_tpl": "{{value_json['pv2power']}}",
        #"dev_cla": "power",
        #"uniq_id": f"pv2-power-{uniqueIdentifier}",
        "dev": {
        "ids": [f"{dataTopic}-{uniqueIdentifier}"],
        "name": "Growatt (zolder)",
        "mdl": "MIN 3600TL-XH",
        "mf": "Growatt"
        },
        "stat_cla": "measurement"
    }
else:
    dataTopic = "growatt-schuur"
    uniqueIdentifier = "4e6a"
    baseData = {
        "stat_t": f"{dataTopic}/data",
        "dev": {
            "ids": [f"{dataTopic}-{uniqueIdentifier}"],
            "name": "Growatt (schuur)",
            "mdl": "MIC 1000TL-X",
            "mf": "Growatt"
        },
        "stat_cla": "measurement"
    }

topicRoot = "homeassistant/sensor/"
def publishConfigObject(name:str, value_template, device_class, unit_of_measurement, icon = None):
    configData = baseData.copy()
    configData["name"] = name
    configData["val_tpl"] = value_template
    configData["unit_of_meas"] = unit_of_measurement
    configData["device_class"] = device_class
    configData["uniq_id"] = f"{name.lower().replace(' ','-')}-{uniqueIdentifier}"
    if icon:
        configData["icon"] = icon

    topicName = topicRoot + configData["uniq_id"] + "/config"

    #print(f"Topic name: '{topicName}'")
    #print(f"Data: '{configData}'")
    publish(topicName, json.dumps(configData))

if __name__ == '__main__':
    client = connect_mqtt()
    client.loop_start()

    if False:
        publishConfigObject("PV1 voltage", "{{value_json['pv1voltage']}}", "voltage", "V")
        publishConfigObject("PV2 voltage", "{{value_json['pv2voltage']}}", "voltage", "V")

        publishConfigObject("PV1 current", "{{value_json['pv1current']}}", "current", "A")
        publishConfigObject("PV2 current", "{{value_json['pv2current']}}", "current", "A")

        publishConfigObject("PV1 power",    "{{value_json['pv1power']}}",       "power", "W")
        publishConfigObject("PV2 power",    "{{value_json['pv2power']}}",       "power", "W")
        publishConfigObject("Output power", "{{value_json['outputpower']}}",    "power", "W")

        publishConfigObject("PV1 energy today",    "{{value_json['pv1energytoday']}}",       "energy", "kWh", "mdi:counter")
        publishConfigObject("PV2 energy today",    "{{value_json['pv2energytoday']}}",       "energy", "kWh", "mdi:counter")
        publishConfigObject("Today energy",        "{{value_json['energytoday']}}",          "energy", "kWh", "mdi:counter")

        publishConfigObject("PV1 energy total",    "{{value_json['pv1energytotal']}}",       "energy", "kWh", "mdi:chart-bar-stacked")
        publishConfigObject("PV2 energy total",    "{{value_json['pv2energytotal']}}",       "energy", "kWh", "mdi:chart-bar-stacked")
        publishConfigObject("Total energy",        "{{value_json['energytotal']}}",          "energy", "kWh", "mdi:chart-bar-stacked")

        publishConfigObject("Grid voltage",        "{{value_json['gridvoltage']}}",       "voltage", "V")
        publishConfigObject("Grid frequency",      "{{value_json['gridfrequency']}}",       "frequency", "Hz", "mdi:rotate-3d-variant")

        publishConfigObject("Temperature", "{{value_json['tempinverter']}}", "temperature", "°C")
    else:
        publishConfigObject("PV1 voltage", "{{value_json['pv1voltage']}}", "voltage", "V")

        publishConfigObject("PV1 current", "{{value_json['pv1current']}}", "current", "A")

        publishConfigObject("PV1 power",    "{{value_json['pv1power']}}",       "power", "W")
        publishConfigObject("Output power", "{{value_json['outputpower']}}",    "power", "W")

        publishConfigObject("Today energy",        "{{value_json['energytoday']}}",          "energy", "kWh", "mdi:counter")

        publishConfigObject("Total energy",        "{{value_json['energytotal']}}",          "energy", "kWh", "mdi:chart-bar-stacked")

        publishConfigObject("Grid voltage",        "{{value_json['gridvoltage']}}",       "voltage", "V")
        publishConfigObject("Grid frequency",      "{{value_json['gridfrequency']}}",       "frequency", "Hz", "mdi:rotate-3d-variant")

        publishConfigObject("Temperature", "{{value_json['tempinverter']}}", "temperature", "°C")


    client.loop_stop()

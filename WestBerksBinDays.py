import json
import paho.mqtt.client as mqtt
import requests

# Toggle for print statements
enable_print_statements = True

# Define the UPRN parameter
uprn = "100081226975"

# Define the JSON payloads
json_payloads = [
    {
        "jsonrpc": "2.0",
        "id": "1",
        "method": "goss.echo.westberks.forms.getNextRubbishCollectionDate",
        "params": {
            "uprn": uprn
        }
    },
    {
        "jsonrpc": "2.0",
        "id": "2",
        "method": "goss.echo.westberks.forms.getNextRecyclingCollectionDate",
        "params": {
            "uprn": uprn
        }
    },
    {
        "jsonrpc": "2.0",
        "id": "3",
        "method": "goss.echo.westberks.forms.getNextFoodWasteCollectionDate",
        "params": {
            "uprn": uprn
        }
    }
]

# URL for the POST request
url = "https://www.westberks.gov.uk/apiserver/ajaxlibrary"

# Set the request headers
headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "User-Agent": "PostmanRuntime/7.32.2",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

# MQTT broker details
mqtt_broker = "192.168.1.55"   #  <--- make this you own! use: https://uprn.uk/postcode/
mqtt_port = 1883
mqtt_topic_base = "bin_days/"
mqtt_topics = [
    "rubbishCollectionDate",
    "recyclingCollectionDate",
    "foodWasteCollectionDate"
]

# MQTT client setup
client = mqtt.Client()
client.connect(mqtt_broker, mqtt_port)

# Send the POST requests and publish responses to MQTT
for i, payload in enumerate(json_payloads):
    # Convert the JSON payload to a string
    json_string = json.dumps(payload)

    # Send the POST request
    if enable_print_statements:
        print("Sending POST request", i+1, "to:", url)
    response = requests.post(url, data=json_string, headers=headers)

    # Check the response status code
    if enable_print_statements:
        print("Response status code:", response.status_code)

    # Publish the response to the MQTT topic
    mqtt_topic = mqtt_topic_base + mqtt_topics[i]
    mqtt_payload = response.text
    if enable_print_statements:
        print("Publishing to MQTT topic:", mqtt_topic)
    client.publish(mqtt_topic, mqtt_payload)

# Disconnect from the MQTT broker
client.disconnect()

if enable_print_statements:
    print("Script execution complete.")

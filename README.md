Python script for making HTTP POST requests and publishing responses to MQTT

This Python script demonstrates how to make HTTP POST requests to a specified URL and publish the corresponding responses to MQTT topics using the Paho MQTT library. It includes the ability to customize the JSON payload, request headers, and MQTT broker details.

Features:
- Sends JSON payloads as POST requests to a URL
- Supports customization of request headers including Content-Type and additional headers
- Publishes the responses to MQTT topics
- Includes conditional print statements for debugging

Usage:
1. Customize the JSON payloads, URL, request headers, and MQTT broker details according to your requirements.
2. Run the script to send the POST requests and publish the responses to MQTT.

Dependencies:
- Python 3.x
- Paho MQTT library (pip install paho-mqtt)
- Requests library (pip install requests)

Note: Make sure to have an active MQTT broker for successful publishing.

Customise this by inserting your Unique Property Reference Number which can be found here: https://uprn.uk/postcode [eg: "100081226975" - Newbury Town Hall]
Also be sure to change your MQTT broker address, username and password

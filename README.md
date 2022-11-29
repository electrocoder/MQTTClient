# MQTT Client

<a href="https://iothook.com/"><img src="https://raw.githubusercontent.com/electrocoder/MQTTClient/main/icon.png"></a>

## Description

This project was developed with Python and Tkinter to subscribe to topics and messages, broadcast and search incoming
messages while developing a project with the MQTT protocol.

## Version History

0v3 26.11.2022: Alfa MQTT Client

0v2 15.10.2022: Alfa MQTT Client

0v1 10.10.2022 : Start project

## Contributing

If you want to be included in the project, please copy it and make the changes you see necessary and submit.

## Use and Operation

<a href="https://iothook.com/"><img src="https://raw.githubusercontent.com/electrocoder/MQTTClient/main/img/_1_main_window.png"></a>

<a href="https://iothook.com/"><img src="https://raw.githubusercontent.com/electrocoder/MQTTClient/main/img/_2_menu.png"></a>

<a href="https://iothook.com/"><img src="https://raw.githubusercontent.com/electrocoder/MQTTClient/main/img/_3_new_connect.png"></a>

<a href="https://iothook.com/"><img src="https://raw.githubusercontent.com/electrocoder/MQTTClient/main/img/_4_open_connect.png"></a>

<a href="https://iothook.com/"><img src="https://raw.githubusercontent.com/electrocoder/MQTTClient/main/img/_5_broker_list.png"></a>

<a href="https://iothook.com/"><img src="https://raw.githubusercontent.com/electrocoder/MQTTClient/main/img/_6_main_window_subscribe.png"></a>

<a href="https://iothook.com/"><img src="https://raw.githubusercontent.com/electrocoder/MQTTClient/main/img/_7_search_window.png"></a>

<a href="https://iothook.com/"><img src="https://raw.githubusercontent.com/electrocoder/MQTTClient/main/img/_8_search.png"></a>

# Install

pip install mqttclient

## Pyinstaller

### MacOS

pyinstaller MQTTClient.py -w --windowed

### Windows

pyinstaller MQTTClient.py -w --windowed

### Linux

pyinstaller MQTTClient.py -w --windowed

## Using TestPyPI with Twine

twine upload --repository testpypi dist/*

## py2app

### MacOS

python setup.py py2app -A --iconfile icon.png

### Windows

python setup.py py2exe -A --iconfile icon.png

## auto-py-to-exe

### Windows

auto-py-to-exe

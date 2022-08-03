import sys
import gc
import os
import secrets


import json
import time
#from umqtt.robust import MQTTClient

print("YAY! main.py is executing ...")
# networking.getGoodWIFI()
# networking.printStatus()



"""
def receivedMessage(topic, msg):
    print(f"Received from {topic}: \n{msg}")
    try:
        message = msg.decode('utf-8')
        data = json.loads(message)
    except ValueError as exc:
        print(f"Received message is not json :( {exc}")
        return
    print(f"Received Command: {data}")
    payload = data["payload"]
    _project, _action, _input = payload["Project"], payload["Action"], payload["Input"]
    execute_command(_project, _action, _input)  # , logger=AIO.publish)


AIO.begin(receivedMessage)
AIO.subscribe("GET")
AIO.subscribe("POST")
AIO.publish("Hello World!")

try:
    while True:
        #print("Checking ...")
        AIO.check(debug=False)
        time.sleep(1)
except Exception as exc:
    print(f"Exiting main.py main loop: {exc}")
    AIO.disconnect()
    raise exc
"""
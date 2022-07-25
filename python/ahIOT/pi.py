import json
from ahIOT.lib.AIO import Aio
from ahIOT.lib.ThermalSensor.Extract_raw import get_frame, iterate

def post_frame(data):
  Aio.send_stream(data)

while True:
  frame = get_frame()
  if frame == None: continue
  post_frame(json.dumps({"stream": list(frame)}))
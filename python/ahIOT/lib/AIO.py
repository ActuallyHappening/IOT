import json
import math
from random import random
from typing import List
import Adafruit_IO as AIO
from dotenv import dotenv_values

aio = None # Attempted to be initialized with .env credentials

defaultSchema = {
  "group": "brad",
  "ping_pi": "ping", # Name is pi_ping, key is 'ping'
  "ping_host": "host-ping",
  "test": "test",
  
  "pi_status": "pi-status",
  "host_status": "host-status",

  "data": "test-data",
  "control": "test-control",
  "stream": "ir-stream",
}

class Aio:
  client: AIO.Client = None
  schema: dict[str, str] = {}
  
  def __init__(self, username: str, key: str, scheme: dict[str, str] = defaultSchema):
    self.client = AIO.Client(username, key)
    self.schema = scheme
  
  # @classmethod
  def send(cls, group: str, feed: str, *, data):
      fullName = group + "." + feed
      cls.client.send(fullName, data)
  
  # @classmethod
  def receive(cls, group: str, feed: str):
      fullName = group + "." + feed
      print(f"Getting from {fullName=}")
      return cls.client.receive(fullName).value

  # @classmethod
  def send_schema(cls, scheme_option, data):
    cls.send(cls.schema["group"], cls.schema[scheme_option], data=data)
    
  # @classmethod
  def receive_schema(cls, scheme_option):
    return cls.receive(cls.schema["group"], cls.schema[scheme_option])

  def send_data(self, data):
      self.send_schema("data", data=data)
  
  def pi_status_send(self, data):
    self.send_schema("pi_status", data=data)
  
  def _get_pi_status(self):
    return self.receive_schema("pi_status")
  
  def host_status_send(self, data):
    self.send_schema("host_status", data=data)
  
  def _get_host_status(self):
    return self.receive_schema("host_status")
      
  def pi_ping(self, *, streaming: bool = True, inactive: bool = False):
    code: int = 0
    if not inactive: 1 + int(streaming)
    else: code = -1
    self.send_schema("ping_pi", code)
  
  def _get_pi_ping_status(self):
    return self.receive_schema("ping_pi")
    
  def host_ping(self, *, receiving: bool = True, inactive: bool = False):
    code: int = 0
    if not inactive: 1 + int(receiving)
    else: code = -1
    self.send_schema("ping_host", code)
  
  def _get_host_ping_status(self):
    return self.receive_schema("ping_host")  

  def receive_control(self):
      return self.receive_schema("control")
  
  def send_stream(self, data):
      self.send_schema("stream", data=data)
  
  def receive_stream(self):
      return self.receive_schema("stream")
  
  def send_stream_data(self, data):
      self.send_stream(json.dumps({
        "stream": data,
      }))
  
  def receive_stream_data(self) -> List[int] | str:
    return json.loads(self.receive_stream())["stream"]
  
def reset_aio_stream(stratagy: str = "lines", *, aio=aio):
  fakeStream = []
  for y in range(24):
    for x in range(32):
      if stratagy == "waves":
        fakeStream.append(x+y)
      elif stratagy == "lines":
        fakeStream.append(x)
      elif stratagy == "columns":
        fakeStream.append(y)
      elif stratagy == "random" or True:
        fakeStream.append(int(random()+1)*69)
  aio.send_stream_data(fakeStream)
  stream_data = aio.receive_stream_data()
  assert len(stream_data) == 32*24

env_variables = dotenv_values()
try:
  defaultPassword = env_variables["ADAFRUIT_IO_USERNAME"]
  defaultKey = env_variables["ADAFRUIT_IO_KEY"]
except KeyError as exc:
  print(f"Couldn't load password and username for Adafruit IO defaults: {exc}")
else:
  if defaultPassword and defaultKey:
    aio = Aio(username=defaultPassword, key=defaultKey)
    print("AIO: Loaded credentials from environment variables")
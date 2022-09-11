from ast import Import
import json
from random import randrange
from typing import List
try:
  from dotenv import dotenv_values
except ImportError:
  from python_dotenv.src.dotenv import dotenv_values
import os
import requests

_env_variables = dotenv_values() | os.environ
_endpoint = _env_variables["FIREBASE_ENDPOINT"]

s = requests.Session()

def send_firebase(data: "List[int]"):
  print("Sending firebase request ...")
  r = s.put(_endpoint, json={"json":json.dumps(data)})
  print(f"Sent firebase request {r}; Status code: {r.status_code}")

def reset_firebase_stream(strategy: str = "lines"):
  fakeStream: List[int] = []
  for y in range(24):
    for x in range(32):
      if strategy == "waves":
        fakeStream.append(x+y)
      elif strategy == "lines":
        fakeStream.append(x)
      elif strategy == "columns":
        fakeStream.append(y)
      elif strategy == "random" or True:
        fakeStream.append(randrange(69))
  print(f"Sending fake {strategy} through firebase ...")
  send_firebase(fakeStream)
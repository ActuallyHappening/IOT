import json
from random import randrange
from typing import List


def send_firebase(data: "List[int]"):
  import requests
  from dotenv import dotenv_values
  import os
  env_variables = dotenv_values() | os.environ
  r = requests.put(env_variables["FIREBASE_ENDPOINT"], json={"json":json.dumps(data)})

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
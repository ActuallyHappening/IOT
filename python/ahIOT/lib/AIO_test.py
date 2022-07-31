from __future__ import annotations
import json
import os
from typing import TYPE_CHECKING, Any, Callable, Tuple
from functools import cache
import uuid
import pytest

@pytest.fixture
def AIO():
  from . import AIO
  return AIO

@pytest.fixture
def Aio(AIO):
  assert AIO.Aio
  return AIO.Aio

@pytest.fixture
def _aio(AIO):
  assert AIO.aio
  return AIO.aio

@pytest.fixture
def env_credentials() -> dict[str, str]:
  from dotenv import dotenv_values
  secrets = dotenv_values(verbose=True) | dict(os.environ)
  _username = "ADAFRUIT_IO_USERNAME"
  _key = "ADAFRUIT_IO_KEY"
  
  assert _username in secrets
  assert secrets[_username]
  
  assert _key in secrets
  assert secrets[_key]
  
  return {_username: secrets[_username], _key: secrets[_key]}

@pytest.fixture
def credentials(env_credentials, _aio):
  aio = _aio
  assert aio is not None
  assert aio is not False
  assert aio.client
  assert aio.client.username == env_credentials["ADAFRUIT_IO_USERNAME"]
  assert aio.client.key == env_credentials["ADAFRUIT_IO_KEY"]
  return True, aio

@pytest.fixture
def aio(credentials):
  """Fixture for aio sign in"""
  status, _aio = credentials
  if status is False:
    raise NotImplementedError("No signed-in AIO instance")
  return _aio


def test_aio_instance_schema(AIO, aio):
  if aio is False: return False
  assert aio.schema == AIO.defaultSchema
  assert aio.schema["group"]

def check_AIO(post, receive, extractID=lambda s: s.split(":")[1]):
  id = str(uuid.uuid4())
  
  post(id)
  received = receive()
  
  assert received
  receivedID = extractID(received)
  assert receivedID == id

def test_schema_send_receive(aio):
  check_AIO(
    lambda id: aio.send_schema("test", data=f"Send from pytest (schema test) test_schema_send_receive:{id}"),
    lambda: aio.receive_schema("test"),
  )
  for schema in aio.schema:
    if schema == "group": continue
    check_AIO(
      lambda id: aio.send_schema(schema, data=f"Send from pytest ([Auto] {schema}) test_schema_send_receive:{id}"),
      lambda: aio.receive_schema(schema),
    )

def test_raw_send_receive(aio):
  check_AIO(
    lambda id: aio.client.send("default.test", f"Send from pytest (default.test) test_raw_send_receive:{id}"),
    lambda: aio.client.receive("default.test").value
  )
  check_AIO(
    lambda id: aio.client.send("brad.test", f"Send from pytest (brad.test) test_raw_send_receive:{id}"),
    lambda: aio.client.receive("brad.test").value
  )

def test_custom_send_receive(aio):
  check_AIO(
    lambda id:
    aio.send("default", "test", data=f"Send from pytest (default.test) test_custom_send_receive:{id}"),
    lambda: aio.receive("default", "test")
  )
  check_AIO(
    lambda id:
    aio.send("brad", "test", data=f"Send from pytest (brad.test) test_custom_send_receive:{id}"),
    lambda: aio.receive("brad", "test")
  )

def test_schema_stream(aio):
  check_AIO(
    lambda id: aio.send_stream(data=json.dumps({
      "stream": [],
      "test": f"Send from pytest (schema stream) test_schema_stream:{id}",
    })),
    lambda: aio.receive_stream(),
    lambda s: json.loads(s)["test"].split(":")[1]
  )

def test_schema_stream_data(aio):
  check_AIO(
    lambda id: aio.send_stream_data(f"Send from pytest (schema stream data) test_schema_stream_data:{id}"),
    lambda: aio.receive_stream_data(),
  )

def test_pi_ping(aio):
  # Manually check ping data
  aio.pi_ping(inactive=True)
  assert int(aio._get_pi_ping_status()) == -1

def test_host_ping(aio):
  # Manually check ping data
  aio.host_ping(inactive=True)
  assert int(aio._get_host_ping_status()) == -1

def test_pi_status_updates(aio):
  check_AIO(
    lambda id: aio.pi_status_send(data=f"Send from pytest (pi status update) test_pi_status_updates:{id}"),
    lambda: aio._get_pi_status(),
  )

def test_host_status_updates(aio):
  check_AIO(
    lambda id: aio.host_status_send(data=f"Send from pytest (host status update) test_host_status_updates:{id}"),
    lambda: aio._get_host_status(),
  )
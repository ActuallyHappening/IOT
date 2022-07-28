
import json
from typing import Callable, Tuple
from functools import cache
import uuid

@cache
def test_aio_import():
  from . import AIO
  return AIO

@cache
def test_aio_class_exists():
  aio = test_aio_import()
  assert aio.Aio
  return aio.Aio

@cache
def test_aio_has_instance():
  aio = test_aio_import()
  assert aio.aio is None or isinstance(aio.aio, aio.Aio)
  return aio.aio if aio.aio is not None else False

@cache
def test_env_credentials():
  from dotenv import dotenv_values
  secrets = dotenv_values(verbose=True)
  # print(f"Secrets: {secrets}")
  if secrets == None:
    return False
  # print("Checking for ADAFRUIT_IO_USERNAME in dotenv values ...")
  assert "ADAFRUIT_IO_USERNAME" in secrets
  # print("Checking for ADAFRUIT_IO_KEY in dotenv values ...")
  assert "ADAFRUIT_IO_KEY" in secrets
  return secrets

@cache
def test_proper_credentials():
  secrets = test_env_credentials()
  if secrets is None:
    return False
  aio = test_aio_has_instance()
  assert aio is not False
  assert aio.client
  assert aio.client.username == secrets["ADAFRUIT_IO_USERNAME"]
  assert aio.client.key == secrets["ADAFRUIT_IO_KEY"]
  return True, aio

def ensure_signed_in(f: Callable) -> Callable:
  """Decorator, passes aio instance signed in (or doesn't call func)"""
  status, aio = test_proper_credentials()
  if status is False:
    return lambda *x, **y: print("No signed-in AIO instance")
  return lambda *x, **y: f(aio, *x, **y)

@cache
def test_aio_instance_schema():
  AIO = test_aio_import()
  aio = test_aio_has_instance()
  if aio is False: return False
  assert aio.schema == AIO.defaultSchema
  assert aio.schema["group"]
  return True

def check_AIO(post, receive, extractID=lambda s: s.split(":")[1]):
  id = str(uuid.uuid4())
  
  post(id)
  received = receive()
  
  assert received
  receivedID = extractID(received)
  assert receivedID == id

@ensure_signed_in
def test_raw_send_receive(aio):
  check_AIO(
    lambda id: aio.client.send("default.test", f"Send from pytest (default.test) test_raw_send_receive:{id}"),
    lambda: aio.client.receive("default.test").value
  )
  check_AIO(
    lambda id: aio.client.send("brad.test", f"Send from pytest (brad.test) test_raw_send_receive:{id}"),
    lambda: aio.client.receive("brad.test").value
  )

@ensure_signed_in
def test_custom_send_receive(aio):
  check_AIO(
    lambda id:
    aio.send("default", "test", data=f"Send from pytest (default.test) test_custom_send_receive:{id}"),
    lambda: aio.receive("default", "test").value
  )
  check_AIO(
    lambda id:
    aio.send("brad", "test", data=f"Send from pytest (brad.test) test_custom_send_receive:{id}"),
    lambda: aio.receive("brad", "test").value
  )

@ensure_signed_in
def test_schema_send_receive(aio):
  check_AIO(
    lambda id: aio.send_schema("test", data=f"Send from pytest (schema test) test_schema_send_receive:{id}"),
    lambda: aio.receive_schema("test").value,
  )
  for schema in aio.schema:
    if schema == "group": continue
    check_AIO(
      lambda id: aio.send_schema(schema, data=f"Send from pytest ([Auto] {schema}) test_schema_send_receive:{id}"),
      lambda: aio.receive_schema(schema).value,
    )
  

@ensure_signed_in
def test_schema_stream(aio):
  check_AIO(
    lambda id: aio.send_stream(data=json.dumps({
      "stream": [],
      "test": f"Send from pytest (schema stream) test_schema_stream:{id}",
    })),
    lambda: aio.receive_stream().value,
    lambda s: json.loads(s)["test"].split(":")[1]
  )

@ensure_signed_in
def test_schema_stream_data(aio):
  check_AIO(
    lambda id: aio.send_stream_data(f"Send from pytest (schema stream data) test_schema_stream_data:{id}"),
    lambda: aio.receive_stream_data(),
  )

@ensure_signed_in
def test_pi_ping(aio):
  # Manually check ping data
  aio.pi_ping(inactive=True)
  assert aio._get_pi_ping_status() == -1

@ensure_signed_in
def test_host_ping(aio):
  # Manually check ping data
  aio.host_ping(inactive=True)
  assert aio._get_host_ping_status() == -1

@ensure_signed_in
def test_pi_status_updates(aio):
  check_AIO(
    lambda id: aio.pi_status_send(data=f"Send from pytest (pi status update) test_pi_status_updates:{id}"),
    lambda: aio._get_pi_status(),
  )

@ensure_signed_in
def test_host_status_updates(aio):
  check_AIO(
    lambda id: aio.host_status_send(data=f"Send from pytest (host status update) test_host_status_updates:{id}"),
    lambda: aio._get_host_status(),
  )
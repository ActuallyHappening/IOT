from functools import cache
import uuid


@cache
def test_pi_import():
  from . import pi
  assert pi
  return pi

@cache
def test_pi_main_exists():
  pi = test_pi_import()
  assert pi.main
  return pi.main

@cache
def test_host_import():
  from . import host
  assert host
  return host

@cache
def test_host_main_exists():
  host = test_host_import()
  assert host.main
  return host.main

@cache
def test_aio_lib_import():
  from .lib import AIO
  if AIO.aio is None:
    raise NotImplementedError("Please instinate AIO.aio with credentials (.env file)")
  assert AIO.aio.send_stream_data
  assert AIO.aio.receive_stream_data
  return AIO.aio

def check_AIO(post, receive, extractID=lambda s: s.split(":")[1]):
  id = str(uuid.uuid4())
  
  post(id)
  received = receive()
  
  assert received
  receivedID = extractID(received)
  assert receivedID == id

def test_aio_stream_works():
  aio = test_aio_lib_import()
  check_AIO(
    lambda id: aio.send_stream_data(f"Send from pytest (__stream_data__) test_aio_stream_works:{id}"),
    lambda: aio.receive_stream_data(),
  )
  return aio
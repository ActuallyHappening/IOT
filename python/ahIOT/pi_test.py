from functools import cache


@cache
def test_pi_import():
  import pi
  assert pi
  return pi

@cache
def test_pi_main_exists():
  pi = test_pi_import()
  assert pi.main
  return pi.main

@cache
def test_aio_lib_import():
  from lib import AIO
  if AIO.aio is None:
    raise NotImplementedError("Please instinate AIO.aio with credentials (.env file)")
  assert AIO.aio.send_stream_data
  return AIO.aio


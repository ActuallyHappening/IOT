from functools import cache
from .do_test import test_host_import
host = test_host_import()

@cache
def test_host_main_exists():
  assert host.main
  return host.main

@cache
def test_host_step_exists():
  assert host.step
  return host.step

def test_host_ping_works():
  assert host._ping
  host._ping(inactive=True, receiving=False)


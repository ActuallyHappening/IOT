from functools import cache
from typing import Callable
from .do_test import test_host_import
host = test_host_import()

@cache
def test_host_main_exists():
  assert host.main
  return host.main

def test_host_funcs_exist():
  assert host.main
  assert host.step

def test_host_internal_funcs_exist():
  assert host._load
  assert host._print
  assert host._ping

def test_host_ping_works():
  assert host._ping
  host._ping(inactive=True, receiving=False)


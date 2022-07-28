from functools import cache
from .do_test import test_pi_import
pi = test_pi_import()

@cache
def test_pi_main_exists():
  assert pi.main
  return pi.main

@cache
def test_pi_step_exists():
  assert pi.step
  return pi.step


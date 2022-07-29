from functools import cache
from .do_test import test_pi_import
pi = test_pi_import()

@cache
def test_pi_main_exists():
  assert pi.main
  return pi.main

def test_pi_funcs_exists():
  assert pi.main
  assert pi.step

def test_pi_internel_funcs_exists():
  assert pi._step
  assert pi._method
  assert pi._step
  
def test_pi_internal_step():
  assert pi._step
  

# Test pings
# test _hidden funcs :)
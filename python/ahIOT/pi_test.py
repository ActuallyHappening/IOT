from functools import cache
from typing import Any, Callable, List, Tuple
import uuid
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
  # Check if method and callback are successful
  def method_callback(return_success: bool = True, **kwargs):
    def _method_callback(data: str, check_called: List[bool | None]) -> Callable[[], Tuple[bool, str]]:
      def __method_callback() -> Tuple[bool, str]:
        check_called[0] = True
        return return_success, data
      return __method_callback
    return _method_callback
  
  def callback_callback(
    *,
    return_success: bool = True,
    data_should_be_same: bool | None = None,
    **kwargs
  ):
    def _callback_callback(should_data: str, check_called: List[bool | None] = [None, None]) -> Callable[[str], bool]:
      def __callback_callback(passed_data: Any) -> bool:
        check_called[1] = True
        if data_should_be_same is True:
          assert should_data == passed_data
        elif data_should_be_same is False:
          assert should_data != passed_data
        return return_success
      return __callback_callback
    return _callback_callback

  def check_step(
    method_gen: Callable[[str, List[bool | None]], Callable[[], bool]],
    callback_gen: Callable[[str, List[bool | None]], Callable[[str], bool]],
    callback_states: Tuple[bool | None, bool | None] = (None, None),
  ):
    check_called: List[bool | None] = [False, False]
    id = str(uuid.uuid4())
    pi._step(
      method_gen(id, check_called),
      callback_gen(id, check_called),
    )
    for state_num, state in enumerate(callback_states):
      if state is not None:
        assert check_called[state_num] is state
  
  check_step(
    method_callback(return_success=True),
    callback_callback(return_success=True, data_should_be_same=True),
    callback_states=(True, True),
  )
  check_step(
    method_callback(return_success=True),
    callback_callback(return_success=False, data_should_be_same=True),
    callback_states=(True, True),
  )
  check_step(
    method_callback(return_success=False),
    callback_callback(return_success=True, data_should_be_same=True),
    callback_states=(True, False),
  )
  check_step(
    method_callback(return_success=False),
    callback_callback(return_success=False, data_should_be_same=True),
    callback_states=(True, False),
  )  

# Test pings
# test _hidden funcs :)
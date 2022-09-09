from functools import cache
from typing import Callable

def extract():
  try:
    from . import Extract_raw as extract
  except NotImplementedError as exc:
    import pytest
    pytest.skip(f"NotImplementedError: {exc}")
  assert extract
  return extract

def test_extract_funcs_exist(extract):
  assert extract.get_frame
  assert extract.main
  
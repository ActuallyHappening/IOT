from functools import cache
from typing import Callable
import pytest

@pytest.fixture
def extract():
  try:
    from . import Extract_raw as extract
  except NotImplementedError as exc:
    pytest.skip(f"NotImplementedError: {exc}")
  assert extract
  return extract

def test_extract_funcs_exist(extract):
  assert extract.get_frame
  assert extract.main
  
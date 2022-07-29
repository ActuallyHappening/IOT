from functools import cache
from typing import Callable

@cache
def test_extract_import():
  from . import Extract_raw as extract
  assert extract
  return extract

def require_extract(f: Callable) -> Callable:
  """
  Decorator to ensure import of module before calling function.
  """
  def wrapper(*args, **kwargs):
    extract = test_extract_import()
    return f(*args, extract=extract, **kwargs)
  return wrapper

@require_extract
def test_extract_funcs_exist(extract):
  assert extract.get_frame
  assert extract.main
  
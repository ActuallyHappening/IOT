

from functools import cache


@cache
def test_process_import():
  from . import Process_raw as raw
  assert raw
  return raw

def require_import(f: Callable) -> Callable:
  """
  Decorator to ensure import of module before calling function.
  """
  def wrapper(*args, **kwargs):
    raw = test_process_import()
    return f(*args, raw=raw, **kwargs)
  return wrapper

@require_import
def test_process_funcs_exists(raw):
  assert raw.iterate_frame
  assert raw.iterate
  assert raw.print_frame
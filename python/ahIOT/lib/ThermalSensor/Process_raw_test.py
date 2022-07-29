from functools import cache
import sys
from typing import Callable
import pytest
from rich import print as rprint

@cache
def test_process_import():
  from . import Process_raw as raw
  assert raw
  return raw

@pytest.fixture
def raw():
  return test_process_import()

def test_process_funcs_exists(raw):
  assert raw.iterate_frame
  assert raw.iterate
  assert raw.print_frame

def test_print_frame_value(raw, capfd):
    _list = [69, 42]
    raw.print_frame_value(_list[0], 0, 0, list=_list, dimensions=(2,1))
    capture1 = capfd.readouterr().out
    _avg = sum(_list) / len(_list)
    _colour = raw.generate_colour(69, avg=_avg)
    rprint(f"[{_colour}]{raw.ascii_chars[len(raw.ascii_chars)-1]}[/{_colour}]", end="")
    capture2 = capfd.readouterr().out
    assert capture1 == capture2
    
  
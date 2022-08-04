from cmd import do
try:
  import uasyncio as asio
except ImportError:
  import asyncio as asio

do("motor step 1")
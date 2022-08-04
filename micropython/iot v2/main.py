from cmd import do
try:
  import uasyncio as asio
except ImportError:
  import asyncio as asio

asio.gather(do("motor step 1"))
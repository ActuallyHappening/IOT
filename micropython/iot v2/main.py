from cmd import do
try:
  import uasyncio as asio
except ImportError:
  import asyncio as asio

do("forall motor forward")

# do("motor forward 1")
# do("motor forward 2")
# do("motor forward 3")
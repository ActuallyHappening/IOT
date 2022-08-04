from cmd.cmd import do
import asyncio as asio

asio.gather(do("motor step 1"))
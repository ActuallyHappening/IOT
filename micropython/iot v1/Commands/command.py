import uasyncio as asio


class Command():
    def __init__(self, asioDo, cleanup=lambda: ..., name=None):
        self.asioDo = asioDo
        self.cleanup = cleanup
        self.name = name

    def __str__(self):
        if self.name is None:
            return f"Command(...)"
        else:
            return f"Command(..., name={self.name})"

    def __repr__(self): return self.__str__()


def _timeoutWrapper(coroutine):
    async def __timeoutWrapper(*_args, time=..., **_kwargs):
        if time is not ...:
            await asio.wait_for(coroutine(*_args, **_kwargs), timeout=time)
        else:
            print(
                f"#>\tRunning __timeoutWrapper with no given time, defaulting to asio.gather(...)")
            await asio.gather(coroutine(*_args, **_kwargs))
    return __timeoutWrapper


def timeoutWrapper(func):
    async def __timeoutWrapper(*_args, time=..., **_kwargs):
        print(f"#>\tRunning timeoutWrapper (syncronous 'promoted' to async)")
        if time is not ...:
            await asio.wait_for(func(*_args, **_kwargs), timeout=time)
        else:
            print(
                f"#>\tRunning __timeoutWrapper with no given {time =}, defaulting to asio.gather(...)")
            await asio.gather(func(*_args, **_kwargs))
    return __timeoutWrapper

"""
This module aims to allow an arbitrary source of commands in a RESTable format
Use it like:
```py
from Commands import Commands as cmds

requested_thing_to_do = input("Get this from whatever")

cmds.execute(cmds.prebuilt["REST execute"]( requested_thing_to_do ))
```


"""

from .command import Command, _timeoutWrapper

RAW_STRUCTURE = {
    "Groups": {
        "Bluetooth": ["Begin", "Send", ],
        "Web Server Host": ["Begin", "Stop"],
        # "Web Server Connect": ["Begin", ],
        "Time": ["Start Timer", "Start Logger", ],
        "Machine": ["Pin", "Led", "Blink", ],
        "Generic": ["Nothing", "Wait", ],
        "REST": ["Execute", "Search", ],
    }}


class REST_COMMAND():
    def parse_from_spaces(self, txt, inputs="", *, seperator=" ", **options):
      # e.g. Web Server Host Begin =txt
        group = None
        arr = txt.split(seperator)
        for group_name in RAW_STRUCTURE["Groups"].keys():
            _group_name_len = len(group_name.split(" "))
            for i in range(len(arr) - _group_name_len + 1):
                if ' '.join(arr[i:i+_group_name_len]) == group_name:
                    group = group_name
                    break
            if group:
                break
        else:
            raise ValueError(
                f"**> Group {group} not found in RAW_STRUCTURE")
        # e.g. Web Server Host       =_group[]
        #      Web Server Host Begin =_verb []
        verb = "Search"
        _verb = arr
        _group_name = group.split(" ")
        for word in _verb:
            if word in _group_name:
                _verb[_verb.index(word)] = None
                _group_name[_group_name.index(word)] = None
        verb = seperator.join([i for i in _verb if i is not None])
        return group, verb

    def parse_from_url():
        ...  # TODO implement for ServerCommands.py

    def __init__(self, group=None, verb=None, *inputs, **options):
        self.group = group or ("REST Search")
        if self.group not in RAW_STRUCTURE["Groups"]:
            raise ValueError(
                f"**> Group {self.group} not found in RAW_STRUCTURE")
        self.verb = verb
        if self.verb not in RAW_STRUCTURE["Groups"][self.group]:
            raise ValueError(
                f"**> Verb {self.verb} not found in RAW_STRUCTURE under group {self.group}")
        self.inputs = inputs
        self.options = options

    @property
    def name(self):
        return f"{self.group} {self.verb}"


@_timeoutWrapper
async def REST_execute(*, logger=print, __constructor__=..., **kwargs):
    _command = ...
    if __constructor__ is ...:
        __constructor__ = f"REST Search"
    if type(__constructor__) is dict
    if "REST_COMMAND" in __constructor__:
        __constructor__ = REST_COMMAND(
            __constructor__["REST_COMMAND"], parse=True)
    logger(f"*> Parsing {__constructor__=} ...")

commands = {
    'REST execute': Command(REST_execute),
}

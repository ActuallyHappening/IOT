import json
import re
import uasyncio as asio
from microdot import Microdot
from microdot_asyncio import Microdot as asio_Microdot
import secrets
from extensions import _dict_add
from . import Commands
from .command import Command, _timeoutWrapper, timeoutWrapper

app = asio_Microdot()

API_CONST = "/api/v1.1"

META_FROM_CONST = f"<ESP32 id:{secrets.get_esp_id()}"
META_TO_CONST = f"receiver"
META_DEVICE_CONST = f"ESP32 API"
META_DEFAULT = {"from": META_FROM_CONST,
                "to": META_TO_CONST, "device": META_DEVICE_CONST}

commandQueue = []
__queuePollPeriod = 5
__queueStop = False

logger = print


@app.route('/')
async def ping(request):
    logger("YIPEE!")
    return json.dumps({"__meta__": META_DEFAULT, "payload": {"ping": "pong"}})


async def __commandQueueTask():
    global __queueStop
    global commandQueue
    try:
        while True:
            if len(commandQueue) > 0:
                task = commandQueue.pop(0)
                Commands.execute(task[0], *task[1], **task[2])
            await asio.sleep(__queuePollPeriod)
            if __queueStop:
                __queueStop = False
                break
    except Exception as exc:
        logger(f"#<\t__commandQueueTask Stopped: {exc}")

# TODO: Add '/' and '' ending support, maybe app.routes to implement /.../v__meta__ and /.../v__meta__/


@app.routes('/api/v__meta__/', methods=["GET"])
async def dump_all(request):
    return json.dumps({"__meta__": META_DEFAULT, "payload": {"__version__": API_CONST, "routes": [x for x in app.url_map]}})


@app.route(f'{API_CONST}/execute-command/<string:command_name>')
async def request_execute_command(request, *, command_name="Nothing"):
    logger("## Command queue request ...")
    if "prebuilt" in request.args:
        if request.args["prebuilt"] not in Commands.prebuilt:
            return f"Error Code 50something\nUnknown command {request.args['prebuilt']=}"
        requested_command = Commands.prebuilt[request.args["prebuilt"]]
        _time = 5
        if "time" in request.args:
            _time = int(request.args["time"])
        else:
            logger(f"#>\tDefaulting to {_time=}")
        logger(f"### Queueing task {requested_command.name}")
        commandQueue.append([requested_command, [], {"time": _time}])
        return json.dumps({"__meta__": META_DEFAULT, "payload": {"status": "queued", "time": _time, "requested_command.name": requested_command.name}})
    else:
        return "Error Code 40something\nUnknown options, use `.../execute-command/?prebuilt=Blink Builtin`\nWOW this API is COOL AS F**K!"


@app.route(f"{API_CONST}/search-commands/<string:search>")
async def request_find_commands(request, *, search="*"):
    logger(f"##! Command search requested ...")
    if search == "*":
        return json.dumps({"__meta__": META_DEFAULT, "payload": {"commands": [x for x in Commands.prebuilt.values()]}})
    else:
        try:
            search = re.compile(search)
        except Exception as exc:
            return f"Error Code 60something\nInvalid search regex: {exc}"
        try:
            return json.dumps({"__meta__": META_DEFAULT, "payload": {"matches":
                                                                     [Commands.prebuilt[index] for index in Commands.prebuilt.keys(
                                                                     ) if re.match(search, Commands.prebuilt.name)]
                                                                     }})
        except Exception as exc:
            return json.dumps({"__meta__": _dict_add(META_DEFAULT, {"error": "Unknown Server Error", "error_exc": f"{exc=}"}), "payload": {"matches": []}})


@_timeoutWrapper
async def start_server(*, port=8080, host="0.0.0.0", **kwargs):
    global logger  # Easiest (hacky) way to get the logger to work
    if "logger" in kwargs:
        logger = kwargs["logger"]
        logger(f"#>\tLogger set to {logger=}")
    try:
        logger(f"#>\tStarting microdot server --async ...")
        await asio.gather(__commandQueueTask(), app.start_server(host='0.0.0.0', port=420, debug=True))
    finally:
        app.shutdown()
        logger(f"#>\tShutdown microdot server --async")


commands = {
    "npm run dev": Command(start_server),
}

from microdot_asyncio import Microdot

app = Microdot()


@app.route("/")
def testing(request):
    return "<h1>Hello World!</h1>"


app.run(host='0.0.0.0', port=420, debug=True)

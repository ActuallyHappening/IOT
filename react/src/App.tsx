import { createContext, CSSProperties, useContext, useEffect, useState } from 'react'
import Cell from './components/Cell'
// require('dotenv').config() // Load .env files

const defaultDimensions = [32, 24] // X, Y

type Colours = CSSProperties['color']
const _defaultFrame: number[][] = []
for (let y = 0; y < defaultDimensions[1]; y++) {
  _defaultFrame[y] = []
  for (let x = 0; x < defaultDimensions[0]; x++) {
    _defaultFrame[y][x] = Math.random() > 0.5 ? 1 : 0
  }
}

const Aio = (username: string, key: string) => {
  return async (group: string, feed: string) => {
    const url = `https://io.adafruit.com/api/v2/${username}/feeds/${group}.${feed}/data?limit=1`
    const res = await fetch(url, {
      headers: {
        'X-AIO-Key': key,
      },
    })
    const data = await res.json()
    // console.log("_data", data)
    return data[0].value
  }
}

const _env_vars = import.meta.env
if (!_env_vars.VITE_ADAFRUIT_IO_USERNAME) {
  // throw new Error('AIO_USERNAME is not set')
  console.log("AIO_USERNAME is not set, requiring dynamic key")
}
const _username: boolean | string = _env_vars.VITE_ADAFRUIT_IO_USERNAME ?? undefined
if (!_env_vars.VITE_ADAFRUIT_IO_KEY) {
  // throw new Error('AIO_KEY is not set')
  console.log("AIO_KEY is not set, requiring dynamic key")
}
const _key = _env_vars.VITE_ADAFRUIT_IO_KEY ?? undefined

export const Credentials = createContext<{username: undefined|string, key: undefined|string}>({
  username: _username,
  key: _key,
})

function App({
  group = "brad",
  feed = "ir-stream",
}: {
  group?: string,
  feed?: string,
}) {
  const [frame, setFrame] = useState(_defaultFrame)

  const frameTotal = frame.reduce((acc, row) => {
    return acc += row.reduce((acc, cell) => acc += cell, 0)
  }, 0)
  const frameAverage = frameTotal / (defaultDimensions[0] * defaultDimensions[1])

  const { username, key } = useContext(Credentials)
  const [_username, _setUsername] = useState<string>(username ?? "Not set")
  const [_key, _setKey] = useState<string>(username ?? "Not set")
  let _show_dynamic_form = false
  let aio = async (g:string,f:string): Promise<string> => {
    console.log("AIO api call not signed in for group:feed", g, f)
    return JSON.stringify({"stream": _defaultFrame})
  }
  if (!username || !key) {
    _show_dynamic_form = true
  } else {
    aio = Aio(username, key)
  }

  const _retrieve_stream = async (): Promise<number[][]> => {
    const value = await aio(group, feed)
    // console.log("value", value)
    let frame = []
    try {
      frame = JSON.parse(value).stream
    } catch (e) {
      // console.log("JSON parse error", e)
      return _defaultFrame
    }
    // console.log("Successful jsonify", frame)
    const parsed_frame: number[][] = []

    // Concert to 2D array
    for (let y = 0; y < defaultDimensions[1]; y++) {
      parsed_frame[y] = []
      for (let x = 0; x < defaultDimensions[0]; x++) {
        parsed_frame[y][x] = frame[y * defaultDimensions[0] + x]
      }
    }

    // console.log("parse?:", parsed_frame)
    if (parsed_frame.length !== defaultDimensions[1]) {
      throw new Error("Frame given is not the correct height!")
    }
    console.log("Parsed Successfully!")
    return parsed_frame
  }

  useEffect(() => {
    const cleanup = setInterval(() => _retrieve_stream().then(setFrame), 1000)
    return () => clearInterval(cleanup)
  })

  const getColour = (value: number) => {
    if (value < frameAverage) {
      return "red"
    } else if (value > frameAverage) {
      return "green"
    } else {
      return "yellow"
    }
  }

  return (
    <>
    {/* <h2>oops</h2> */}
    {/* <Cell pos={[0, 0]} colour={getColour(frame[0][0])} /> */}
    <form
      style={{
        display: _show_dynamic_form ? "block" : "none",
        left: "90%",
        top: "10%",
        position: "absolute",
      }}
      onSubmit={(e) => {
        e.preventDefault()
        setContext({ username: _username, key: _key })
      }}
    >
      <label>Username:</label>
      <input type="text" name="username" />
      <label>Key:</label>
      <input type="text" name="key" />
      <button type="submit">Submit</button>
    </form>
    <div style={{
      position: "absolute",
      top: "10%",
      left: "10%",
      width: "80%",
      height: "80%",
      backgroundColor: "black",
      border: "1px solid black",
    }}></div>
    {frame.map((row, y) => {
      return row.map((cell, x) => {
        return <Cell pos={[y, x]} colour={getColour(cell)} />
      })
    }
    )}
    </>
  )
}

export default App

export const setContext = ({ username, key }: { username: string, key: string }) => {
  setContext({ username, key })
}

export const setContext = ({ username, key }: { username: string, key: string }) => {
  setContext({ username, key })
}

export const setContext = ({ username, key }: { username: string, key: string }) => {
  setContext({ username, key })
}

export const setContext = ({ username, key }: { username: string, key: string }) => {
  setContext({ username, key })
}

export const setContext = ({ username, key }: { username: string, key: string }) => {
  setContext({ username, key })
}

export const setContext = ({ username, key }: { username: string, key: string }) => {
  setContext({ username, key })
}
    >
      <label>
        Enter AIO Username:
        <input type="text" name="username" />
      </label>
      <label>
        Enter AIO Key:
        <input type="text" name="key" />
      </label>
      <input type="submit" value="Submit" />
    </form>
    {frame.map((row, y) => {
      return row.map((cell, x) => {
        return <Cell key={String(x) + String(y)} pos={[x, y]} colour={getColour(cell)} />
        // return <h1>y</h1>
      })
    })}
    </>
  )
}

export default App

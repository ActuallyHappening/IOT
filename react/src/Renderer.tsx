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

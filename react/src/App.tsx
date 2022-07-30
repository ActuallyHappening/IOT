import { CSSProperties, useEffect, useState } from 'react'
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
    const url = `https://io.adafruit.io/api/v2/${username}/feeds/${group}.${feed}/data?limit=1`
    const res = await fetch(url, {
      headers: {
        'X-AIO-Key': key,
      },
    })
    const data = await res.json()
    return data.value
  }
}
const _env_vars = import.meta
console.log(_env_vars)
if (!_env_vars.ADAFRUIT_IO_USERNAME) {
  throw new Error('AIO_USERNAME is not set')
}
if (!_env_vars.ADAFRUIT_IO_KEY) {
  throw new Error('AIO_KEY is not set')
}
const aio = Aio(_env_vars.ADAFRUIT_IO_USERNAME, _env_vars.ADAFRUIT_IO_KEY)

function App({
  group = "brad",
  feed = "ir-stream",
}: {
  group?: string,
  feed?: string,
}) {
  const [frame, setFrame] = useState(_defaultFrame)
  // console.log(frame)
  const frameTotal = frame.reduce((acc, row) => {
    return acc += row.reduce((acc, cell) => acc += cell, 0)
  }, 0)
  const frameAverage = frameTotal / (defaultDimensions[0] * defaultDimensions[1])

  const _retrieve_stream = async () => {
    const value = await aio(group, feed)
    const data = JSON.parse(value)
    return data
  }

  useEffect(() => {
    _retrieve_stream().then(data => {
      console.log(data)
    })
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
        return <Cell pos={[x, y]} colour={getColour(cell)} />
        // return <h1>y</h1>
      })
    })}
    </>
  )
}

export default App

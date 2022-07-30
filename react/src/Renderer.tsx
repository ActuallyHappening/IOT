import { createContext, CSSProperties, useContext, useEffect, useState } from 'react'
import Cell from './components/Cell'
import { Credentials } from './CredentialProvider'
import { defaultDimensions, defaultFrame, getFrameAverage, getFrameTotal } from './lib/ThermalCam'
// require('dotenv').config() // Load .env files

type Colours = CSSProperties['color']

function App({
  group = "brad",
  feed = "ir-stream",
}: {
  group?: string,
  feed?: string,
}) {
  const [frame, setFrame] = useState(defaultFrame)

  const frameTotal = getFrameTotal(frame)
  const frameAverage = getFrameAverage(frame, frameTotal)

  const aio = useContext(Credentials)

  const _retrieve_stream = async (): Promise<number[][]> => {
    const value = await aio(group, feed)
    // console.log("value", value)
    let frame = []
    try {
      frame = JSON.parse(value).stream
    } catch (e) {
      // console.log("JSON parse error", e)
      return defaultFrame
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
function _defaultFrame(_defaultFrame: any): [any, any]
{
  throw new Error('Function not implemented.')
}


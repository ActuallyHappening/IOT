import { createContext, CSSProperties, useContext, useEffect, useState } from 'react'
import Cell from '../Cell'
import { defaultDimensions, defaultFrame, getFrameAverage, getFrameTotal, ProcessFrame } from './ThermalCam'
import { aio as _aio } from '../../lib/AIO'

function App({
  group = "brad",
  feed = "ir-stream",
}: {
  group?: string,
  feed?: string,
}) {
  const [frame, setFrame] = useState(defaultFrame)

  const aio = useContext(_aio)

  const _retrieve_stream = async (): Promise<[number, number][][]> => {
    // console.warn("_retrieve_stream", group, feed, aio)

    const value = await aio(group, feed)

    let frame = []
    try {
      frame = JSON.parse(value).stream
    } catch (e) {
      console.error("While _retrieve_stream json parsing, encountered e=", e, "with value=", value)
      return defaultFrame
    }

    const parsed_frame: [number, number][][] = []

    // Concert to 2D array
    for (let y = 0; y < defaultDimensions[1]; y++) {
      parsed_frame[y] = []
      for (let x = 0; x < defaultDimensions[0]; x++) {
        parsed_frame[y][x] = [0, frame[y * defaultDimensions[0] + x]]
      }
    }

    if (parsed_frame.length !== defaultDimensions[1]) {
      throw new Error("Frame given is not the correct height!")
    }

    return parsed_frame
  }

  useEffect(() => {
    // _retrieve_stream().then(setFrame)
    const cleanup = setInterval(() => _retrieve_stream().then((newFrame) => {
      setFrame(ProcessFrame(newFrame))
    }), 1000)
    return () => clearInterval(cleanup)
  })

  return (
    <>
    {/* <h2>oops</h2> */}
    {/* <Cell pos={[0, 0]} colour={getColour(frame[0][0])} /> */}
    {frame.map((row, y) => {
      return row.map((cell, x) => {
        return <Cell key={String(x) + ":" + String(y)} pos={[x, y]} colour={cell[0]} value={cell[1]} />
        // return <h1>y</h1>
      })
    })}
    </>
  )
}

export default App

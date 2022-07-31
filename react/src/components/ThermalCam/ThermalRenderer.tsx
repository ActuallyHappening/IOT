import { createContext, CSSProperties, useContext, useEffect, useState } from 'react'
import Cell from '../Cell'
import { defaultDimensions, defaultFrame, defaultRawFrame, getFrameAverage, getFrameTotal, ProcessFrame, T_streamRaw } from './ThermalCam'
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

  const retrieve_stream = async (): Promise<T_streamRaw> => {
    const value = await aio(group, feed)

    let frame = []
    try {
      frame = JSON.parse(value).stream
    } catch (e) {
      console.error("While _retrieve_stream json parsing, encountered e=", e, "with value=", value)
      return defaultRawFrame
    }

    const parsed_frame: T_streamRaw = []

    // Concert to 2D array
    for (let y = 0; y < defaultDimensions[1]; y++) {
      parsed_frame[y] = []
      for (let x = 0; x < defaultDimensions[0]; x++) {
        parsed_frame[y][x] = frame[y * defaultDimensions[0] + x]
      }
    }

    if (parsed_frame.length !== defaultDimensions[1]) {
      console.error("Frame given is not the correct height!")
      return defaultRawFrame
    }

    return parsed_frame
  }

  useEffect(() => {
    const cleanup = setInterval(() => retrieve_stream().then((newFrame) => {
      setFrame(ProcessFrame(newFrame))
    }), 1000)
    return () => clearInterval(cleanup)
  })

  return (
    <>
    {frame.map((row, y) => {
      return row.map((cell, x) => {
        return <Cell key={String(x) + ":" + String(y)} pos={[x, y]} colour={cell[1]} value={cell[0]} />
      })
    })}
    </>
  )
}

export default App

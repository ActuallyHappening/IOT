import { createContext, CSSProperties, useContext, useEffect, useState } from 'react'
import Cell from './components/Cell'
import { Credentials } from './components/credentials/CredentialProvider'
import { defaultDimensions, defaultFrame, getFrameAverage, getFrameTotal, Process } from './lib/ThermalCam'

function App({
  group = "brad",
  feed = "ir-stream",
}: {
  group?: string,
  feed?: string,
}) {
  const [frame, setFrame] = useState(defaultFrame)

  const aio = useContext(Credentials)
  // console.log("aio CONTEXT:: ", aio)

  const _retrieve_stream = async (): Promise<[number, number][][]> => {
    // console.warn("_retrieve_stream", group, feed, aio)

    // throw "Not implemented -:)"

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
    const parsed_frame: [number, number][][] = []

    // Concert to 2D array
    for (let y = 0; y < defaultDimensions[1]; y++) {
      parsed_frame[y] = []
      for (let x = 0; x < defaultDimensions[0]; x++) {
        parsed_frame[y][x] = [0, frame[y * defaultDimensions[0] + x]]
      }
    }

    // console.log("parse?:", parsed_frame)
    if (parsed_frame.length !== defaultDimensions[1]) {
      throw new Error("Frame given is not the correct height!")
    }
    // console.log("Parsed Successfully!")
    // console.log("Parsed Successfully!", parsed_frame)
    return parsed_frame
  }

  useEffect(() => {
    // _retrieve_stream().then(setFrame)
    const cleanup = setInterval(() => _retrieve_stream().then((newFrame) => {
      setFrame(Process(newFrame))
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

import { CSSProperties, useState } from 'react'
import Cell from './components/Cell'

const defaultDimensions = [32, 24] // X, Y

type Colours = CSSProperties['color']
const _defaultFrame: number[][] = []
for (let y = 0; y < defaultDimensions[1]; y++) {
  _defaultFrame[y] = []
  for (let x = 0; x < defaultDimensions[0]; x++) {
    _defaultFrame[y][x] = Math.random() > 0.5 ? 1 : 0
  }
}

function App() {
  const [frame, setFrame] = useState(_defaultFrame)
  console.log(frame)
  const frameTotal = frame.reduce((acc, row) => {
    return acc += row.reduce((acc, cell) => acc += cell, 0)
  }, 0)
  const frameAverage = frameTotal / (defaultDimensions[0] * defaultDimensions[1])

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

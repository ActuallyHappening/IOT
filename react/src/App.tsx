import { CSSProperties, useState } from 'react'
import Cell from './components/Cell'

const defaultDimensions = [32, 24] // X, Y

type Colours = CSSProperties['color']
const _defaultFrame: number[][] = []
for (let y = 0; y < defaultDimensions[1]; y++) {
  _defaultFrame[y] = []
  for (let x = 0; x < defaultDimensions[0]; x++) {
    _defaultFrame[y][x] = [0, "red"]
  }
}

function App() {
  const [frame, setFrame] = useState(_defaultFrame)
  const frameTotal = frame.reduce((acc, row) => {
    return acc += row.reduce((acc, cell) => acc += cell, 0)
  }, 0)
  const frameAverage = frameTotal / (defaultDimensions[0] * defaultDimensions[1])

  const getColour = (value: number) => {
    if (value < frameAverage) {
      return "red"
    } else if (value > frameAverage) {
      return "green"
    }
  }

  return (
    <>
    {frame.map((row, y) => {
      row.map((cell, x) => {
        return <Cell pos={[x, y]} colour={getColour(cell)} />
      })
    })}
    </>
  )
}

export default App

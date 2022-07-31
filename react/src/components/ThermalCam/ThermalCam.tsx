
export type T_streamProcessed = [number, number][][]
export type T_streamPreprocessed = T_streamProcessed
export type T_streamRaw = number[][]
export type T_streamAny = T_streamRaw | T_streamPreprocessed | T_streamProcessed

export const defaultDimensions = [32, 24] // X, Y
export const _lowestTemp = 0
export const _highestTemp = 70

export const processedForEach = (frame: T_streamProcessed, callback: (cell: [number, number], x: number, y: number) => void) => {
  for (let y = 0; y < defaultDimensions[1]; y++) {
    frame[y] = frame[y] || []
    for (let x = 0; x < defaultDimensions[0]; x++) {
      callback(frame[y][x], x, y)
    }
  }
}
export const rawForEach = (frame: T_streamRaw, callback: (cell: number, x: number, y: number) => void) => {
  for (let y = 0; y < defaultDimensions[1]; y++) {
    frame[y] = frame[y] || []
    for (let x = 0; x < defaultDimensions[0]; x++) {
      callback(frame[y][x], x, y)
    }
  }
}

const _defaultFrame: T_streamProcessed = []
processedForEach(_defaultFrame, (cell, x, y) => {
  _defaultFrame[y] = _defaultFrame[y] || []
  _defaultFrame[y][x] = [69, Math.random() > 0.5 ? 1 : 0]
})
export const defaultFrame: T_streamProcessed = _defaultFrame

const _defaultRawFrame: T_streamRaw = []
rawForEach(_defaultRawFrame, (cell, x, y) => {
  _defaultRawFrame[y] = _defaultRawFrame[y] || []
  _defaultRawFrame[y][x] = (Math.random() + 1) * 25
})
export const defaultRawFrame: T_streamRaw = _defaultRawFrame

export const getFrameTotal = (frame: T_streamPreprocessed) => {
  return frame.reduce((acc, row) => {
    return acc += row.reduce((acc, cell) => {
      return typeof cell === "number" ? acc + cell : acc += cell[0]
    }, 0)
  }, 0)
}

export const getFrameAverage = (frame: T_streamPreprocessed, total?: number): number => {
  return (total ?? getFrameTotal(frame)) / (defaultDimensions[0] * defaultDimensions[1])
}

export const getFrameMin = (frame: T_streamPreprocessed): number => {
  return frame.reduce((acc, row) => {
    return row.reduce((acc, _cell) => {
      const cell = typeof _cell === "number" ? _cell : _cell[0]
      if (cell < _lowestTemp) return acc
      if (cell > _highestTemp) return acc
      return Math.min(acc, cell)
    }, acc)
  }, Infinity)
}

export const getFrameMax = (frame: T_streamPreprocessed): number => {
  return frame.reduce((acc, row) => {
    return row.reduce((acc, cell) => {
      return typeof cell === "number" ? Math.max(acc, cell) : Math.max(acc, cell[0])
    }, acc)
  }, -Infinity)
}

export const mapRange = (value: number, low1: number, high1: number, low2: number, high2: number) => {
  return low2 + (high2 - low2) * (value - low1) / (high1 - low1);
}

export const ProcessFrame = (_frame: T_streamRaw): T_streamProcessed => {
  const frame: T_streamProcessed = []

  // Convert to 2D array
  // @ts-ignore
  const total = getFrameTotal(_frame)
  // @ts-ignore
  const average = getFrameAverage(_frame, total)
  // @ts-ignore
  const min = Math.max(getFrameMin(_frame), _lowestTemp)
  // @ts-ignore
  const max = Math.min(getFrameMax(_frame), _highestTemp)

  console.log("ProcessFrame", { total, average, min, max })

  rawForEach(_frame, (cell, x, y) => {
    frame[y] = frame[y] ?? []
    const colourValue = mapRange(cell, min, max, 0, 255)
    // console.log("ProcessFrame", { cell, x, y, colourValue })
    frame[y][x] = [cell, colourValue]
  })
  return frame
}
export const defaultDimensions = [32, 24] // X, Y

const _defaultFrame: number[][] = []
for (let y = 0; y < defaultDimensions[1]; y++) {
  _defaultFrame[y] = []
  for (let x = 0; x < defaultDimensions[0]; x++) {
    _defaultFrame[y][x] = Math.random() > 0.5 ? 1 : 0
  }
}

export const getFrameTotal = (frame: number[][]) => {
  return frame.reduce((acc, row) => {
    return acc += row.reduce((acc, cell) => acc += cell, 0)
  }, 0)
}

export const getFrameAverage = (frame: number[][], total?: number): number => {
  return (total ?? getFrameTotal(frame)) / (defaultDimensions[0] * defaultDimensions[1])
}

export const defaultFrame = _defaultFrame
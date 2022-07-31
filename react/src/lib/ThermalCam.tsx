export const defaultDimensions = [32, 24] // X, Y

const _defaultFrame: [number, number][][] = []
for (let y = 0; y < defaultDimensions[1]; y++) {
  _defaultFrame[y] = []
  for (let x = 0; x < defaultDimensions[0]; x++) {
    _defaultFrame[y][x] = [69, Math.random() > 0.5 ? 1 : 0]
  }
}

export const getFrameTotal = (frame: [number, number][][]) => {
  return frame.reduce((acc, row) => {
    return acc += row.reduce((acc, cell) => acc += cell[0], 0)
  }, 0)
}

export const getFrameAverage = (frame: [number, number][][], total?: number): number => {
  return (total ?? getFrameTotal(frame)) / (defaultDimensions[0] * defaultDimensions[1])
}

export const mapRange = (value: number, low1: number, high1: number, low2: number, high2: number) => {
  return low2 + (high2 - low2) * (value - low1) / (high1 - low1);
}

export const Process = (frame: [number, number][][]): [number, number][][] => {
  const total = getFrameTotal(frame)
  const average = getFrameAverage(frame, total)
  const newFrame: [number, number][][] = []
  for (let y = 0; y < defaultDimensions[1]; y++) {
    newFrame[y] = []
    for (let x = 0; x < defaultDimensions[0]; x++) {
      const value = frame[y][x]
      const newValue = mapRange(value[0], 0, 70, 0, 255)
      newFrame[y][x] = [value[0], newValue]
    }
  }
  return newFrame
}

export const defaultFrame = _defaultFrame
import React, { CSSProperties } from 'react'

const Cell = ({
  pos,
  colour = undefined,
  scale = 25,
  value = "",
}: {
  pos: [number, number],
  colour: string | number | undefined,
  // colour: CSSProperties['color'],
  scale?: number,
  value?: string | number,
}) => {
  const getColour = (value: string | number | undefined) => {
    if (typeof value === "string") {
      return value
    } else if (typeof value === "number") {
      return `rgb(${value}, 0, 0)`
    } else {
      return `rgba(0, 0, 0, 0)`
    }
  }
  return (
    <div style={{
      position: 'absolute',
      top: pos[0] * scale,
      left: pos[1] * scale,
      width: scale,
      height: scale,
      backgroundColor: getColour(colour),
      // border: '1px solid black',
      overflow: 'hidden',
    }}>{String(value).substring(0, 2)}</div>
  )
}

export default Cell
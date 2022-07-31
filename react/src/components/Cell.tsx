import React, { CSSProperties } from 'react'

const Cell = ({
  pos,
  colour = "black",
  scale = 25,
  value = "",
}: {
  pos: [number, number],
  colour: string | number,
  // colour: CSSProperties['color'],
  scale?: number,
  value?: string | number,
}) => {
  return (
    <div style={{
      position: 'absolute',
      top: pos[0] * scale,
      left: pos[1] * scale,
      width: scale,
      height: scale,
      backgroundColor: `rgba(${colour}, 0, 0, ${value > 70 || value < 0 ? 0 : 1})`,
      // backgroundColor: colour,
      border: '1px solid black'
    }}>{String(value)}</div>
  )
}

export default Cell
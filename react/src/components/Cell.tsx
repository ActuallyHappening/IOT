import React, { CSSProperties } from 'react'

const Cell = ({
  pos,
  colour = "black",
  scale = 25,
}: {
  pos: [number, number],
  colour: CSSProperties['color'],
  scale?: number,
}) => {
  return (
    <div style={{
      position: 'absolute',
      top: pos[0] * scale,
      left: pos[1] * scale,
      width: scale,
      height: scale,
      backgroundColor: colour,
      border: '1px solid black'
    }}>T</div>
  )
}

export default Cell
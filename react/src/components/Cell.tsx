import React, { CSSProperties } from 'react'

const Cell = ({pos, colour}: {
  pos: [number, number],
  colour: CSSProperties['color']
}) => {
  return (
    <div style={{
      position: 'absolute',
      top: pos[0] * 10,
      left: pos[1] * 10,
      width: 10,
      height: 10,
      backgroundColor: colour,
      border: '1px solid black'
    }}>X</div>
  )
}

export default Cell
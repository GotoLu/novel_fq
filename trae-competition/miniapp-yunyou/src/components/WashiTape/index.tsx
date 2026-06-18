import React from 'react'
import { View } from '@tarojs/components'
import styles from './index.module.scss'

interface Props {
  color?: string
  rotate?: number
  width?: number
  height?: number
  top?: number | string
  right?: number | string
  left?: number | string
  bottom?: number | string
  position?: 'absolute' | 'relative'
}

/** 和纸胶带装饰（CSS 实现） */
const WashiTape: React.FC<Props> = ({
  color = 'rgba(232,137,92,0.55)',
  rotate = -8,
  width = 100,
  height = 22,
  top, right, left, bottom,
  position = 'absolute'
}) => {
  return (
    <View
      className={styles.tape}
      style={{
        background: color,
        width: `${width}rpx`,
        height: `${height}rpx`,
        top, right, left, bottom,
        position,
        transform: `rotate(${rotate}deg)`
      }}
    />
  )
}

export default WashiTape

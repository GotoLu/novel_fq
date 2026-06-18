import React, { useEffect, useRef } from 'react'
import { View } from '@tarojs/components'
import styles from './index.module.scss'

interface Props {
  count?: number    // 柱条数 10-15
  active?: boolean  // 是否跳动
  height?: number   // 容器高度 px
}

/** 实时语音波形（CSS 错峰 delay 实现） */
const VoiceWave: React.FC<Props> = ({ count = 15, active = true, height = 56 }) => {
  const heightsRef = useRef<number[]>([])
  // 初始化 15 根随机高度
  if (heightsRef.current.length === 0) {
    heightsRef.current = Array.from({ length: 20 }, () => 0.3 + Math.random() * 0.7)
  }
  return (
    <View className={styles.bars} style={{ height: `${height}rpx` }}>
      {Array.from({ length: count }).map((_, i) => {
        const h = Math.round(heightsRef.current[i] * height)
        const delay = (i * 0.07).toFixed(2)
        return (
          <View
            key={i}
            className={`${styles.bar} ${active ? styles.active : ''}`}
            style={{
              height: `${h}rpx`,
              animationDelay: `${delay}s`
            }}
          />
        )
      })}
    </View>
  )
}

export default VoiceWave

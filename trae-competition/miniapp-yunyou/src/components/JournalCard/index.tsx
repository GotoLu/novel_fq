import React from 'react'
import { View, Text, Image } from '@tarojs/components'
import Taro from '@tarojs/taro'
import classnames from 'classnames'
import type { JournalEntry } from '@/types/journal'
import WashiTape from '@/components/WashiTape'
import styles from './index.module.scss'

interface Props {
  entry: JournalEntry
  onLike?: (id: string) => void
  onTap?: (id: string) => void
}

/** 手账条目卡片（含装饰 + 时间 + 地点 + 标签 + 配图 + 点赞） */
const JournalCard: React.FC<Props> = ({ entry, onLike, onTap }) => {
  const handleLike = (e: any) => {
    e?.stopPropagation?.()
    onLike?.(entry.id)
    Taro.vibrateShort({ type: 'light' }).catch(() => {})
  }
  const handleTap = () => onTap?.(entry.id)

  return (
    <View className={styles.card} onClick={handleTap}>
      <View className={styles.header}>
        <View className={styles.dateWrap}>
          <Text className={styles.dateDay}>{entry.date.split('.')[2]}</Text>
          <Text className={styles.dateMonth}>{entry.date.split('.')[0]}.{entry.date.split('.')[1]}</Text>
        </View>
        <View className={styles.titleWrap}>
          <Text className={styles.title}>{entry.title}</Text>
          <View className={styles.metaRow}>
            <Text className={styles.metaItem}>🕓 {entry.time}</Text>
            <Text className={styles.metaItem}>📍 {entry.location}</Text>
            {entry.weather && <Text className={styles.metaItem}>🌤 {entry.weather}</Text>}
          </View>
        </View>
        <WashiTape top="6rpx" right="6rpx" rotate={20} color="rgba(232,137,92,0.45)" width={80} height={20} />
      </View>

      {entry.images[0] && (
        <View className={styles.imgWrap}>
          <Image className={styles.img} src={entry.images[0]} mode="aspectFill" />
        </View>
      )}

      <Text className={styles.content}>{entry.content}</Text>

      <View className={styles.tagsRow}>
        {entry.tags.map((t, i) => (
          <View key={i} className={styles.tag}>
            <Text className={styles.tagText}>#{t}</Text>
          </View>
        ))}
      </View>

      <View className={styles.footer}>
        <View
          className={classnames(styles.likeBtn, entry.isLiked && styles.liked)}
          onClick={handleLike}
        >
          <Text className={styles.likeIcon}>{entry.isLiked ? '❤️' : '🤍'}</Text>
          <Text className={styles.likeCount}>{entry.likes}</Text>
        </View>
        <View className={styles.actionBtn}>
          <Text className={styles.actionText}>分享</Text>
        </View>
      </View>
    </View>
  )
}

export default JournalCard

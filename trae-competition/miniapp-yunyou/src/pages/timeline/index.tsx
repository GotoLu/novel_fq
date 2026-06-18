import React, { useState } from 'react'
import { View, Text, ScrollView } from '@tarojs/components'
import Taro from '@tarojs/taro'
import JournalCard from '@/components/JournalCard'
import { mockJournals, mockCurrentUser } from '@/data/mockJournals'
import type { JournalEntry } from '@/types/journal'
import styles from './index.module.scss'

const TimelinePage: React.FC = () => {
  const [entries, setEntries] = useState<JournalEntry[]>(mockJournals)

  const handleLike = (id: string) => {
    setEntries(prev => prev.map(e =>
      e.id === id
        ? { ...e, isLiked: !e.isLiked, likes: e.isLiked ? e.likes - 1 : e.likes + 1 }
        : e
    ))
  }

  const handleTap = (id: string) => {
    console.log('[Timeline] tap journal', id)
    Taro.navigateTo({ url: `/pages/detail/index?id=${id}` })
  }

  const handleRecord = () => {
    console.log('[Timeline] go to record')
    Taro.switchTab({ url: '/pages/record/index' })
  }

  return (
    <View className={styles.page}>
      <ScrollView scrollY enhanced showScrollbar={false}>
        <View className={styles.hero}>
          <Text className={styles.heroGreeting}>下午好，{mockCurrentUser.nickname} ✨</Text>
          <Text className={styles.heroTitle}>
            走过的 {mockCurrentUser.totalCities} 座城市，{'\n'}
            <Text className={styles.heroAccent}>都是你的手账</Text>
          </Text>
          <Text className={styles.heroSub}>按一下麦克风，把今天的见闻说给 AI 听，回家就是一本精装游记。</Text>

          <View className={styles.statRow}>
            <View className={styles.statCard}>
              <Text className={styles.statNum}>{mockCurrentUser.totalDays}</Text>
              <Text className={styles.statLabel}>旅程天数</Text>
            </View>
            <View className={styles.statCard}>
              <Text className={styles.statNum}>{mockCurrentUser.totalEntries}</Text>
              <Text className={styles.statLabel}>手账条数</Text>
            </View>
            <View className={styles.statCard}>
              <Text className={styles.statNum}>{mockCurrentUser.totalCities}</Text>
              <Text className={styles.statLabel}>城市足迹</Text>
            </View>
          </View>

          <View className={styles.ctaBtn} onClick={handleRecord}>
            <Text className={styles.ctaIcon}>🎙</Text>
            <Text>按住录一段今天的旅行</Text>
          </View>
        </View>

        <View className={styles.section}>
          <View className={styles.sectionHeader}>
            <Text className={styles.sectionTitle}>📖 最近 30 天</Text>
            <Text className={styles.sectionMore}>{entries.length} 条</Text>
          </View>

          {entries.slice(0, 8).map(entry => (
            <JournalCard
              key={entry.id}
              entry={entry}
              onLike={handleLike}
              onTap={handleTap}
            />
          ))}
        </View>
      </ScrollView>
    </View>
  )
}

export default TimelinePage

import React from 'react'
import { View, Text, Image } from '@tarojs/components'
import Taro from '@tarojs/taro'
import { mockCurrentUser } from '@/data/mockJournals'
import styles from './index.module.scss'

const cells = [
  { icon: '📚', iconBg: 'rgba(232,137,92,0.12)', iconColor: '#E8895C', title: '我的手账库', hint: '234 条已整理', badge: '' },
  { icon: '⭐', iconBg: 'rgba(74,143,184,0.12)', iconColor: '#4A8FB8', title: '收藏的行程', hint: '12 个待出发', badge: 'NEW' },
  { icon: '🎨', iconBg: 'rgba(91,117,83,0.12)', iconColor: '#5B7553', title: '我的模板', hint: '3 款自定义风格' },
  { icon: '📤', iconBg: 'rgba(255,125,0,0.12)', iconColor: '#FF7D00', title: '分享与导出', hint: 'PDF / 视频 / 实体相册' },
  { icon: '⚙️', iconBg: 'rgba(45,42,38,0.08)', iconColor: '#6B6660', title: '偏好设置', hint: '字体 / 字号 / 默认模板' },
  { icon: '💬', iconBg: 'rgba(232,137,92,0.12)', iconColor: '#E8895C', title: '意见反馈', hint: '让产品更好用', badge: '' },
  { icon: 'ℹ️', iconBg: 'rgba(74,143,184,0.12)', iconColor: '#4A8FB8', title: '关于云游手账', hint: 'v1.0.0 MVP' }
]

const MinePage: React.FC = () => {
  const handleCell = (title: string) => {
    console.log('[Mine] tap', title)
    Taro.showToast({ title: `${title} · 功能开发中`, icon: 'none' })
  }

  return (
    <View className={styles.page}>
      <View className={styles.header}>
        <View className={styles.profileRow}>
          <Image className={styles.avatar} src={mockCurrentUser.avatar} mode="aspectFill" />
          <View className={styles.profileInfo}>
            <Text className={styles.nickname}>{mockCurrentUser.nickname}</Text>
            <Text className={styles.signature}>{mockCurrentUser.signature}</Text>
          </View>
          <View className={styles.editBtn} onClick={() => handleCell('编辑资料')}>
            编辑
          </View>
        </View>
      </View>

      <View className={styles.statsCard}>
        <View className={styles.statItem}>
          <Text className={styles.statNum}>{mockCurrentUser.totalDays}</Text>
          <Text className={styles.statLabel}>天数</Text>
        </View>
        <View className={styles.statItem}>
          <Text className={styles.statNum}>{mockCurrentUser.totalEntries}</Text>
          <Text className={styles.statLabel}>手账</Text>
        </View>
        <View className={styles.statItem}>
          <Text className={styles.statNum}>{mockCurrentUser.totalCities}</Text>
          <Text className={styles.statLabel}>城市</Text>
        </View>
        <View className={styles.statItem}>
          <Text className={styles.statNum}>2.1w</Text>
          <Text className={styles.statLabel}>粉丝</Text>
        </View>
      </View>

      <View className={styles.section}>
        <Text className={styles.sectionTitle}>内容与服务</Text>
        <View className={styles.card}>
          {cells.slice(0, 4).map((c, i) => (
            <View key={i} className={styles.cell} onClick={() => handleCell(c.title)}>
              <View className={styles.cellIcon} style={{ background: c.iconBg, color: c.iconColor }}>
                {c.icon}
              </View>
              <View className={styles.cellBody}>
                <Text className={styles.cellTitle}>{c.title}</Text>
                <Text className={styles.cellHint}>{c.hint}</Text>
              </View>
              {c.badge && <Text className={styles.cellBadge}>{c.badge}</Text>}
              <Text className={styles.cellArrow}>›</Text>
            </View>
          ))}
        </View>
      </View>

      <View className={styles.section}>
        <Text className={styles.sectionTitle}>其他</Text>
        <View className={styles.card}>
          {cells.slice(4).map((c, i) => (
            <View key={i} className={styles.cell} onClick={() => handleCell(c.title)}>
              <View className={styles.cellIcon} style={{ background: c.iconBg, color: c.iconColor }}>
                {c.icon}
              </View>
              <View className={styles.cellBody}>
                <Text className={styles.cellTitle}>{c.title}</Text>
                <Text className={styles.cellHint}>{c.hint}</Text>
              </View>
              {c.badge && <Text className={styles.cellBadge}>{c.badge}</Text>}
              <Text className={styles.cellArrow}>›</Text>
            </View>
          ))}
        </View>
      </View>

      <Text className={styles.version}>云游手账 v1.0.0 · Made with TRAE</Text>
    </View>
  )
}

export default MinePage

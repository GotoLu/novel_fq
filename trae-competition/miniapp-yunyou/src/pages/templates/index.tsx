import React, { useState, useMemo } from 'react'
import { View, Text, ScrollView } from '@tarojs/components'
import Taro from '@tarojs/taro'
import TemplateCard from '@/components/TemplateCard'
import { mockTemplates } from '@/data/mockTemplates'
import styles from './index.module.scss'

const FILTERS = [
  { key: 'all', label: '全部' },
  { key: 'hot', label: '🔥 热门' },
  { key: 'literary', label: '文艺' },
  { key: 'practical', label: '实用' },
  { key: 'fun', label: '趣味' }
]

const TemplatesPage: React.FC = () => {
  const [filter, setFilter] = useState('all')
  const [activeId, setActiveId] = useState<string>('t01')

  const filtered = useMemo(() => {
    if (filter === 'all') return mockTemplates
    if (filter === 'hot') return mockTemplates.filter(t => t.hot)
    if (filter === 'literary') return mockTemplates.filter(t => ['t01','t05','t07'].includes(t.id))
    if (filter === 'practical') return mockTemplates.filter(t => ['t02','t09'].includes(t.id))
    if (filter === 'fun') return mockTemplates.filter(t => ['t03','t06','t08'].includes(t.id))
    return mockTemplates
  }, [filter])

  const active = useMemo(() => mockTemplates.find(t => t.id === activeId) || mockTemplates[0], [activeId])

  const handleUse = () => {
    console.log('[Templates] use', activeId)
    Taro.showModal({
      title: '已套用模板',
      content: `「${active.name}」已应用为默认风格，回到「录入」页录一段语音试试。`,
      showCancel: false,
      success: () => {
        Taro.switchTab({ url: '/pages/record/index' })
      }
    })
  }

  return (
    <View className={styles.page}>
      <ScrollView scrollY enhanced showScrollbar={false}>
        <View className={styles.banner}>
          <Text className={styles.bannerTitle}>9 种风格化模板</Text>
          <Text className={styles.bannerSub}>同一段旅行，不同的呈现方式。点一下切换，让你的手账适配朋友圈、小红书、攻略、亲子、美食各种场景。</Text>
          <View className={styles.bannerStat}>
            <View className={styles.bannerStatItem}>
              <Text className={styles.bannerStatNum}>9</Text>
              <Text>模板</Text>
            </View>
            <View className={styles.bannerStatItem}>
              <Text className={styles.bannerStatNum}>68,000+</Text>
              <Text>累计使用</Text>
            </View>
            <View className={styles.bannerStatItem}>
              <Text className={styles.bannerStatNum}>98%</Text>
              <Text>好评率</Text>
            </View>
          </View>
        </View>

        <ScrollView className={styles.filterRow} scrollX enhanced showScrollbar={false}>
          {FILTERS.map(f => (
            <View
              key={f.key}
              className={`${styles.filterItem} ${filter === f.key ? styles.active : ''}`}
              onClick={() => setFilter(f.key)}
            >
              {f.label}
            </View>
          ))}
        </ScrollView>

        <View className={styles.section}>
          <View className={styles.sectionHeader}>
            <Text className={styles.sectionTitle}>{FILTERS.find(f => f.key === filter)?.label} · {filtered.length} 款</Text>
            <Text className={styles.sectionMore}>默认按热度</Text>
          </View>
          <View className={styles.list}>
            {filtered.map(t => (
              <TemplateCard
                key={t.id}
                template={t}
                active={t.id === activeId}
                onTap={setActiveId}
              />
            ))}
          </View>
        </View>

        <View style={{ height: '140rpx' }} />
      </ScrollView>

      <View className={styles.previewBar}>
        <View className={styles.previewRow}>
          <Text className={styles.previewName}>
            已选：<Text className={styles.previewNameAccent}>{active.name}</Text>
          </Text>
          <View className={styles.previewBtn} onClick={handleUse}>
            ✨ 套用
          </View>
        </View>
      </View>
    </View>
  )
}

export default TemplatesPage

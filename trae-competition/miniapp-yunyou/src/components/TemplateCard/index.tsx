import React from 'react'
import { View, Text, Image } from '@tarojs/components'
import classnames from 'classnames'
import type { JournalTemplate } from '@/types/journal'
import styles from './index.module.scss'

interface Props {
  template: JournalTemplate
  active?: boolean
  onTap?: (id: string) => void
}

/** 模板卡（封面 + 名称 + 描述 + 风格色卡） */
const TemplateCard: React.FC<Props> = ({ template, active, onTap }) => {
  return (
    <View
      className={classnames(styles.card, active && styles.active)}
      onClick={() => onTap?.(template.id)}
      style={{ borderColor: active ? template.color : 'transparent' }}
    >
      <View className={styles.coverWrap}>
        <Image className={styles.cover} src={template.cover} mode="aspectFill" />
        {template.hot && (
          <View className={styles.hotBadge}>
            <Text className={styles.hotText}>🔥 HOT</Text>
          </View>
        )}
        {active && (
          <View className={styles.checkBadge} style={{ background: template.color }}>
            <Text className={styles.checkText}>✓</Text>
          </View>
        )}
      </View>
      <View className={styles.info}>
        <Text className={styles.name} style={{ color: template.color }}>{template.name}</Text>
        <Text className={styles.desc}>{template.description}</Text>
        <View className={styles.footRow}>
          <Text className={styles.count}>{template.usedCount.toLocaleString()} 人在用</Text>
          <View className={styles.dotRow}>
            <View className={styles.dot} style={{ background: template.styles.titleColor }} />
            <View className={styles.dot} style={{ background: template.styles.bgColor, border: '1rpx solid #E5E6EB' }} />
            <View className={styles.dot} style={{ background: template.styles.textColor }} />
          </View>
        </View>
      </View>
    </View>
  )
}

export default TemplateCard

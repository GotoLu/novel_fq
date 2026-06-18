import React from 'react'
import { View, Text } from '@tarojs/components'
import Taro from '@tarojs/taro'
import styles from './index.module.scss'

const features = [
  { icon: '🎬', bg: 'rgba(232,137,92,0.12)', title: '短视频自动生成', desc: '把多天手账拼成 1 分钟 vlog', status: '即将上线' },
  { icon: '🖨', bg: 'rgba(74,143,184,0.12)', title: 'PDF 高清导出', desc: '保留手账排版和配图', status: '已支持' },
  { icon: '📦', bg: 'rgba(91,117,83,0.12)', title: '实体相册直送', desc: '精装布面 / 烫金封面 / 顺丰包邮', status: '已支持' },
  { icon: '☁️', bg: 'rgba(255,125,0,0.12)', title: '云端同步', desc: '多设备无缝衔接', status: '开发中' }
]

const CraftPage: React.FC = () => {
  const handleBack = () => {
    Taro.navigateBack().catch(() => {
      Taro.switchTab({ url: '/pages/timeline/index' })
    })
  }

  return (
    <View className={styles.page}>
      <View className={styles.iconWrap}>
        <View className={styles.bigIcon}>✨</View>
        <Text className={styles.title}>一键成册</Text>
        <Text className={styles.subtitle}>让你的手账不止于手机</Text>
        <Text className={styles.hint}>把多次旅行拼成一本精装相册 / 一段 vlog / 一份分享海报</Text>
      </View>

      <View className={styles.featureList}>
        {features.map((f, i) => (
          <View key={i} className={styles.featureItem}>
            <View className={styles.featureIcon} style={{ background: f.bg }}>
              {f.icon}
            </View>
            <View className={styles.featureBody}>
              <Text className={styles.featureTitle}>{f.title}</Text>
              <Text className={styles.featureDesc}>{f.desc}</Text>
            </View>
            <Text className={styles.featureStatus}>{f.status}</Text>
          </View>
        ))}
      </View>

      <View className={styles.backBtn} onClick={handleBack}>
        返回上一页
      </View>
    </View>
  )
}

export default CraftPage

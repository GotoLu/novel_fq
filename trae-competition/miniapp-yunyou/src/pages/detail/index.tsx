import React, { useState, useEffect } from 'react'
import { View, Text, Image } from '@tarojs/components'
import Taro, { useRouter } from '@tarojs/taro'
import WashiTape from '@/components/WashiTape'
import { mockJournals } from '@/data/mockJournals'
import type { JournalEntry } from '@/types/journal'
import styles from './index.module.scss'

const DetailPage: React.FC = () => {
  const router = useRouter()
  const [entry, setEntry] = useState<JournalEntry | null>(null)

  useEffect(() => {
    const id = router.params.id
    if (id) {
      const found = mockJournals.find(j => j.id === id)
      if (found) {
        setEntry(found)
        Taro.setNavigationBarTitle({ title: found.title }).catch(() => {})
      }
    }
    // from=record 时不传 id，给一个默认条目
    if (!id) {
      setEntry(mockJournals[0])
    }
  }, [router.params.id])

  if (!entry) {
    return (
      <View className={styles.page}>
        <View className={styles.section}>
          <Text>加载中…</Text>
        </View>
      </View>
    )
  }

  const handleLike = () => {
    Taro.vibrateShort({ type: 'light' }).catch(() => {})
    Taro.showToast({ title: entry.isLiked ? '取消点赞' : '已点赞 ❤️', icon: 'none' })
  }

  const handleShare = () => {
    Taro.showActionSheet({
      itemList: ['微信好友', '朋友圈', '小红书', '复制链接'],
      success: (res) => {
        Taro.showToast({ title: '分享成功 ✨', icon: 'success' })
        console.log('[Detail] share to', res.tapIndex)
      }
    })
  }

  const handleCraft = () => {
    Taro.navigateTo({ url: '/pages/craft/index' })
  }

  return (
    <View className={styles.page}>
      <View className={styles.cover}>
        <Image className={styles.coverImg} src={entry.images[0]} mode="aspectFill" />
        <View className={styles.coverMask} />
        <View className={styles.coverInfo}>
          <Text className={styles.coverDate}>{entry.date} · {entry.time}</Text>
          <Text className={styles.coverTitle}>{entry.title}</Text>
          <Text className={styles.coverLoc}>📍 {entry.location}</Text>
        </View>
      </View>

      <View className={styles.body}>
        <View className={styles.metaCard}>
          <View className={styles.metaItem}>
            <Text className={styles.metaIcon}>🕓</Text>
            <Text className={styles.metaLabel}>时间</Text>
            <Text className={styles.metaValue}>{entry.time}</Text>
          </View>
          <View className={styles.metaItem}>
            <Text className={styles.metaIcon}>🌤</Text>
            <Text className={styles.metaLabel}>天气</Text>
            <Text className={styles.metaValue}>{entry.weather || '晴'}</Text>
          </View>
          <View className={styles.metaItem}>
            <Text className={styles.metaIcon}>❤️</Text>
            <Text className={styles.metaLabel}>点赞</Text>
            <Text className={styles.metaValue}>{entry.likes}</Text>
          </View>
        </View>

        <View className={styles.section}>
          <Text className={styles.sectionTitle}>📖 当日游记</Text>
          <Text className={styles.content}>{entry.content}</Text>
          <View className={styles.tagsRow}>
            {entry.tags.map((t, i) => (
              <View key={i} className={styles.tag}>
                <Text className={styles.tagText}>#{t}</Text>
              </View>
            ))}
          </View>
          <WashiTape top="-8rpx" right="40rpx" rotate={12} color="rgba(91,117,83,0.5)" />
        </View>

        {entry.images.length > 1 && (
          <View className={styles.section}>
            <Text className={styles.sectionTitle}>📷 旅行相册</Text>
            <View className={styles.gallery}>
              {entry.images.map((img, i) => (
                <Image
                  key={i}
                  className={styles.galleryImg}
                  src={img}
                  mode="aspectFill"
                  onClick={() => Taro.previewImage({ urls: entry.images, current: img }).catch(() => {})}
                />
              ))}
            </View>
          </View>
        )}
      </View>

      <View className={styles.footer}>
        <View className={styles.footerAction} onClick={handleLike}>
          {entry.isLiked ? '❤️ 已赞' : '🤍 点赞'}
        </View>
        <View className={styles.footerAction} onClick={handleShare}>
          📤 分享
        </View>
        <View className={styles.footerPrimary} onClick={handleCraft}>
          ✨ 一键成册
        </View>
      </View>
    </View>
  )
}

export default DetailPage

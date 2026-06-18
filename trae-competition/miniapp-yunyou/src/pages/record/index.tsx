import React, { useState } from 'react'
import { View, Text, Image } from '@tarojs/components'
import Taro from '@tarojs/taro'
import VoiceWave from '@/components/VoiceWave'
import WashiTape from '@/components/WashiTape'
import { mockVoiceScripts } from '@/data/mockVoices'
import styles from './index.module.scss'

type Mode = 'voice' | 'text' | 'photo'

const RecordPage: React.FC = () => {
  const [mode, setMode] = useState<Mode>('voice')
  const [listening, setListening] = useState(false)
  const [scriptIdx, setScriptIdx] = useState(0)
  const [transcript, setTranscript] = useState('')
  const [transcriptMeta, setTranscriptMeta] = useState<{ location: string; duration: string } | null>(null)

  const handleMicClick = () => {
    if (listening) return
    setListening(true)
    setTranscript('')
    setTranscriptMeta(null)
    console.log('[Record] start listening')

    // 1.5s 后模拟"转写完成"
    setTimeout(() => {
      const v = mockVoiceScripts[scriptIdx % mockVoiceScripts.length]
      setScriptIdx(scriptIdx + 1)
      setTranscript(v.text)
      setTranscriptMeta({ location: v.location, duration: v.duration })
      setListening(false)
      console.log('[Record] transcribed:', v.text)
      Taro.vibrateShort({ type: 'medium' }).catch(() => {})
    }, 1500)
  }

  const handleSave = () => {
    if (!transcript) {
      Taro.showToast({ title: '请先录一段语音或写一段文字', icon: 'none' })
      return
    }
    Taro.showModal({
      title: '已生成手账',
      content: '已自动套用「文艺清新」风格，可在「我的」中查看。',
      showCancel: false
    })
  }

  const handlePreview = () => {
    if (!transcript) {
      Taro.showToast({ title: '请先录一段语音', icon: 'none' })
      return
    }
    Taro.showToast({ title: '正在打开预览…', icon: 'none', duration: 800 })
    setTimeout(() => {
      Taro.navigateTo({ url: '/pages/detail/index?from=record' })
    }, 800)
  }

  return (
    <View className={styles.page}>
      <View className={styles.headerCard}>
        <Text className={styles.headerTitle}>今天，又是一段好旅程</Text>
        <Text className={styles.headerSub}>选择你喜欢的方式记录，AI 帮你整理成册</Text>
      </View>

      <View className={styles.modeRow}>
        <View
          className={`${styles.modeItem} ${mode === 'voice' ? styles.active : ''}`}
          onClick={() => setMode('voice')}
        >
          🎙 语音
        </View>
        <View
          className={`${styles.modeItem} ${mode === 'text' ? styles.active : ''}`}
          onClick={() => setMode('text')}
        >
          ✍️ 文字
        </View>
        <View
          className={`${styles.modeItem} ${mode === 'photo' ? styles.active : ''}`}
          onClick={() => setMode('photo')}
        >
          📷 拍照
        </View>
      </View>

      {mode === 'voice' && (
        <View className={styles.voiceCard}>
          <Text className={styles.dateLabel}>2026 · 5 · 19 · 巴厘岛</Text>
          <Text className={styles.sectionTitle}>边走边说</Text>
          <Text className={styles.sectionSub}>AI 自动转写 + GPS 自动打点</Text>

          <View className={styles.micWrap}>
            <View
              className={`${styles.micBtn} ${listening ? styles.listening : ''}`}
              onClick={handleMicClick}
            >
              <Text className={styles.micIcon}>{listening ? '🔴' : '🎙'}</Text>
            </View>
            <Text className={styles.hint}>
              {listening ? '正在聆听…' : transcript ? '再点一次录下一段' : '点麦克风开始录音'}
            </Text>
            {listening && (
              <VoiceWave count={15} active={true} height={56} />
            )}
          </View>

          <View className={styles.transcriptCard}>
            <Text className={styles.transcriptLabel}>
              {transcript ? '✓ 转写完成' : '转写内容'}
            </Text>
            <Text className={styles.transcriptText}>
              {transcript || '（点上方麦克风开始）'}
            </Text>
            {transcriptMeta && (
              <View className={styles.transcriptMeta}>
                <Text>📍 {transcriptMeta.location}</Text>
                <Text>⏱ {transcriptMeta.duration}</Text>
              </View>
            )}
          </View>
        </View>
      )}

      {mode === 'text' && (
        <View className={styles.voiceCard}>
          <Text className={styles.sectionTitle}>✍️ 文字记录</Text>
          <Text className={styles.sectionSub}>手写一段今天的感悟</Text>
          <View
            className={styles.transcriptCard}
            style={{ minHeight: '320rpx' }}
            onClick={() => Taro.showToast({ title: '文字编辑功能开发中', icon: 'none' })}
          >
            <Text className={styles.transcriptText} style={{ color: '#A8A39C' }}>
              （点此开始手写）
            </Text>
          </View>
        </View>
      )}

      {mode === 'photo' && (
        <View className={styles.voiceCard}>
          <Text className={styles.sectionTitle}>📷 拍照打点</Text>
          <Text className={styles.sectionSub}>AI 自动识别地点 + 推荐配文</Text>
          <View
            className={styles.transcriptCard}
            style={{ minHeight: '320rpx' }}
            onClick={() => Taro.showToast({ title: '相机功能开发中', icon: 'none' })}
          >
            <Text className={styles.transcriptText} style={{ color: '#A8A39C' }}>
              （点此打开相机）
            </Text>
          </View>
        </View>
      )}

      <View className={styles.toolsRow}>
        <View className={styles.toolBtn} onClick={() => Taro.showToast({ title: '位置服务开启', icon: 'none' })}>
          <Text className={styles.toolIcon}>📍</Text>
          <Text className={styles.toolLabel}>GPS</Text>
          <Text className={styles.toolHint}>已开启</Text>
        </View>
        <View className={styles.toolBtn} onClick={() => Taro.showToast({ title: 'AI 配图已就绪', icon: 'none' })}>
          <Text className={styles.toolIcon}>🎨</Text>
          <Text className={styles.toolLabel}>AI 配图</Text>
          <Text className={styles.toolHint}>3 张推荐</Text>
        </View>
        <View className={styles.toolBtn} onClick={() => Taro.showToast({ title: '天气数据已同步', icon: 'none' })}>
          <Text className={styles.toolIcon}>🌤</Text>
          <Text className={styles.toolLabel}>天气</Text>
          <Text className={styles.toolHint}>28°C 晴</Text>
        </View>
      </View>

      {transcript && (
        <View className={styles.previewSection}>
          <View className={styles.previewHeader}>
            <Text className={styles.previewTitle}>手账预览</Text>
            <Text className={styles.previewTag}>套用模板：文艺清新</Text>
          </View>
          <Image
            className={styles.previewImg}
            src="https://picsum.photos/id/1015/600/320"
            mode="aspectFill"
          />
          <View className={styles.previewBody}>
            <Text className={styles.previewHead}>2026.05.19 · 巴厘岛</Text>
            <Text className={styles.previewLoc}>📍 印尼 · 巴厘岛 · GPS 自动打点</Text>
            <Text className={styles.previewText}>"{transcript}"</Text>
          </View>
          <View className={styles.previewFoot}>
            <Text className={styles.footMeta}>❤️ 0 · ✨ 刚刚</Text>
            <View className={styles.footAction} onClick={handlePreview}>
              展开预览
            </View>
          </View>
          <WashiTape top="-10rpx" right="40rpx" rotate={15} color="rgba(74,143,184,0.55)" />
        </View>
      )}

      <View style={{ height: '160rpx' }} />

      <View className={styles.bottomBar}>
        <View className={styles.bottomBarSecondary} onClick={handlePreview}>
          👁 预览
        </View>
        <View className={styles.bottomBarPrimary} onClick={handleSave}>
          ✨ 一键成册
        </View>
      </View>
    </View>
  )
}

export default RecordPage

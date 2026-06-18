// 云游手账 · 业务类型定义

/** 手账条目 */
export interface JournalEntry {
  id: string
  date: string            // YYYY.MM.DD
  time: string            // HH:MM
  title: string
  content: string
  location: string        // GPS 地点
  weather?: string        // 天气
  images: string[]        // picsum 图
  tags: string[]          // 标签
  templateId?: string     // 套用模板
  likes: number
  isLiked: boolean
}

/** 风格化模板 */
export interface JournalTemplate {
  id: string
  name: string            // 文艺/攻略/小红书/...
  cover: string           // picsum 图
  description: string
  color: string           // 主色
  fontFamily: string      // 字体
  hot: boolean            // 是否热门
  usedCount: number
  styles: {
    titleColor: string
    bgColor: string
    textColor: string
  }
}

/** 语音转写片段 */
export interface VoiceScript {
  id: string
  text: string
  location: string
  duration: string
}

/** 当前用户 */
export interface CurrentUser {
  nickname: string
  avatar: string
  totalDays: number
  totalEntries: number
  totalCities: number
  signature: string
}

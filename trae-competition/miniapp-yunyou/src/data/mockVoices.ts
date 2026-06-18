import type { VoiceScript } from '@/types/journal'

/** 3 段真实感语音文稿（点击麦克风循环播放） */
export const mockVoiceScripts: VoiceScript[] = [
  {
    id: 'v01',
    text: '今天到了巴厘岛金巴兰海滩，傍晚的夕阳把海面染成橘子色，烤鱼的香气在晚风里弥漫……',
    location: '印尼 · 巴厘岛金巴兰海滩',
    duration: '00:18'
  },
  {
    id: 'v02',
    text: '刚走进乌布市场，藤编包好精致啊，老板开价 200k 印尼盾，砍价砍到 80k 拿下！',
    location: '印尼 · 巴厘岛乌布皇宫',
    duration: '00:12'
  },
  {
    id: 'v03',
    text: '回酒店泡澡，阳台望出去是银河，旅途的疲惫都被这碗热汤洗掉了 ✨',
    location: '印尼 · 巴厘岛乌布山区酒店',
    duration: '00:14'
  }
]

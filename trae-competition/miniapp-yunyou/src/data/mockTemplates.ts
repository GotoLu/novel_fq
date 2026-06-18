import type { JournalTemplate } from '@/types/journal'

/** 9 种风格化模板 */
export const mockTemplates: JournalTemplate[] = [
  {
    id: 't01', name: '文艺清新', cover: 'https://picsum.photos/id/1015/600/400',
    description: '淡淡的笔触、留白和纸胶带，适合慢节奏的旅行记录',
    color: '#E8895C', fontFamily: '"Noto Serif SC", serif', hot: true, usedCount: 12580,
    styles: { titleColor: '#2D2A26', bgColor: '#FAF7F2', textColor: '#6B6660' }
  },
  {
    id: 't02', name: '攻略实用', cover: 'https://picsum.photos/id/1036/600/400',
    description: '时间地点预算一应俱全，是分享给朋友的最佳格式',
    color: '#4A8FB8', fontFamily: '"Noto Sans SC", sans-serif', hot: true, usedCount: 8940,
    styles: { titleColor: '#1F3A52', bgColor: '#F0F5FA', textColor: '#2E6F95' }
  },
  {
    id: 't03', name: '小红书爆款', cover: 'https://picsum.photos/id/1018/600/400',
    description: 'emoji 拉满 + 醒目标题 + 大色块，让你的笔记脱颖而出',
    color: '#F53F3F', fontFamily: '"Noto Sans SC", sans-serif', hot: true, usedCount: 18320,
    styles: { titleColor: '#F53F3F', bgColor: '#FFF5F5', textColor: '#2D2A26' }
  },
  {
    id: 't04', name: '朋友圈短文', cover: 'https://picsum.photos/id/1039/600/400',
    description: '9 图 + 1 段金句，发圈必赞',
    color: '#5B7553', fontFamily: '"Noto Sans SC", sans-serif', hot: false, usedCount: 6210,
    styles: { titleColor: '#5B7553', bgColor: '#F4F8F1', textColor: '#2D2A26' }
  },
  {
    id: 't05', name: '胶片复古', cover: 'https://picsum.photos/id/1044/600/400',
    description: '漏光、颗粒、暗角，复古胶片氛围一键套用',
    color: '#B85B33', fontFamily: '"Caveat", cursive', hot: false, usedCount: 4570,
    styles: { titleColor: '#B85B33', bgColor: '#FDF2EC', textColor: '#6B6660' }
  },
  {
    id: 't06', name: '童趣手绘', cover: 'https://picsum.photos/id/292/600/400',
    description: '蜡笔笔触 + 简笔插画，亲子游首选',
    color: '#FF7D00', fontFamily: '"Noto Sans SC", sans-serif', hot: false, usedCount: 3890,
    styles: { titleColor: '#FF7D00', bgColor: '#FFF8E7', textColor: '#2D2A26' }
  },
  {
    id: 't07', name: '极简留白', cover: 'https://picsum.photos/id/312/600/400',
    description: '一图一行字，less is more',
    color: '#1D2129', fontFamily: '"Noto Serif SC", serif', hot: false, usedCount: 2340,
    styles: { titleColor: '#1D2129', bgColor: '#FFFFFF', textColor: '#4E5969' }
  },
  {
    id: 't08', name: '美食地图', cover: 'https://picsum.photos/id/431/600/400',
    description: '菜名+店名+人均+地址，馋哭朋友圈',
    color: '#E8895C', fontFamily: '"Noto Sans SC", sans-serif', hot: true, usedCount: 9870,
    styles: { titleColor: '#B85B33', bgColor: '#FDF2EC', textColor: '#2D2A26' }
  },
  {
    id: 't09', name: '商务简报', cover: 'https://picsum.photos/id/1/600/400',
    description: '出差报告 / 团建总结 / 行业考察专用',
    color: '#2E6F95', fontFamily: '"Noto Sans SC", sans-serif', hot: false, usedCount: 1280,
    styles: { titleColor: '#2E6F95', bgColor: '#F0F5FA', textColor: '#1D2129' }
  }
]

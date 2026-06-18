import type { JournalEntry } from '@/types/journal'

/** 时光轴首页 Mock：13 条手账 */
export const mockJournals: JournalEntry[] = [
  {
    id: 'j01', date: '2026.05.18', time: '18:32',
    title: '金巴兰日落 · 烤鱼配啤酒',
    content: '今天到了巴厘岛金巴兰海滩，傍晚的夕阳把海面染成橘子色，烤鱼的香气在晚风里弥漫。三个人光着脚踩在温热的沙滩上，点了一份烤鱼拼盘加三瓶 Bintang 啤酒。',
    location: '印尼 · 巴厘岛金巴兰海滩', weather: '28°C 晴',
    images: ['https://picsum.photos/id/1015/600/400', 'https://picsum.photos/id/1036/600/400'],
    tags: ['日落', '海岛', '美食'],
    templateId: 't01', likes: 128, isLiked: true
  },
  {
    id: 'j02', date: '2026.05.18', time: '11:15',
    title: '乌布市场砍价记',
    content: '刚走进乌布市场，藤编包好精致啊，老板开价 200k 印尼盾，砍价砍到 80k 拿下！然后发现隔壁一模一样的卖 60k……',
    location: '印尼 · 巴厘岛乌布皇宫', weather: '30°C 多云',
    images: ['https://picsum.photos/id/1044/600/400'],
    tags: ['市集', '购物', '乌布'],
    likes: 56, isLiked: false
  },
  {
    id: 'j03', date: '2026.05.17', time: '21:08',
    title: '酒店阳台的银河',
    content: '回酒店泡澡，阳台望出去是银河，旅途的疲惫都被这碗热汤洗掉了 ✨ 决定明天哪都不去，就在阳台躺一天。',
    location: '印尼 · 巴厘岛乌布山区酒店', weather: '23°C 晴',
    images: ['https://picsum.photos/id/1018/600/400'],
    tags: ['夜景', '酒店', '度假'],
    templateId: 't02', likes: 312, isLiked: true
  },
  {
    id: 'j04', date: '2026.05.16', time: '15:46',
    title: '京都岚山竹林小径',
    content: '岚山的竹林小径比想象中更绿更静，竹叶沙沙声像下了一场绿色的雨。穿着浴衣走完全程，抹茶冰激凌是最大的慰藉。',
    location: '日本 · 京都岚山', weather: '22°C 阴',
    images: ['https://picsum.photos/id/1039/600/400', 'https://picsum.photos/id/1018/600/400'],
    tags: ['京都', '竹林', '古都'],
    templateId: 't03', likes: 445, isLiked: false
  },
  {
    id: 'j05', date: '2026.05.15', time: '07:12',
    title: '清水寺清晨',
    content: '清晨 6 点起床赶在游客大军前抵达清水寺，露水还挂在音羽瀑布的石头阶梯上。鸟居红得发亮，整个世界属于我一个人。',
    location: '日本 · 京都清水寺', weather: '18°C 晴',
    images: ['https://picsum.photos/id/1015/600/400'],
    tags: ['古寺', '清晨', '京都'],
    likes: 234, isLiked: true
  },
  {
    id: 'j06', date: '2026.05.12', time: '19:50',
    title: '东京涉谷十字路口',
    content: '站在 Starbucks 二楼看涉谷十字路口，60 秒一次的"全球最忙路口"，每一波人流都像一场无声的舞蹈。今晚吃了鳗鱼饭，明早去筑地。',
    location: '日本 · 东京涉谷', weather: '20°C 晴',
    images: ['https://picsum.photos/id/1036/600/400', 'https://picsum.photos/id/1044/600/400'],
    tags: ['都市', '夜景', '东京'],
    likes: 89, isLiked: false
  },
  {
    id: 'j07', date: '2026.05.10', time: '14:22',
    title: '杭州西湖断桥',
    content: '细雨中的西湖有一种不真实的美，断桥残雪的意境没看到，撑着油纸伞倒是被很多人拍了照。',
    location: '中国 · 杭州西湖', weather: '19°C 小雨',
    images: ['https://picsum.photos/id/1018/600/400'],
    tags: ['江南', '西湖', '烟雨'],
    templateId: 't01', likes: 67, isLiked: true
  },
  {
    id: 'j08', date: '2026.05.08', time: '10:05',
    title: '大理洱海骑行',
    content: '环洱海骑了 130 公里，3 天 2 夜。海舌公园的夫妻树，蝴蝶泉边的野花，双廊的落日——每公里都值得。',
    location: '中国 · 大理洱海', weather: '24°C 晴',
    images: ['https://picsum.photos/id/1015/600/400', 'https://picsum.photos/id/1039/600/400'],
    tags: ['骑行', '洱海', '云南'],
    likes: 521, isLiked: true
  },
  {
    id: 'j09', date: '2026.05.05', time: '20:18',
    title: '重庆洪崖洞夜景',
    content: '洪崖洞亮灯的那一瞬间全场惊呼，像《千与千寻》的汤屋真的存在。吃了一份酸辣粉 + 一碗小面，重庆的夜生活才刚刚开始。',
    location: '中国 · 重庆洪崖洞', weather: '26°C 阴',
    images: ['https://picsum.photos/id/1036/600/400'],
    tags: ['夜景', '美食', '重庆'],
    likes: 178, isLiked: false
  },
  {
    id: 'j10', date: '2026.05.02', time: '12:30',
    title: '三亚天涯海角',
    content: '天涯石、海角石、南天一柱。传说里浪漫的地方真实到访多少有点失落，但椰子树下的椰子鸡是真的好喝。',
    location: '中国 · 三亚天涯海角', weather: '31°C 晴',
    images: ['https://picsum.photos/id/1044/600/400'],
    tags: ['海岛', '三亚', '椰风'],
    likes: 45, isLiked: false
  },
  {
    id: 'j11', date: '2026.04.28', time: '16:08',
    title: '西安回民街肉夹馍',
    content: '在回民街吃了一整条街，老白家肉夹馍 + 麻酱凉皮 + 冰峰三件套是标配。钟楼下的夕阳照在鼓楼飞檐上，美极了。',
    location: '中国 · 西安回民街', weather: '25°C 晴',
    images: ['https://picsum.photos/id/1018/600/400'],
    tags: ['美食', '古城', '西安'],
    likes: 92, isLiked: true
  },
  {
    id: 'j12', date: '2026.04.25', time: '08:46',
    title: '拉萨布达拉宫',
    content: '凌晨 4 点起床去排队，第一个进布达拉宫。金顶在朝阳下闪着光，喇嘛的诵经声从白宫深处传来——离天空最近的地方。',
    location: '中国 · 拉萨布达拉宫', weather: '12°C 晴',
    images: ['https://picsum.photos/id/1015/600/400', 'https://picsum.photos/id/1036/600/400'],
    tags: ['朝圣', '高原', '拉萨'],
    templateId: 't02', likes: 678, isLiked: true
  },
  {
    id: 'j13', date: '2026.04.20', time: '13:00',
    title: '厦门鼓浪屿',
    content: '从厦门轮渡到鼓浪屿，岛上没有机动车，只有钢琴博物馆和无处不在的三角梅。买了一本盖章本，盖了 38 个章。',
    location: '中国 · 厦门鼓浪屿', weather: '23°C 多云',
    images: ['https://picsum.photos/id/1039/600/400'],
    tags: ['海岛', '文艺', '厦门'],
    likes: 156, isLiked: false
  }
]

/** 当前用户 Mock */
export const mockCurrentUser = {
  nickname: '云游 · 小美',
  avatar: 'https://picsum.photos/id/64/200/200',
  totalDays: 87,
  totalEntries: 234,
  totalCities: 36,
  signature: '用脚丈量世界，用手账记录时光 ✈️'
}

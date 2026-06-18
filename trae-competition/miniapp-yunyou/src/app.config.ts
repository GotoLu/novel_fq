export default defineAppConfig({
  pages: [
    'pages/timeline/index',
    'pages/record/index',
    'pages/templates/index',
    'pages/mine/index',
    'pages/detail/index',
    'pages/craft/index'
  ],
  window: {
    backgroundTextStyle: 'light',
    navigationBarBackgroundColor: '#FAF7F2',
    navigationBarTitleText: '云游手账',
    navigationBarTextStyle: 'black',
    backgroundColor: '#FAF7F2'
  },
  tabBar: {
    color: '#A8A39C',
    selectedColor: '#E8895C',
    backgroundColor: '#FFFFFF',
    borderStyle: 'white',
    list: [
      { pagePath: 'pages/timeline/index', text: '时光轴' },
      { pagePath: 'pages/record/index', text: '录入' },
      { pagePath: 'pages/templates/index', text: '模板' },
      { pagePath: 'pages/mine/index', text: '我的' }
    ]
  }
})

import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "AI Nav",
  description: "Global AI Directory, Podcasts, and News",
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: 'AI 目录', link: '/directory/' },
      { text: 'AI 播客', link: '/podcasts/' },
      { text: 'AI 新闻', link: '/news/' }
    ],
    sidebar: {
      '/directory/': [
        {
          text: 'AI 目录',
          items: [
            { text: '全部工具', link: '/directory/' }
          ]
        }
      ],
      '/podcasts/': [
        {
          text: 'AI 播客',
          items: [
            { text: '最新播客', link: '/podcasts/' }
          ]
        }
      ],
      '/news/': [
        {
          text: 'AI 新闻',
          items: [
            { text: '每日新闻', link: '/news/' }
          ]
        }
      ]
    }
  }
})

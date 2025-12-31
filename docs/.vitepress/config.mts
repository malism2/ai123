import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "AI Nav",
  description: "Global AI Directory, Podcasts, and News",
  lang: 'en-US',
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Podcasts', link: '/podcasts/' },
      { text: 'News', link: '/news/' }
    ],
    sidebar: {
      '/podcasts/': [
        {
          text: 'AI Podcasts',
          items: [
            { text: 'Latest Episodes', link: '/podcasts/' }
          ]
        }
      ],
      '/news/': [
        {
          text: 'AI News',
          items: [
            { text: 'Daily Updates', link: '/news/' }
          ]
        }
      ]
    }
  }
})

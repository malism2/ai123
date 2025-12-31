import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "AI Nav",
  description: "The Ultimate Global AI Directory",
  lang: 'en-US',
  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Podcasts', link: '/podcasts/' },
      { text: 'News', link: '/news/' }
    ],
    sidebar: [
      {
        text: 'Categories',
        items: [
          { text: 'All Tools', link: '/' },
          { text: 'Chatbots', link: '/#chatbots' },
          { text: 'Image Generation', link: '/#image' },
          { text: 'Video Generation', link: '/#video' },
          { text: 'Writing & SEO', link: '/#writing' },
          { text: 'Coding Assistant', link: '/#coding' },
          { text: 'Audio & Music', link: '/#audio' },
          { text: 'Productivity', link: '/#productivity' }
        ]
      }
    ]
  }
})

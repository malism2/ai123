/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./docs/**/*.{md,vue,js,ts}",
    "./docs/.vitepress/**/*.{md,vue,js,ts}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#6750A4',
        'on-primary': '#FFFFFF',
        'primary-container': '#EADDFF',
        'on-primary-container': '#21005D',
        secondary: '#625B71',
        'on-secondary': '#FFFFFF',
        'secondary-container': '#E8DEF8',
        'on-secondary-container': '#1D192B',
        surface: '#FEF7FF',
        'on-surface': '#1D1B20',
        'surface-variant': '#E7E0EC',
        'on-surface-variant': '#49454F',
        outline: '#79747E',
      },
      borderRadius: {
        'm3': '12px',
        'm3-lg': '28px',
      }
    },
  },
  plugins: [],
}

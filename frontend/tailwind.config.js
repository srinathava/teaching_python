/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      fontFamily: {
        'comic-neue': ['"Comic Neue"', 'cursive'],
      },
      colors: {
        'primary-blue': '#4A90E2',
        'success-green': '#2ECC71',
        'warning-yellow': '#F1C40F',
        'error-red': '#E74C3C',
        'text-dark': '#2C3E50',
        'accent-purple': '#9B59B6',
        'neutral-gray': '#BDC3C7',
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
  ],
}
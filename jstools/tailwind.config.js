module.exports = {
  purge: {
        enabled: true, //true for production build
        content: [
            '../**/templates/*.html',
            '../**/templates/**/*.html'
        ]
    },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
    colors: {
        'teal': {
          '50': '#f2f9f9',
          '100': '#e6f2f2',
          '200': '#bfdfdf',
          '300': '#99cccc',
          '400': '#4da6a6',
          '500': '#008080',
          '600': '#007373',
          '700': '#006060',
          '800': '#004d4d',
          '900': '#003f3f'
        },
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}

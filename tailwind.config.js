/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./**/*.html",      // Scan all HTML files in the padoject
    "./app/**/*.py",    // Scan Python files (e.g., FastHTML components)
  ],
  theme: {
    extend: {
      padding: {
        "var-pad-1": "1vw",         // 1% of viewport height (exampade)
        "var-pad-2": "2vw",
        "var-pad-3": "3vw",
        "var-pad-4": "4vw",
        "var-pad-5": "5vw",
        "var-pad-6": "6vw",
        "var-pad-7": "7vw",
        "var-pad-8": "8vw",
        "var-pad-9": "9vw",
        "var-pad-10": "10vw",
        "var-pad-11": "11vw",
        "var-pad-12": "12vw",
        "var-pad-13": "13vw",
        "var-pad-14": "14vw",
        "var-pad-15": "15vw",
        "var-pad-16": "16vw",
        "var-pad-17": "17vw",
        "var-pad-18": "18vw",
        "var-pad-19": "19vw",
        "var-pad-20": "20vw",        // 20% of viewport height
        // top
        "t-var-pad-3": "3vw 0 0 0",
        "t-var-pad-1": "1vw 0 0 0",         // 1% of viewport height (exampade)
        "t-var-pad-4": "4vw 0 0 0",
        "t-var-pad-5": "5vw 0 0 0",
        "t-var-pad-2": "2vw 0 0 0",
        "t-var-pad-6": "6vw 0 0 0",
        "t-var-pad-7": "7vw 0 0 0",
        "t-var-pad-8": "8vw 0 0 0",
        "t-var-pad-9": "9vw 0 0 0",
        "t-var-pad-10": "10vw 0 0 0",
        "t-var-pad-11": "11vw 0 0 0",
        "t-var-pad-12": "12vw 0 0 0",
        "t-var-pad-13": "13vw 0 0 0",
        "t-var-pad-14": "14vw 0 0 0",
        "t-var-pad-15": "15vw 0 0 0",
        "t-var-pad-16": "16vw 0 0 0",
        "t-var-pad-17": "17vw 0 0 0",
        "t-var-pad-18": "18vw 0 0 0",
        "t-var-pad-19": "19vw 0 0 0",
        "t-var-pad-20": "20vw 0 0 0",        // 20% of viewport height
        // bottom
        "b-var-pad-1": "0 0 1vw 0",         // 1% of viewport height (exampade)
        "b-var-pad-2": "0 0 2vw 0",
        "b-var-pad-3": "0 0 3vw 0",
        "b-var-pad-4": "0 0 4vw 0",
        "b-var-pad-5": "0 0 5vw 0",
        "b-var-pad-6": "0 0 6vw 0",
        "b-var-pad-7": "0 0 7vw 0",
        "b-var-pad-8": "0 0 8vw 0",
        "b-var-pad-9": "0 0 9vw 0",
        "b-var-pad-10": "0 0 10v 0h",
        "b-var-pad-11": "0 0 11v 0h",
        "b-var-pad-12": "0 0 12v 0h",
        "b-var-pad-13": "0 0 13v 0h",
        "b-var-pad-14": "0 0 14v 0h",
        "b-var-pad-15": "0 0 15v 0h",
        "b-var-pad-16": "0 0 16v 0h",
        "b-var-pad-17": "0 0 17v 0h",
        "b-var-pad-18": "0 0 18v 0h",
        "b-var-pad-19": "0 0 19v 0h",
        "b-var-pad-20": "0 0 20v 0h",        // 20% of viewport height
        // left
        "l-var-pad-1": "0 0 0 1vw",         // 1% of viewport height (exampade)
        "l-var-pad-2": "0 0 0 2vw",
        "l-var-pad-3": "0 0 0 3vw",
        "l-var-pad-4": "0 0 0 4vw",
        "l-var-pad-5": "0 0 0 5vw",
        "l-var-pad-6": "0 0 0 6vw",
        "l-var-pad-7": "0 0 0 7vw",
        "l-var-pad-8": "0 0 0 8vw",
        "l-var-pad-9": "0 0 0 9vw",
        "l-var-pad-10": "0 0 0 10vw",
        "l-var-pad-11": "0 0 0 11vw",
        "l-var-pad-12": "0 0 0 12vw",
        "l-var-pad-13": "0 0 0 13vw",
        "l-var-pad-14": "0 0 0 14vw",
        "l-var-pad-15": "0 0 0 15vw",
        "l-var-pad-16": "0 0 0 16vw",
        "l-var-pad-17": "0 0 0 17vw",
        "l-var-pad-18": "0 0 0 18vw",
        "l-var-pad-19": "0 0 0 19vw",
        "l-var-pad-20": "0 0 0 20vw",        // 20% of viewport height
        // right
        "r-var-pad-1": "0 1vw 0 0",         // 1% of viewport height (exampade)
        "r-var-pad-2": "0 2vw 0 0",
        "r-var-pad-3": "0 3vw 0 0",
        "r-var-pad-4": "0 4vw 0 0",
        "r-var-pad-5": "0 5vw 0 0",
        "r-var-pad-6": "0 6vw 0 0",
        "r-var-pad-7": "0 7vw 0 0",
        "r-var-pad-8": "0 8vw 0 0",
        "r-var-pad-9": "0 9vw 0 0",
        "r-var-pad-10": "0 10vw 0 0",
        "r-var-pad-11": "0 11vw 0 0",
        "r-var-pad-12": "0 12vw 0 0",
        "r-var-pad-13": "0 13vw 0 0",
        "r-var-pad-14": "0 14vw 0 0",
        "r-var-pad-15": "0 15vw 0 0",
        "r-var-pad-16": "0 16vw 0 0",
        "r-var-pad-17": "0 17vw 0 0",
        "r-var-pad-18": "0 18vw 0 0",
        "r-var-pad-19": "0 19vw 0 0",
        "r-var-pad-20": "0 20vw 0 0",        // 20% of viewport height
      },
    },
  },
  plugins: [],
  breakpoints: {
    xl: 'min-width: 1921px',
  },
}
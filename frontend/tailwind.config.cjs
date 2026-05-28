/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        sand: "#f7f1e8",
        ink: "#1f1b17",
        clay: "#c96b3b",
        sage: "#8da27b",
        mist: "#dbe4e0",
      },
      boxShadow: {
        card: "0 20px 50px rgba(31, 27, 23, 0.08)",
      },
      fontFamily: {
        sans: ["'Avenir Next'", "ui-sans-serif", "system-ui", "sans-serif"],
      },
    },
  },
  plugins: [],
};

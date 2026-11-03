/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        darkBg: "#0B0F19",
        cardBg: "#111827",
        borderSubtle: "#1F2937",
        cyberCyan: "#06B6D4",
        cyberBlue: "#3B82F6",
        cyberGreen: "#10B981",
        cyberRed: "#EF4444",
        cyberPurple: "#8B5CF6",
        cyberAmber: "#F59E0B"
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        mono: ['Fira Code', 'monospace']
      }
    },
  },
  plugins: [],
}

import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/task": {
        target: "http://127.0.0.1:8000",
        changeOrigin: true,
      },
      "/tasks": {
        target: "http://127.0.0.1:8000",
        changeOrigin: true,
      },
    },
  },
  test: {
    environment: "jsdom",
    setupFiles: "./src/setupTests.js",
    include: ["test/**/*.test.{js,jsx}"],
    reporters: ["verbose", "html"],
    outputFile: { html: "./test-report/index.html" },
  },
});

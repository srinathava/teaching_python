import { defineConfig } from 'vitest/config';
import { sveltekit } from '@sveltejs/kit/vite';

export default defineConfig({
	plugins: [sveltekit()],

	server: {
		proxy: {
			'/api': {
				target: 'http://localhost:8000',
				changeOrigin: true
			}
		}
	},

	// Configure Vite to watch additional files
	optimizeDeps: {
		// Force Vite to consider exercises.json as a dependency
		// This ensures changes to this file trigger a reload
		include: ['src/lib/server/content/exercises.json']
	},

	test: {
		include: ['src/**/*.{test,spec}.{js,ts}']
	}
});

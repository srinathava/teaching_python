<script lang="ts">
  import { onMount } from 'svelte';
  import { popIn, slideIn } from '$lib/transitions';
  import LoginButton from '$lib/components/LoginButton.svelte';
  import '../app.css';
  import type { LayoutData } from './$types';
  
  export let data: LayoutData;
  let mounted = false;
  
  onMount(() => {
    mounted = true;
  });
</script>

<!-- Navigation -->
<nav class="bg-white shadow-sm">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex justify-between h-16">
      <div class="flex items-center">
        <!-- Logo -->
        <div class="flex-shrink-0 flex items-center">
          {#if mounted}
            <a href="/">
              <img 
                class="h-8 w-auto" 
                src="/logo.svg" 
                alt="Python Kids Logo"
                in:popIn={{duration: 400}}
              >
            </a>
          {/if}
        </div>
      </div>
      <!-- Navigation Links and Login -->
      <div class="flex items-center space-x-8">
        {#if mounted}
          <a
            href="/achievements"
            class="text-gray-700 hover:text-primary-blue px-3 py-2 rounded-md text-lg font-medium transition-colors"
            in:slideIn={{duration: 400, delay: 400}}
          >
            Achievements
          </a>
          <div in:slideIn={{duration: 400, delay: 600}}>
            <LoginButton />
          </div>
        {/if}
      </div>
    </div>
  </div>
</nav>

<main>
  <slot />
</main>

<style>
  /* Add Comic Neue font */
  @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@300;400;700&display=swap');
</style>

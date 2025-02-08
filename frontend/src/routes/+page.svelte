<script lang="ts">
  import { onMount } from 'svelte';
  import { float, popIn, slideIn } from '$lib/transitions';
  
  let mounted = false;
  
  interface LessonCard {
    icon: string;
    title: string;
    desc: string;
    href: string;
  }

  interface FeatureCard {
    icon: string;
    title: string;
    desc: string;
  }

  interface StepCard {
    icon: string;
    title: string;
    desc: string;
  }

  const lessonCards: LessonCard[] = [
    { icon: '🏷️', title: 'The Magic Label Maker', desc: 'Learn about variables and how they store different types of information.', href: '/lessons/variables' },
    { icon: '🎡', title: 'The Math Adventure Park', desc: 'Discover how to perform calculations and work with numbers.', href: '/lessons/operations' },
    { icon: '🤖', title: 'The Robot Game Master', desc: 'Learn how to make decisions in your code using if/else statements.', href: '/lessons/decisions' },
    { icon: '💃', title: 'The Robot Dance Academy', desc: 'Master the art of repeating actions using loops.', href: '/lessons/loops' },
    { icon: '👩‍🍳', title: 'The Recipe Lab', desc: 'Create reusable code recipes with functions.', href: '/lessons/functions' }
  ];

  const featureCards: FeatureCard[] = [
    { icon: '👩‍💻', title: 'Learn by Doing', desc: 'Write real code and see it come to life instantly!' },
    { icon: '🎮', title: 'Fun Challenges', desc: 'Solve exciting puzzles and create amazing projects!' },
    { icon: '✨', title: 'Instant Feedback', desc: 'Get helpful tips and celebrate your successes!' },
    { icon: '🏆', title: 'Earn Achievements', desc: 'Collect badges and track your progress!' }
  ];

  const stepCards: StepCard[] = [
    { icon: '1️⃣', title: 'Choose Your Adventure', desc: 'Pick your first exciting lesson to begin with' },
    { icon: '2️⃣', title: 'Follow the Story', desc: 'Learn through fun, interactive stories' },
    { icon: '3️⃣', title: 'Complete Challenges', desc: 'Practice your skills with exciting exercises' }
  ];
  
  onMount(() => {
    mounted = true;
  });
</script>

<!-- Hero Section -->
<div class="bg-gradient-to-b from-blue-50 to-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
    <div class="text-center">
      {#if mounted}
        <h1 
          class="text-4xl tracking-tight font-extrabold text-text-dark sm:text-5xl md:text-6xl font-comic-neue"
          in:float={{y: 20, duration: 1000}}
        >
          Learn Python Through Fun Adventures!
        </h1>
        <p 
          class="mt-3 max-w-md mx-auto text-base text-gray-500 sm:text-lg md:mt-5 md:text-xl md:max-w-3xl"
          in:float={{y: 20, duration: 1000, delay: 200}}
        >
          Join us on an exciting journey where coding meets creativity! Perfect for young minds ready to explore the world of programming.
        </p>
        <div 
          class="mt-5 max-w-md mx-auto sm:flex sm:justify-center md:mt-8"
          in:float={{y: 20, duration: 1000, delay: 400}}
        >
          <div class="rounded-md shadow">
            <a 
              href="/lessons/introduction" 
              class="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-primary-blue hover:bg-blue-600 md:py-4 md:text-lg md:px-10 transition-colors"
            >
              Start Learning
            </a>
          </div>
        </div>
      {/if}
    </div>
  </div>
</div>

<!-- Learning Path -->
<div class="py-12 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    {#if mounted}
      <div 
        class="text-center"
        in:float={{y: 20, duration: 1000}}
      >
        <h2 class="text-3xl font-extrabold text-text-dark font-comic-neue">
          Your Learning Adventure
        </h2>
        <p class="mt-4 max-w-2xl text-xl text-gray-500 mx-auto">
          Follow our carefully crafted path to master Python programming!
        </p>
      </div>

      <div class="mt-10">
        <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-5">
          {#each lessonCards as { icon, title, desc, href }, i}
            <div 
              class="relative group bg-white p-6 focus-within:ring-2 focus-within:ring-inset focus-within:ring-primary-blue rounded-lg shadow-sm hover:shadow-md transition-shadow"
              in:popIn={{duration: 400, delay: i * 100}}
            >
              <div>
                <span class="rounded-lg inline-flex p-3 bg-blue-50 text-blue-700 ring-4 ring-white">
                  {icon}
                </span>
              </div>
              <div class="mt-4">
                <h3 class="text-lg font-medium font-comic-neue">
                  <a {href} class="focus:outline-none">
                    <span class="absolute inset-0" aria-hidden="true"></span>
                    {title}
                  </a>
                </h3>
                <p class="mt-2 text-sm text-gray-500">
                  {desc}
                </p>
              </div>
            </div>
          {/each}
        </div>
      </div>
    {/if}
  </div>
</div>

<!-- Features Section -->
<div class="bg-gray-50 py-12">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    {#if mounted}
      <div 
        class="text-center"
        in:float={{y: 20, duration: 1000}}
      >
        <h2 class="text-3xl font-extrabold text-text-dark font-comic-neue">
          Why Learn With Us?
        </h2>
      </div>

      <div class="mt-10">
        <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4">
          {#each featureCards as { icon, title, desc }, i}
            <div 
              class="bg-white p-6 rounded-lg shadow-sm"
              in:popIn={{duration: 400, delay: 200 + i * 100}}
            >
              <div class="text-center">
                <span class="text-4xl">{icon}</span>
                <h3 class="mt-4 text-lg font-medium font-comic-neue">{title}</h3>
                <p class="mt-2 text-sm text-gray-500">
                  {desc}
                </p>
              </div>
            </div>
          {/each}
        </div>
      </div>
    {/if}
  </div>
</div>

<!-- Getting Started -->
<div class="bg-white py-12">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    {#if mounted}
      <div 
        class="text-center"
        in:float={{y: 20, duration: 1000}}
      >
        <h2 class="text-3xl font-extrabold text-text-dark font-comic-neue">
          Ready to Start?
        </h2>
        <p class="mt-4 max-w-2xl text-xl text-gray-500 mx-auto">
          Begin your coding adventure in three simple steps!
        </p>
      </div>

      <div class="mt-10">
        <div class="grid grid-cols-1 gap-8 sm:grid-cols-3">
          {#each stepCards as { icon, title, desc }, i}
            <div 
              class="text-center"
              in:slideIn={{duration: 400, delay: 400 + i * 100}}
            >
              <div class="text-4xl">{icon}</div>
              <h3 class="mt-4 text-lg font-medium font-comic-neue">{title}</h3>
              <p class="mt-2 text-sm text-gray-500">
                {desc}
              </p>
            </div>
          {/each}
        </div>

        <div 
          class="mt-10 text-center"
          in:float={{y: 20, duration: 1000, delay: 800}}
        >
          <a 
            href="/lessons/introduction" 
            class="inline-flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-primary-blue hover:bg-blue-600 md:py-4 md:text-lg md:px-10 transition-colors"
          >
            Begin Adventure
          </a>
        </div>
      </div>
    {/if}
  </div>
</div>

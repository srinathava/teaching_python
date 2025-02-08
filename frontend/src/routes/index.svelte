<script lang="ts">
  // Import any required components here
</script>

<svelte:head>
  <title>Learn Python Through Fun Adventures!</title>
</svelte:head>

<!-- Navigation -->
<nav class="bg-white shadow-sm">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex justify-between h-16">
      <div class="flex items-center">
        <!-- Logo -->
        <div class="flex-shrink-0 flex items-center">
          <img class="h-8 w-auto" src="/logo.svg" alt="Python Kids Logo">
        </div>
      </div>
      <!-- Navigation Links -->
      <div class="flex space-x-8">
        <a href="/lessons" class="text-gray-700 hover:text-blue-500 px-3 py-2 rounded-md text-lg font-medium">Lessons</a>
        <a href="/progress" class="text-gray-700 hover:text-blue-500 px-3 py-2 rounded-md text-lg font-medium">Progress</a>
        <a href="/achievements" class="text-gray-700 hover:text-blue-500 px-3 py-2 rounded-md text-lg font-medium">Achievements</a>
      </div>
    </div>
  </div>
</nav>

<!-- Hero Section -->
<div class="bg-gradient-to-b from-blue-50 to-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
    <div class="text-center">
      <h1 class="text-4xl tracking-tight font-extrabold text-gray-900 sm:text-5xl md:text-6xl font-comic-neue">
        Learn Python Through Fun Adventures!
      </h1>
      <p class="mt-3 max-w-md mx-auto text-base text-gray-500 sm:text-lg md:mt-5 md:text-xl md:max-w-3xl">
        Join us on an exciting journey where coding meets creativity! Perfect for young minds ready to explore the world of programming.
      </p>
      <div class="mt-5 max-w-md mx-auto sm:flex sm:justify-center md:mt-8">
        <div class="rounded-md shadow">
          <a href="/lessons/introduction" class="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-blue-500 hover:bg-blue-600 md:py-4 md:text-lg md:px-10">
            Start Learning
          </a>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Learning Path -->
<div class="py-12 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center">
      <h2 class="text-3xl font-extrabold text-gray-900 font-comic-neue">
        Your Learning Adventure
      </h2>
      <p class="mt-4 max-w-2xl text-xl text-gray-500 mx-auto">
        Follow our carefully crafted path to master Python programming!
      </p>
    </div>

    <div class="mt-10">
      <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-5">
        <!-- Variables -->
        <div class="relative group bg-white p-6 focus-within:ring-2 focus-within:ring-inset focus-within:ring-blue-500 rounded-lg shadow-sm hover:shadow-md transition-shadow">
          <div>
            <span class="rounded-lg inline-flex p-3 bg-blue-50 text-blue-700 ring-4 ring-white">
              🏷️
            </span>
          </div>
          <div class="mt-4">
            <h3 class="text-lg font-medium font-comic-neue">
              <a href="/lessons/variables" class="focus:outline-none">
                <span class="absolute inset-0" aria-hidden="true"></span>
                The Magic Label Maker
              </a>
            </h3>
            <p class="mt-2 text-sm text-gray-500">
              Learn about variables and how they store different types of information.
            </p>
          </div>
        </div>

        <!-- Basic Operations -->
        <div class="relative group bg-white p-6 focus-within:ring-2 focus-within:ring-inset focus-within:ring-blue-500 rounded-lg shadow-sm hover:shadow-md transition-shadow">
          <div>
            <span class="rounded-lg inline-flex p-3 bg-blue-50 text-blue-700 ring-4 ring-white">
              🎡
            </span>
          </div>
          <div class="mt-4">
            <h3 class="text-lg font-medium font-comic-neue">
              <a href="/lessons/operations" class="focus:outline-none">
                <span class="absolute inset-0" aria-hidden="true"></span>
                The Math Adventure Park
              </a>
            </h3>
            <p class="mt-2 text-sm text-gray-500">
              Discover how to perform calculations and work with numbers.
            </p>
          </div>
        </div>

        <!-- Making Decisions -->
        <div class="relative group bg-white p-6 focus-within:ring-2 focus-within:ring-inset focus-within:ring-blue-500 rounded-lg shadow-sm hover:shadow-md transition-shadow">
          <div>
            <span class="rounded-lg inline-flex p-3 bg-blue-50 text-blue-700 ring-4 ring-white">
              🤖
            </span>
          </div>
          <div class="mt-4">
            <h3 class="text-lg font-medium font-comic-neue">
              <a href="/lessons/decisions" class="focus:outline-none">
                <span class="absolute inset-0" aria-hidden="true"></span>
                The Robot Game Master
              </a>
            </h3>
            <p class="mt-2 text-sm text-gray-500">
              Learn how to make decisions in your code using if/else statements.
            </p>
          </div>
        </div>

        <!-- Loops -->
        <div class="relative group bg-white p-6 focus-within:ring-2 focus-within:ring-inset focus-within:ring-blue-500 rounded-lg shadow-sm hover:shadow-md transition-shadow">
          <div>
            <span class="rounded-lg inline-flex p-3 bg-blue-50 text-blue-700 ring-4 ring-white">
              💃
            </span>
          </div>
          <div class="mt-4">
            <h3 class="text-lg font-medium font-comic-neue">
              <a href="/lessons/loops" class="focus:outline-none">
                <span class="absolute inset-0" aria-hidden="true"></span>
                The Robot Dance Academy
              </a>
            </h3>
            <p class="mt-2 text-sm text-gray-500">
              Master the art of repeating actions using loops.
            </p>
          </div>
        </div>

        <!-- Functions -->
        <div class="relative group bg-white p-6 focus-within:ring-2 focus-within:ring-inset focus-within:ring-blue-500 rounded-lg shadow-sm hover:shadow-md transition-shadow">
          <div>
            <span class="rounded-lg inline-flex p-3 bg-blue-50 text-blue-700 ring-4 ring-white">
              👩‍🍳
            </span>
          </div>
          <div class="mt-4">
            <h3 class="text-lg font-medium font-comic-neue">
              <a href="/lessons/functions" class="focus:outline-none">
                <span class="absolute inset-0" aria-hidden="true"></span>
                The Recipe Lab
              </a>
            </h3>
            <p class="mt-2 text-sm text-gray-500">
              Create reusable code recipes with functions.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Features Section -->
<div class="bg-gray-50 py-12">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center">
      <h2 class="text-3xl font-extrabold text-gray-900 font-comic-neue">
        Why Learn With Us?
      </h2>
    </div>

    <div class="mt-10">
      <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4">
        <!-- Learn by Doing -->
        <div class="bg-white p-6 rounded-lg shadow-sm">
          <div class="text-center">
            <span class="text-4xl">👩‍💻</span>
            <h3 class="mt-4 text-lg font-medium font-comic-neue">Learn by Doing</h3>
            <p class="mt-2 text-sm text-gray-500">
              Write real code and see it come to life instantly!
            </p>
          </div>
        </div>

        <!-- Fun Challenges -->
        <div class="bg-white p-6 rounded-lg shadow-sm">
          <div class="text-center">
            <span class="text-4xl">🎮</span>
            <h3 class="mt-4 text-lg font-medium font-comic-neue">Fun Challenges</h3>
            <p class="mt-2 text-sm text-gray-500">
              Solve exciting puzzles and create amazing projects!
            </p>
          </div>
        </div>

        <!-- Instant Feedback -->
        <div class="bg-white p-6 rounded-lg shadow-sm">
          <div class="text-center">
            <span class="text-4xl">✨</span>
            <h3 class="mt-4 text-lg font-medium font-comic-neue">Instant Feedback</h3>
            <p class="mt-2 text-sm text-gray-500">
              Get helpful tips and celebrate your successes!
            </p>
          </div>
        </div>

        <!-- Earn Achievements -->
        <div class="bg-white p-6 rounded-lg shadow-sm">
          <div class="text-center">
            <span class="text-4xl">🏆</span>
            <h3 class="mt-4 text-lg font-medium font-comic-neue">Earn Achievements</h3>
            <p class="mt-2 text-sm text-gray-500">
              Collect badges and track your progress!
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Getting Started -->
<div class="bg-white py-12">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center">
      <h2 class="text-3xl font-extrabold text-gray-900 font-comic-neue">
        Ready to Start?
      </h2>
      <p class="mt-4 max-w-2xl text-xl text-gray-500 mx-auto">
        Begin your coding adventure in three simple steps!
      </p>
    </div>

    <div class="mt-10">
      <div class="grid grid-cols-1 gap-8 sm:grid-cols-3">
        <!-- Step 1 -->
        <div class="text-center">
          <div class="text-4xl">1️⃣</div>
          <h3 class="mt-4 text-lg font-medium font-comic-neue">Choose Your Adventure</h3>
          <p class="mt-2 text-sm text-gray-500">
            Pick your first exciting lesson to begin with
          </p>
        </div>

        <!-- Step 2 -->
        <div class="text-center">
          <div class="text-4xl">2️⃣</div>
          <h3 class="mt-4 text-lg font-medium font-comic-neue">Follow the Story</h3>
          <p class="mt-2 text-sm text-gray-500">
            Learn through fun, interactive stories
          </p>
        </div>

        <!-- Step 3 -->
        <div class="text-center">
          <div class="text-4xl">3️⃣</div>
          <h3 class="mt-4 text-lg font-medium font-comic-neue">Complete Challenges</h3>
          <p class="mt-2 text-sm text-gray-500">
            Practice your skills with exciting exercises
          </p>
        </div>
      </div>

      <div class="mt-10 text-center">
        <a href="/lessons/introduction" class="inline-flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-blue-500 hover:bg-blue-600 md:py-4 md:text-lg md:px-10">
          Begin Adventure
        </a>
      </div>
    </div>
  </div>
</div>

<style>
  /* Add Comic Neue font */
  @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@300;400;700&display=swap');
  
  /* Custom font classes */
  .font-comic-neue {
    font-family: 'Comic Neue', cursive;
  }
</style>
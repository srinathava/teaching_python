<!-- This file contains the visual content for the Circus Banner Maker exercise -->
<script>
  // You can add any Svelte-specific logic here if needed
</script>

<div class="exercise-content">
  <div class="exercise-description">
    <p>
      The circus needs personalized welcome banners for visitors. 
      Use Python's f-string formatting to create a welcome message!
    </p>
  </div>
  
  <div class="exercise-visual">
    <div class="banner-preview">
      <div class="banner">
        <h3>Welcome, Alex! Enjoy the juggling show!</h3>
      </div>
    </div>
    
    <div class="code-explanation">
      <p>
        F-strings are a powerful way to embed variables directly into strings.
        They start with the letter <code>f</code> before the opening quote:
      </p>
      <pre>f"Hello, &#123;name&#125;!"</pre>
      
      <p>
        The curly braces <code>&#123;&#125;</code> contain the variable names that will be
        replaced with their values when the string is created.
      </p>
    </div>
  </div>
</div>

<style>
  .exercise-content {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }
  
  .exercise-visual {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
  
  .banner-preview {
    display: flex;
    justify-content: center;
    margin: 1rem 0;
  }
  
  .banner {
    background-color: #f8d568;
    border: 3px solid #e67e22;
    border-radius: 8px;
    padding: 1rem 2rem;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .banner h3 {
    margin: 0;
    color: #d35400;
    font-size: 1.5rem;
  }
  
  .code-explanation {
    background-color: #f8f9fa;
    border-radius: 8px;
    padding: 1rem;
  }
  
  .code-explanation pre {
    background-color: #272822;
    color: #f8f8f2;
    padding: 0.5rem;
    border-radius: 4px;
    overflow-x: auto;
  }
</style>
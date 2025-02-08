<script lang="ts">
  import { onMount, onDestroy, createEventDispatcher } from 'svelte';
  import { browser } from '$app/environment';

  export let value = '';
  export let language = 'python';
  export let theme = 'vs-dark';
  export let height = '200px';

  let editorElement: HTMLElement;
  let editor: any;
  let monaco: any;

  // Create a custom event dispatcher
  const dispatch = createEventDispatcher<{
    change: string;
  }>();

  onMount(async () => {
    if (!browser) return;

    // Dynamically import monaco-editor only on the client side
    const monacoEditor = await import('monaco-editor');
    monaco = monacoEditor;

    editor = monaco.editor.create(editorElement, {
      value,
      language,
      theme,
      minimap: { enabled: false },
      scrollBeyondLastLine: false,
      lineNumbers: 'on',
      roundedSelection: false,
      automaticLayout: true,
      fontSize: 14,
      tabSize: 2,
      wordWrap: 'on',
      wrappingStrategy: 'advanced',
      scrollbar: {
        vertical: 'visible',
        horizontal: 'visible',
      },
    });

    // Handle content changes
    editor.onDidChangeModelContent(() => {
      const newValue = editor.getValue();
      value = newValue;
      dispatch('change', newValue);
    });

    // Set initial height
    editorElement.style.height = height;
  });

  onDestroy(() => {
    if (editor) {
      editor.dispose();
    }
  });

  // Update editor content when value prop changes
  $: if (editor && value !== editor.getValue()) {
    editor.setValue(value);
  }
</script>

<div 
  bind:this={editorElement} 
  class="monaco-editor-container rounded-lg overflow-hidden border border-gray-700"
></div>

<style>
  .monaco-editor-container {
    width: 100%;
    min-height: 200px;
  }

  :global(.monaco-editor .margin) {
    background-color: #1e1e1e !important;
  }
</style>
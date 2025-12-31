import os

tools = [
    # Chatbots
    {"id": "chatgpt", "name": "ChatGPT", "cat": "chatbots", "desc": "Leading conversational AI by OpenAI."},
    {"id": "claude", "name": "Claude", "cat": "chatbots", "desc": "Safe and helpful AI assistant by Anthropic."},
    {"id": "gemini", "name": "Gemini", "cat": "chatbots", "desc": "Google's most capable AI model."},
    {"id": "perplexity", "name": "Perplexity", "cat": "chatbots", "desc": "AI-powered search engine for instant answers."},
    {"id": "character-ai", "name": "Character.ai", "cat": "chatbots", "desc": "Chat with fictional and historical characters."},
    
    # Image
    {"id": "midjourney", "name": "Midjourney", "cat": "image", "desc": "High-quality AI image generation via Discord."},
    {"id": "dalle-3", "name": "DALL-E 3", "cat": "image", "desc": "OpenAI's latest text-to-image model."},
    {"id": "stable-diffusion", "name": "Stable Diffusion", "cat": "image", "desc": "Open-source image generation model."},
    {"id": "canva-ai", "name": "Canva AI", "cat": "image", "desc": "Design tools powered by AI."},
    {"id": "leonardo-ai", "name": "Leonardo.ai", "cat": "image", "desc": "Creative production platform for images."},
    
    # Video
    {"id": "runway", "name": "Runway", "cat": "video", "desc": "AI tools for professional video editing and generation."},
    {"id": "pika", "name": "Pika Labs", "cat": "video", "desc": "Idea-to-video platform for creators."},
    {"id": "sora", "name": "Sora", "cat": "video", "desc": "OpenAI's text-to-video model (upcoming)."},
    {"id": "heygen", "name": "HeyGen", "cat": "video", "desc": "AI video generator for business avatars."},
    {"id": "synthesia", "name": "Synthesia", "cat": "video", "desc": "Create AI videos from text in minutes."},
    
    # Coding
    {"id": "github-copilot", "name": "GitHub Copilot", "cat": "coding", "desc": "Your AI pair programmer."},
    {"id": "cursor", "name": "Cursor", "cat": "coding", "desc": "The AI-first code editor."},
    {"id": "replit-ghostwriter", "name": "Replit Ghostwriter", "cat": "coding", "desc": "AI coding assistant in the browser."},
    {"id": "tabnine", "name": "Tabnine", "cat": "coding", "desc": "AI assistant for software developers."},
    {"id": "codium", "name": "CodiumAI", "cat": "coding", "desc": "AI that generates meaningful tests for your code."},
    
    # Writing
    {"id": "jasper", "name": "Jasper", "cat": "writing", "desc": "AI content platform for enterprise teams."},
    {"id": "copy-ai", "name": "Copy.ai", "cat": "writing", "desc": "AI writing tool for marketing and sales."},
    {"id": "grammarly", "name": "Grammarly", "cat": "writing", "desc": "AI writing assistant for clear communication."},
    {"id": "writesonic", "name": "Writesonic", "cat": "writing", "desc": "AI writer for blogs, ads, and websites."},
    {"id": "notion-ai", "name": "Notion AI", "cat": "writing", "desc": "AI integrated directly into your workspace."},
    
    # Audio
    {"id": "elevenlabs", "name": "ElevenLabs", "cat": "audio", "desc": "The most realistic AI speech software."},
    {"id": "suno", "name": "Suno AI", "cat": "audio", "desc": "Generate full songs with vocals and instruments."},
    {"id": "udio", "name": "Udio", "cat": "audio", "desc": "Discover and create music with AI."},
    {"id": "descript", "name": "Descript", "cat": "audio", "desc": "Simple, powerful video and podcast editing."},
    {"id": "otter-ai", "name": "Otter.ai", "cat": "audio", "desc": "AI meeting assistant and transcription."},
]

template = """---
layout: page
title: {name}
category: {cat}
---

<div class="flex flex-col lg:flex-row gap-8 mt-4">
  <div class="flex-1">
    <h1 class="text-4xl font-bold text-slate-900 dark:text-white mb-4">{name}</h1>
    <p class="text-lg text-slate-600 dark:text-slate-400 mb-6">{desc}</p>
    
    <div class="space-y-4">
      <h2 class="text-xl font-semibold">Key Features</h2>
      <ul class="list-disc list-inside text-slate-700 dark:text-slate-300">
        <li>Advanced AI capabilities</li>
        <li>User-friendly interface</li>
        <li>Industry-leading performance</li>
      </ul>
    </div>

    <div class="mt-8">
      <a href="#" class="inline-block bg-blue-600 text-white px-8 py-3 rounded-lg font-medium hover:bg-blue-700 transition-colors">Visit Website</a>
    </div>
  </div>
  
  <div class="lg:w-1/2">
    <div class="bg-slate-100 dark:bg-slate-800 rounded-xl aspect-video flex items-center justify-center border-2 border-dashed border-slate-300 dark:border-slate-600">
      <span class="text-slate-400">Screenshot Placeholder</span>
    </div>
  </div>
</div>
"""

os.makedirs("docs/directory", exist_ok=True)

for tool in tools:
    path = f"docs/directory/{tool['id']}.md"
    with open(path, "w") as f:
        f.write(template.format(**tool))

print(f"Generated {len(tools)} tool pages.")

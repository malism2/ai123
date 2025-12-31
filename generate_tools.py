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
---

<div style="display: flex; flex-direction: row; gap: 2rem; margin-top: 2rem; flex-wrap: wrap;">
  <div style="flex: 1; min-width: 300px;">
    <h1 style="font-size: 2.5rem; font-weight: bold; margin-bottom: 1rem;">{name}</h1>
    <p style="font-size: 1.25rem; color: var(--vp-c-text-2); margin-bottom: 1.5rem;">{desc}</p>
    
    <div style="margin-top: 2rem;">
      <h2 style="font-size: 1.5rem; font-weight: 600; margin-bottom: 1rem;">Key Features</h2>
      <ul style="list-style-type: disc; padding-left: 1.5rem; color: var(--vp-c-text-2);">
        <li>Advanced AI capabilities</li>
        <li>User-friendly interface</li>
        <li>Industry-leading performance</li>
      </ul>
    </div>

    <div style="margin-top: 2.5rem;">
      <a href="#" style="display: inline-block; background-color: var(--vp-c-brand-1); color: white; padding: 0.75rem 2rem; border-radius: 0.5rem; font-weight: 500; text-decoration: none;">Visit Website</a>
    </div>
  </div>
  
  <div style="flex: 1; min-width: 300px;">
    <div class="screenshot-box">
      <span style="color: var(--vp-c-text-3);">Screenshot Placeholder</span>
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

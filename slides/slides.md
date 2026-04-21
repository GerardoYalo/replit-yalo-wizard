---
theme: default
title: "How to build your own Replit Dashboard on Yalo via Claude Code!"
info: "AI Friday — Replit Yalo Wizard"
author: ENG. GERARDO COLLANTE [CBA, ARG]
css: unocss
transition: slide-up
---

<style>
  .slidev-layout {
    background-color: #111111 !important;
    color: #FFFFFF !important;
    font-family: 'Inter', sans-serif !important;
  }
  @keyframes levitate {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
  }
  .animate-levitate {
    animation: levitate 1.5s ease-in-out infinite;
  }
  .glass-card {
    @apply bg-white/5 border border-[#EEAE3D]/20 backdrop-blur-md rounded-2xl p-6 relative overflow-hidden transition-all hover:border-[#EEAE3D]/50 hover:bg-white/10;
  }
  .glass-pill {
    @apply inline-block bg-white/10 border border-[#EEAE3D]/30 rounded-full px-5 py-1.5 text-sm font-medium text-white/90;
  }
  h1 { @apply font-['Poppins',sans-serif] text-5xl font-bold leading-tight tracking-tight; }
  h2 { @apply font-['Poppins',sans-serif] text-3xl font-semibold; }
  h3 { @apply font-['Poppins',sans-serif] text-xl font-semibold text-white; }
  p, li { @apply text-white/70 text-lg leading-relaxed; }
  .text-yalo-orange { @apply text-[#EEAE3D]; }
</style>

<Starfield />

<div class="h-full flex flex-col justify-center relative z-10">
  <img src="/yalo-logo.svg" style="filter: brightness(0) invert(1);" class="w-32 mb-8 opacity-90" />

  <div>
    <div class="glass-pill mb-8 inline-flex items-center justify-center whitespace-nowrap" v-motion :initial="{ y: 50, opacity: 0 }" :enter="{ y: 0, opacity: 1, transition: { type: 'spring', damping: 14 } }">
      <div class="i-ph-magic-wand-duotone text-lg text-[#EEAE3D] mr-1.5 flex-shrink-0"></div>
      <span class="leading-none relative top-[1px]">AI Friday</span>
    </div>
  </div>

  <h1 v-motion :initial="{ y: 50, opacity: 0 }" :enter="{ y: 0, opacity: 1, transition: { delay: 200, type: 'spring', damping: 14 } }">
    How to build your own<br>
    <span class="text-yalo-orange">Replit Dashboard</span>
  </h1>

  <p class="mt-6 text-xl text-white/80" v-motion :initial="{ y: 50, opacity: 0 }" :enter="{ y: 0, opacity: 1, transition: { delay: 400 } }">
    on Yalo via <img src="/claudecode-color.png" class="h-6 inline-block align-sub mx-1 animate-levitate" /> Claude Code!
  </p>

  <p class="mt-8 text-white/40 text-sm font-medium tracking-wide uppercase" v-motion :initial="{ y: 50, opacity: 0 }" :enter="{ y: 0, opacity: 1, transition: { delay: 600 } }">
    ENG. GERARDO COLLANTE [CBA, ARG]
  </p>
</div>

---
transition: fade
---

# The <span class="text-yalo-orange">Problem</span>

<div class="grid grid-cols-2 gap-6 mt-8">
  <div class="glass-card" v-click>
    <div class="i-ph-lock-key-duotone text-4xl text-yalo-orange mb-4"></div>
    <h3>Manual access</h3>
    <p class="mt-2 text-base">Ping Mario on #ask-mario every time someone needs Replit access</p>
  </div>
  <div class="glass-card" v-click>
    <div class="i-ph-question-duotone text-4xl text-yalo-orange mb-4"></div>
    <h3>No onboarding</h3>
    <p class="mt-2 text-base">No guide, no tutorial — people don't know where to start</p>
  </div>
  <div class="glass-card" v-click>
    <div class="i-ph-warning-duotone text-4xl text-yalo-orange mb-4"></div>
    <h3>Lost developers</h3>
    <p class="mt-2 text-base">Multiple people have lost access or can't find the workspace</p>
  </div>
  <div class="glass-card" v-click>
    <div class="i-ph-chart-line-up-duotone text-4xl text-yalo-orange mb-4"></div>
    <h3>Low adoption</h3>
    <p class="mt-2 text-base">Replit is approved but most Yaleros have never deployed an app</p>
  </div>
</div>

---
transition: slide-left
layout: center
class: text-center
---

<div class="glass-pill mb-8 mx-auto" v-motion :initial="{ scale: 0.8, opacity: 0 }" :enter="{ scale: 1, opacity: 1 }">💡 The Idea</div>

<h1 v-motion :initial="{ y: 30, opacity: 0 }" :enter="{ y: 0, opacity: 1, transition: { delay: 200 } }">
  What if an agent could<br><span class="text-yalo-orange">do the whole thing for you?</span>
</h1>

<div class="mt-8" v-click>
  <pre class="inline-block px-8 py-4 bg-black/40 border border-yalo-orange/30 rounded-xl shadow-[0_0_30px_rgba(238,174,61,0.15)]"><code class="text-yalo-orange font-mono text-2xl">/yalo-replit:wizard</code></pre>
</div>

<p class="mt-8 text-xl" v-click>One command. Access check → project setup → deploy → live URL.</p>

---
transition: fade
---

# What We <span class="text-yalo-orange">Built</span>

<div class="grid grid-cols-2 gap-6 mt-8">
  <div class="glass-card">
    <p class="text-yalo-orange text-xs font-bold uppercase tracking-widest mb-2 border-b border-yalo-orange/30 inline-block">Onboarding</p>
    <h2 class="mb-4 mt-2">/yalo-replit:wizard</h2>
    <p class="text-base text-white/70">7-phase flow from access check to live deployment. Handles GitHub, Replit config, and guides the user through every step.</p>
  </div>
  <div class="glass-card">
    <p class="text-yalo-orange text-xs font-bold uppercase tracking-widest mb-2 border-b border-yalo-orange/30 inline-block">Deploy</p>
    <h2 class="mb-4 mt-2">/yalo-replit:deploy</h2>
    <p class="text-base text-white/70">Triggered by "ready" or "deploy". Commits, pushes, tells you to click Redeploy. One command to go live.</p>
  </div>
</div>

<div class="mt-6 flex items-center justify-center p-4 bg-white/5 border border-white/10 rounded-xl" v-click>
  <div class="i-ph-stack-duotone text-2xl mr-3 text-yalo-orange"></div>
  <p class="text-base m-0"><strong>Stack:</strong> SKILL.md — natively supports dropdowns, Slack MCP, Bash. No Python runtime needed.</p>
</div>

---
transition: fade
---

# The <span class="text-yalo-orange">7 Phases</span>

<div class="mt-4 flex flex-col relative gap-2">
<div class="absolute left-[15px] top-4 h-[120px] w-0.5 bg-gradient-to-b from-[#EEAE3D] to-[#EEAE3D]/40 z-0"></div>

<div class="flex items-center z-10" v-click>
<div class="flex-shrink-0 w-8 h-8 rounded-full bg-[#111111] border-2 border-[#EEAE3D] text-[#EEAE3D] flex items-center justify-center font-bold text-sm shadow-[0_0_12px_rgba(238,174,61,0.5)]">1</div>
<div class="ml-6 glass-card !p-1.5 px-4 flex-grow flex items-center justify-between">
<span class="text-sm font-medium">Access check → Slack to Mario if needed</span>
<span class="text-[10px] px-2 py-[1px] bg-[#EEAE3D]/20 text-[#EEAE3D] rounded font-bold uppercase tracking-wider">auto</span>
</div>
</div>

<div class="flex items-center z-10" v-click>
<div class="flex-shrink-0 w-8 h-8 rounded-full bg-[#111111] border-2 border-[#EEAE3D] text-[#EEAE3D] flex items-center justify-center font-bold text-sm shadow-[0_0_12px_rgba(238,174,61,0.5)]">2</div>
<div class="ml-6 glass-card !p-1.5 px-4 flex-grow flex items-center justify-between">
<span class="text-sm font-medium">Project setup — template or from scratch</span>
<span class="text-[10px] px-2 py-[1px] bg-[#EEAE3D]/20 text-[#EEAE3D] rounded font-bold uppercase tracking-wider">auto</span>
</div>
</div>

<div class="flex items-center z-10" v-click>
<div class="flex-shrink-0 w-8 h-8 rounded-full bg-[#111111] border-2 border-[#EEAE3D] text-[#EEAE3D] flex items-center justify-center font-bold text-sm shadow-[0_0_12px_rgba(238,174,61,0.5)]">3</div>
<div class="ml-6 glass-card !p-1.5 px-4 flex-grow flex items-center justify-between">
<span class="text-sm font-medium">Iterate until you're happy</span>
<span class="text-[10px] px-2 py-[1px] bg-[#EEAE3D]/20 text-[#EEAE3D] rounded font-bold uppercase tracking-wider">auto</span>
</div>
</div>

<div class="grid grid-cols-2 gap-6 mt-1 relative">

<div class="flex flex-col gap-1.5 relative">
<div class="text-center text-[10px] text-white/50 font-bold uppercase tracking-widest border-b border-white/10 pb-0.5 mb-1" v-click>Path A: With GitHub</div>
<div class="absolute left-[15px] top-6 bottom-4 w-0.5 bg-gradient-to-b from-[#EEAE3D]/40 to-white/20 z-0"></div>

<div class="flex items-center z-10" v-click>
<div class="flex-shrink-0 w-8 h-8 rounded-full bg-[#111111] border-2 border-[#EEAE3D] text-[#EEAE3D] flex items-center justify-center font-bold text-sm shadow-[0_0_8px_rgba(238,174,61,0.3)]">4</div>
<div class="ml-3 glass-card !p-1.5 px-3 flex-grow flex items-center justify-between">
<span class="text-[0.7rem] font-medium">Create GitHub Repo</span>
</div>
</div>

<div class="flex items-center z-10" v-click>
<div class="flex-shrink-0 w-8 h-8 rounded-full bg-[#111111] border-2 border-[#EEAE3D] text-[#EEAE3D] flex items-center justify-center font-bold text-sm shadow-[0_0_8px_rgba(238,174,61,0.3)]">5</div>
<div class="ml-3 glass-card !p-1.5 px-3 flex-grow flex items-center justify-between">
<span class="text-[0.7rem] font-medium">Inject config (.replit + nix)</span>
</div>
</div>

<div class="flex items-center z-10" v-click>
<div class="flex-shrink-0 w-8 h-8 rounded-full bg-[#111111] border-2 border-white/30 text-white/50 flex items-center justify-center font-bold text-sm">6</div>
<div class="ml-3 glass-card !border-white/10 !bg-transparent !p-1.5 px-3 flex-grow flex items-center justify-between">
<span class="text-[0.7rem] text-white/60 font-medium">Import to Replit</span>
<span class="text-[8px] px-1 py-0.5 bg-white/10 text-white/40 rounded uppercase tracking-wider">manual</span>
</div>
</div>
</div>

<div class="flex flex-col gap-1.5 relative">
<div class="text-center text-[10px] text-white/50 font-bold uppercase tracking-widest border-b border-white/10 pb-0.5 mb-1" v-click>Path B: Without GitHub</div>
<div class="absolute left-[15px] top-6 bottom-4 w-0.5 bg-gradient-to-b from-white/30 to-white/10 z-0"></div>

<div class="flex items-center z-10" v-click>
<div class="flex-shrink-0 w-8 h-8 rounded-full bg-[#111111] border-2 border-white/40 text-white/80 flex items-center justify-center font-bold text-sm">4</div>
<div class="ml-3 glass-card !border-white/20 !p-1.5 px-3 flex-grow flex items-center justify-between">
<span class="text-[0.7rem] text-white/80 font-medium">Generate local ZIP</span>
</div>
</div>

<div class="flex items-center z-10" v-click>
<div class="flex-shrink-0 w-8 h-8 rounded-full bg-[#111111] border-2 border-white/40 text-white/80 flex items-center justify-center font-bold text-sm">5</div>
<div class="ml-3 glass-card !border-white/20 !p-1.5 px-3 flex-grow flex items-center justify-between">
<span class="text-[0.7rem] text-white/80 font-medium">Inject config (.replit + nix)</span>
</div>
</div>

<div class="flex items-center z-10" v-click>
<div class="flex-shrink-0 w-8 h-8 rounded-full bg-[#111111] border-2 border-white/30 text-white/50 flex items-center justify-center font-bold text-sm">6</div>
<div class="ml-3 glass-card !border-white/10 !bg-transparent !p-1.5 px-3 flex-grow flex items-center justify-between">
<span class="text-[0.7rem] text-white/60 font-medium">Upload at replit.com</span>
<span class="text-[8px] px-1 py-0.5 bg-white/10 text-white/40 rounded uppercase tracking-wider">manual</span>
</div>
</div>
</div>
</div>

<div class="flex items-center z-10 mt-1 mx-auto w-1/2" v-click>
<div class="flex-shrink-0 w-10 h-10 rounded-full bg-gradient-to-br from-pink-500 to-[#EEAE3D] text-white flex items-center justify-center font-black text-lg shadow-[0_0_15px_rgba(238,174,61,0.6)]">7</div>
<div class="ml-4 glass-card !border-[#EEAE3D]/50 !bg-[#EEAE3D]/10 !p-2 px-4 flex-grow flex items-center justify-between cursor-pointer">
<span class="text-sm text-white font-bold uppercase tracking-widest">Click Deploy!</span>
</div>
</div>
</div>

---
transition: slide-up
---

# Build <span class="text-yalo-orange">Together</span>

<p class="text-xl mt-4 text-white/80">The wizard doesn't just set up a pipeline. It helps you build your app.</p>

<div class="grid grid-cols-4 gap-4 mt-8">
  <div class="glass-card text-center flex flex-col items-center !p-4 hover:-translate-y-2 transition-transform" v-click>
    <div class="i-ph-squares-four-duotone text-5xl text-yalo-orange mb-3"></div>
    <h3 class="text-lg">Dashboard</h3>
    <p class="text-sm mt-2">Charts, metrics, filters</p>
  </div>
  <div class="glass-card text-center flex flex-col items-center !p-4 hover:-translate-y-2 transition-transform" v-click>
    <div class="i-ph-brain-duotone text-5xl text-yalo-orange mb-3"></div>
    <h3 class="text-lg">AI Tool</h3>
    <p class="text-sm mt-2">LLM-powered apps</p>
  </div>
  <div class="glass-card text-center flex flex-col items-center !p-4 hover:-translate-y-2 transition-transform" v-click>
    <div class="i-ph-clipboard-text-duotone text-5xl text-yalo-orange mb-3"></div>
    <h3 class="text-lg">Internal Tool</h3>
    <p class="text-sm mt-2">Forms & workflows</p>
  </div>
  <div class="glass-card text-center flex flex-col items-center !p-4 hover:-translate-y-2 transition-transform" v-click>
    <div class="i-ph-lightbulb-duotone text-5xl text-yalo-orange mb-3"></div>
    <h3 class="text-lg">Your Idea</h3>
    <p class="text-sm mt-2">Anything you want</p>
  </div>
</div>

<div class="mt-8 p-4 bg-yalo-orange/5 border border-yalo-orange/20 rounded-xl text-center" v-click>
  <p class="m-0 text-white flex items-center justify-center">
    <div class="i-ph-arrows-clockwise-duotone mr-2 text-2xl text-yalo-orange"></div> Iteration Loop:
    <span class="mx-2 font-mono text-sm opacity-80 text-yalo-orange">write code → preview → tweak → repeat → "looks great"</span>
  </p>
</div>

---
transition: fade
---

# Data via <span class="text-yalo-orange">Looker MCP</span>

<p class="text-xl mt-4 text-white/80">Your dashboard needs data — but Replit is a public runtime. Credentials can't live there.</p>

<div class="grid grid-cols-2 gap-6 mt-8">
  <div class="glass-card border-red-500/30" v-click>
    <div class="i-ph-prohibit-duotone text-4xl text-red-400 mb-3"></div>
    <h3 class="text-red-300">Direct BigQuery — NO</h3>
    <p class="mt-2 text-base">Service account keys in a Repl. Raw SQL without governance. Every dashboard re-inventing joins.</p>
  </div>
  <div class="glass-card border-[#EEAE3D]/50" v-click>
    <div class="i-ph-database-duotone text-4xl text-yalo-orange mb-3"></div>
    <h3 class="text-yalo-orange">Looker MCP — YES</h3>
    <p class="mt-2 text-base">Governed semantic layer. Auth handled once. The <code class="text-yalo-orange">looker-analytics</code> skill queries Explores for you.</p>
  </div>
</div>

<div class="mt-6 p-4 bg-yalo-orange/5 border border-yalo-orange/20 rounded-xl" v-click>
  <p class="m-0 flex items-center text-white">
    <div class="i-ph-shield-check-duotone text-2xl mr-2 text-yalo-orange"></div>
    Phase 2c of the wizard walks you through this — the setup guide is in Notion.
  </p>
</div>

---
transition: fade
---

# Looker MCP <span class="text-yalo-orange">Setup</span>

<p class="text-base mt-4 text-white/70">One-time setup — the wizard runs you through all of this in Phase 2c.</p>

<div class="flex flex-col gap-3 mt-6">
  <div class="glass-card !p-3 flex items-center" v-click>
    <div class="flex-shrink-0 w-9 h-9 rounded-full bg-yalo-orange/10 border border-yalo-orange/50 text-yalo-orange flex items-center justify-center font-bold mr-4">1</div>
    <div class="flex-grow">
      <h3 class="text-base m-0">Download the MCP bundle</h3>
      <p class="text-sm m-0 mt-1"><code class="text-yalo-orange">looker-mcp-connector.mcpb</code> — drag into Claude Code to install the connector</p>
    </div>
  </div>

  <div class="glass-card !p-3 flex items-center" v-click>
    <div class="flex-shrink-0 w-9 h-9 rounded-full bg-yalo-orange/10 border border-yalo-orange/50 text-yalo-orange flex items-center justify-center font-bold mr-4">2</div>
    <div class="flex-grow">
      <h3 class="text-base m-0">Install the governance skill</h3>
      <p class="text-sm m-0 mt-1"><code class="text-yalo-orange">looker-analytics-0.5.2.skill</code> — teaches Claude how to query Looker properly</p>
    </div>
  </div>

  <div class="glass-card !p-3 flex items-center" v-click>
    <div class="flex-shrink-0 w-9 h-9 rounded-full bg-yalo-orange/10 border border-yalo-orange/50 text-yalo-orange flex items-center justify-center font-bold mr-4">3</div>
    <div class="flex-grow">
      <h3 class="text-base m-0">Get Looker API credentials</h3>
      <p class="text-sm m-0 mt-1">Client ID + Secret — request in <code class="text-yalo-orange">#ask-mario</code> if you don't have them yet</p>
    </div>
  </div>
</div>

<div class="mt-5 glass-card border-yalo-orange/40 !py-3 flex items-center justify-center" v-click>
  <div class="i-ph-notion-logo-duotone text-3xl mr-3 text-yalo-orange"></div>
  <div>
    <p class="text-xs m-0 text-white/60 uppercase tracking-widest font-bold">Full guide on Notion</p>
    <p class="text-sm m-0 mt-1 text-yalo-orange font-mono break-all">notion.so/yalo/How-to-Set-Up-Looker-Analytics-in-Claude-Cowork-325d53382b23812496b5ef272fb4c26d</p>
  </div>
</div>

---
transition: slide-up
---

# Two Paths to <span class="text-yalo-orange">Replit</span>

<div class="grid grid-cols-2 gap-8 mt-10">
  <div class="glass-card hover:border-[#111111]/50 border-white/30 transition-colors" v-click>
    <div class="bg-white/5 border border-white/10 rounded-xl text-center mb-6 py-4">
      <div class="i-ph-github-logo-fill text-6xl text-white mx-auto"></div>
    </div>
    <h3 class="text-white mb-4 text-center">With GitHub</h3>
    <ul class="space-y-3 text-base">
      <li class="flex items-center"><div class="i-ph-arrow-right-bold text-white mr-2"></div> Agent creates repo, pushes code</li>
      <li class="flex items-center"><div class="i-ph-arrow-right-bold text-white mr-2"></div> User imports repo in Replit</li>
      <li class="flex items-center"><div class="i-ph-arrow-right-bold text-white mr-2"></div> `git push` → Redeploy for updates</li>
    </ul>
    <div class="mt-6 pt-4 border-t border-white/10 text-center text-white/50 font-medium text-sm uppercase">Best for ongoing projects</div>
  </div>

  <div class="glass-card hover:border-yalo-orange/50 transition-colors" v-click>
    <div class="bg-[#EEAE3D]/10 border border-[#EEAE3D]/30 rounded-xl text-center mb-6 py-4">
      <div class="i-ph-file-zip-duotone text-6xl text-yalo-orange mx-auto"></div>
    </div>
    <h3 class="text-yalo-orange mb-4 text-center">Without GitHub</h3>
    <ul class="space-y-3 text-base">
      <li class="flex items-center"><div class="i-ph-arrow-right-bold text-yalo-orange mr-2"></div> Agent creates ZIP file locally</li>
      <li class="flex items-center"><div class="i-ph-arrow-right-bold text-yalo-orange mr-2"></div> User uploads at replit.com/import</li>
      <li class="flex items-center"><div class="i-ph-arrow-right-bold text-yalo-orange mr-2"></div> Drag & drop for updates</li>
    </ul>
    <div class="mt-6 pt-4 border-t border-yalo-orange/20 text-center text-yalo-orange font-medium text-sm uppercase">Best for quick one-offs</div>
  </div>
</div>

---
transition: slide-up
layout: center
class: text-center
---

<div class="glass-pill mb-8 mx-auto border-yalo-orange text-yalo-orange bg-yalo-orange/10 transition-colors">🎬 Live Demo</div>

<h1 class="mb-8">Time to start the<br><span class="text-yalo-orange">Live Demo.</span></h1>

<div class="px-8 py-5 glass-card inline-block min-w-[500px] border-yalo-orange/30 shadow-[0_0_50px_rgba(238,174,61,0.15)] overflow-hidden text-left" v-motion :initial="{ scale: 0.9, opacity: 0 }" :enter="{ scale: 1, opacity: 1, transition: { delay: 300 } }">
  <div class="font-mono text-xl text-white/90 font-medium">
    <span class="text-white/40">❯</span>
    <span class="text-yalo-orange font-bold">/yalo-replit:</span><span class="text-white/70">wizard</span>
    <span class="inline-block w-2 bg-yalo-orange h-[1.1rem] align-middle ml-1 animate-pulse mb-1"></span>
  </div>
</div>

<p class="mt-10 text-white/50 flex flex-wrap items-center justify-center space-x-2 text-sm uppercase tracking-widest font-bold" v-motion :initial="{ opacity: 0 }" :enter="{ opacity: 1, transition: { delay: 600 } }">
  <span>Access check</span> <span class="text-yalo-orange mx-2">→</span>
  <span>template</span> <span class="text-yalo-orange mx-2">→</span>
  <span>dashboard</span> <span class="text-yalo-orange mx-2">→</span>
  <span>iterate</span> <span class="text-yalo-orange mx-2">→</span>
  <span>publish</span>
</p>

---
transition: slide-up
---

# The Deploy <span class="text-yalo-orange">Cycle</span>

<p class="text-xl my-6">After the one-time initial setup, the daily flow is incredibly simple:</p>

<div class="glass-card text-center !py-8 border-yalo-orange/30 bg-[#EEAE3D]/5" v-click>
  <p class="text-2xl font-medium tracking-wide flex items-center justify-center space-x-4">
    <span>Edit `app.py`</span>
    <span class="i-ph-arrow-right-bold text-yalo-orange opacity-50"></span>
    <span>say <span class="text-yalo-orange bg-black/60 px-3 py-1.5 rounded-lg border border-yalo-orange/30">"ready"</span></span>
    <span class="i-ph-arrow-right-bold text-yalo-orange opacity-50"></span>
    <span>agent pushes</span>
    <span class="i-ph-arrow-right-bold text-yalo-orange opacity-50"></span>
    <span>click <strong class="bg-black/60 px-3 py-1.5 rounded-lg text-white border border-white/30">Redeploy</strong></span>
    <span class="i-ph-arrow-right-bold text-yalo-orange opacity-50"></span>
    <span class="text-yalo-orange font-bold underline decoration-yalo-orange/50 underline-offset-4">Live</span>
  </p>
</div>

<div class="grid grid-cols-3 gap-6 mt-10">
  <div class="glass-card text-center flex flex-col items-center justify-center p-8" v-click>
    <div class="text-7xl font-black text-yalo-orange">5</div>
    <div class="mt-4 text-sm text-white/50 font-bold uppercase tracking-widest">Phases Automated</div>
  </div>
  <div class="glass-card text-center flex flex-col items-center justify-center p-8" v-click>
    <div class="text-7xl font-black text-yalo-orange">2</div>
    <div class="mt-4 text-sm text-white/50 font-bold uppercase tracking-widest">Browser Steps</div>
  </div>
  <div class="glass-card text-center flex flex-col items-center justify-center p-8" v-click>
    <div class="text-7xl font-black text-yalo-orange">1</div>
    <div class="mt-4 text-sm text-white/50 font-bold uppercase tracking-widest">Click per Deploy</div>
  </div>
</div>

---
transition: fade
---

# How to <span class="text-yalo-orange">Install</span>

<div class="flex flex-col gap-6 mt-8">
  <div class="glass-card" v-click>
    <h3 class="mb-4 flex items-center"><div class="i-ph-download-simple-duotone text-3xl text-yalo-orange mr-2"></div> One-time setup</h3>
    <pre class="bg-black/60 border border-white/10 rounded-xl p-4 !text-sm leading-relaxed overflow-x-auto"><code class="text-white/80"><span class="text-white/30 block mb-2"># Inside Claude Code</span><span class="text-white/50">/plugin</span> <span class="text-white">marketplace add GerardoYalo/replit-yalo-wizard</span><br><span class="text-white/50">/plugin</span>                <span class="text-white/30">← select and enable yalo-replit</span><br><span class="text-white/50">/reload-plugins</span></code></pre>
  </div>

  <div class="glass-card border-yalo-orange/30 bg-[#EEAE3D]/5" v-click>
    <h3 class="mb-4 flex items-center text-yalo-orange"><div class="i-ph-play-circle-duotone text-3xl text-yalo-orange mr-2"></div> Usage</h3>
    <pre class="bg-black/60 border border-white/10 rounded-xl p-4 !text-sm leading-relaxed overflow-x-auto"><code class="text-white/80"><span class="text-white/30 block mb-2"># Start building something</span><span class="text-yalo-orange font-bold">/yalo-replit:wizard</span><br><br><span class="text-white/30 block mt-4 mb-2"># Deploy your updates</span><span class="text-yalo-orange font-bold">/yalo-replit:deploy</span></code></pre>
  </div>
</div>

<div class="mt-8 glass-card border flex items-center justify-center font-medium opacity-80" v-click>
  <div class="i-ph-info-duotone mr-2 text-2xl text-yalo-orange"></div> Works entirely on your local machine — no extra runtime required.
</div>

---
transition: fade
---

# <span class="text-yalo-orange">Key Takeaways</span>

<div class="mt-8 flex flex-col gap-4">
  <div class="glass-card !p-4 flex items-center" v-click>
    <div class="flex-shrink-0 w-10 h-10 rounded-full bg-yalo-orange/10 border border-yalo-orange/50 text-yalo-orange flex items-center justify-center font-bold text-lg mr-5 shadow-[0_0_15px_rgba(238,174,61,0.2)]">1</div>
    <p class="m-0 text-lg"><strong class="text-white">SKILL.md > Agent SDK</strong> for wizard-style sequential flows in Claude Code</p>
  </div>

  <div class="glass-card !p-4 flex items-center" v-click>
    <div class="flex-shrink-0 w-10 h-10 rounded-full bg-yalo-orange/10 border border-yalo-orange/50 text-yalo-orange flex items-center justify-center font-bold text-lg mr-5 shadow-[0_0_15px_rgba(238,174,61,0.2)]">2</div>
    <p class="m-0 text-lg"><strong class="text-white">Plugins are easy to distribute</strong> — marketplace + 2 install commands</p>
  </div>

  <div class="glass-card !p-4 flex items-center" v-click>
    <div class="flex-shrink-0 w-10 h-10 rounded-full bg-yalo-orange/10 border border-yalo-orange/50 text-yalo-orange flex items-center justify-center font-bold text-lg mr-5 shadow-[0_0_15px_rgba(238,174,61,0.2)]">3</div>
    <p class="m-0 text-lg"><strong class="text-white">The wizard should own the flow</strong> — do the active work, don't just instruct</p>
  </div>

  <div class="glass-card !p-4 flex items-center" v-click>
    <div class="flex-shrink-0 w-10 h-10 rounded-full bg-yalo-orange/10 border border-yalo-orange/50 text-yalo-orange flex items-center justify-center font-bold text-lg mr-5 shadow-[0_0_15px_rgba(238,174,61,0.2)]">4</div>
    <p class="m-0 text-lg"><strong class="text-white">Governed data via MCP</strong> — no credentials on Replit, no raw SQL</p>
  </div>

  <div class="glass-card !p-4 flex items-center" v-click>
    <div class="flex-shrink-0 w-10 h-10 rounded-full bg-yalo-orange/10 border border-yalo-orange/50 text-yalo-orange flex items-center justify-center font-bold text-lg mr-5 shadow-[0_0_15px_rgba(238,174,61,0.2)]">5</div>
    <p class="m-0 text-lg"><strong class="text-white">Ship the config Replit expects</strong> — embrace the platform</p>
  </div>
</div>

---
layout: center
class: text-center
---

<h1 class="text-8xl mb-8">Questions? <span class="text-yalo-orange">🤔</span></h1>

<div v-click class="absolute inset-0 bg-[#111111] z-50 flex flex-col items-center justify-center">
  <Fireworks />

  <h1 class="text-[9rem] font-black leading-none bg-gradient-to-br from-yalo-orange via-pink-400 to-yalo-orange bg-clip-text text-transparent filter drop-shadow-[0_0_60px_rgba(238,174,61,0.6)] mb-8" v-motion :initial="{ scale: 0.5, opacity: 0 }" :enter="{ scale: 1, opacity: 1, transition: { type: 'spring', damping: 10 } }">
    THANK YOU!
  </h1>
</div>

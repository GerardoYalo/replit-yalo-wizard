---
theme: none
title: "From Local to Live in 5 Minutes"
info: "AI Friday — Replit Yalo Wizard"
author: Gerardo Collante
css: unocss
---

<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Inter:wght@300;400;500;600;700&family=Fira+Code:wght@300;400&display=swap">

<style>
  :root {
    --yalo-bg: #0F0F1C;
    --yalo-card: #1A1A2E;
    --yalo-border: #2A2A3E;
    --yalo-text: #FFFFFF;
    --yalo-muted: #888899;
    --yalo-purple: #8B5CF6;
    --yalo-pink: #EC4899;
    --yalo-orange: #F59E0B;
    --yalo-teal: #06B6D4;
  }
  .slidev-layout {
    background: var(--yalo-bg) !important;
    color: var(--yalo-text) !important;
    font-family: 'Inter', -apple-system, sans-serif !important;
    padding: 3rem 4rem !important;
  }
  .slidev-layout::after {
    content: '';
    position: absolute;
    bottom: 24px;
    left: 40px;
    width: 60px;
    height: 30px;
    background-image: url('/yalo-white.svg');
    background-size: contain;
    background-repeat: no-repeat;
    opacity: 0.4;
  }
  h1 {
    font-family: 'Poppins', sans-serif !important;
    font-size: 3.2rem !important;
    font-weight: 700 !important;
    line-height: 1.1 !important;
    letter-spacing: -0.5px !important;
  }
  h2 {
    font-family: 'Poppins', sans-serif !important;
    font-size: 1.8rem !important;
    font-weight: 600 !important;
    color: #CCCCDD !important;
  }
  h3 {
    font-family: 'Poppins', sans-serif !important;
    font-size: 1.3rem !important;
    font-weight: 600 !important;
  }
  p, li {
    color: #AAAABC !important;
    font-size: 1.1rem !important;
    line-height: 1.7 !important;
  }
  code {
    font-family: 'Fira Code', monospace !important;
    background: var(--yalo-card) !important;
    border: 1px solid var(--yalo-border) !important;
    color: var(--yalo-teal) !important;
    padding: 2px 8px !important;
    border-radius: 6px !important;
  }
  pre {
    font-family: 'Fira Code', monospace !important;
    background: var(--yalo-card) !important;
    border: 1px solid var(--yalo-border) !important;
    border-radius: 12px !important;
  }
  .grad {
    background: linear-gradient(135deg, #8B5CF6, #EC4899, #F59E0B);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .grad-teal {
    background: linear-gradient(135deg, #06B6D4, #8B5CF6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .card {
    background: var(--yalo-card);
    border: 1px solid var(--yalo-border);
    border-radius: 16px;
    padding: 1.5rem;
  }
  .metric-value {
    font-size: 2.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #8B5CF6, #EC4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .metric-label {
    color: var(--yalo-muted);
    font-size: 0.9rem;
    margin-top: 0.3rem;
  }
  .pill {
    display: inline-block;
    background: var(--yalo-card);
    border: 1px solid var(--yalo-border);
    border-radius: 999px;
    padding: 6px 20px;
    font-size: 0.85rem;
    color: #CCCCDD;
  }
  .phase-num {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: linear-gradient(135deg, #8B5CF6, #EC4899);
    color: white;
    font-weight: 700;
    font-size: 0.9rem;
    margin-right: 12px;
    flex-shrink: 0;
  }
  .phase-row {
    display: flex;
    align-items: center;
    padding: 10px 0;
    font-size: 1.1rem;
    color: #CCCCDD;
  }
  .tag-auto {
    display: inline-block;
    background: rgba(6, 182, 212, 0.15);
    color: #06B6D4;
    padding: 2px 10px;
    border-radius: 6px;
    font-size: 0.75rem;
    margin-left: 8px;
  }
  .tag-manual {
    display: inline-block;
    background: rgba(236, 72, 153, 0.15);
    color: #EC4899;
    padding: 2px 10px;
    border-radius: 6px;
    font-size: 0.75rem;
    margin-left: 8px;
  }
  table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    background: var(--yalo-card);
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid var(--yalo-border);
  }
  th {
    background: rgba(139, 92, 246, 0.1) !important;
    color: #CCCCDD !important;
    padding: 12px 16px !important;
    font-size: 0.85rem !important;
    text-transform: uppercase;
    letter-spacing: 1px;
  }
  td {
    padding: 12px 16px !important;
    color: #AAAABC !important;
    border-top: 1px solid var(--yalo-border) !important;
  }
</style>

<div style="display:flex; flex-direction:column; justify-content:center; height:100%;">
  <img src="/yalo-white.svg" style="width:100px; margin-bottom:2rem; opacity:0.9;" />
  <div class="pill" style="margin-bottom:2rem;">✨ AI Friday</div>
  <h1>From Local to Live<br><span class="grad">in 5 Minutes.</span></h1>
  <p style="margin-top:1.5rem; font-size:1.2rem;">Building and shipping a Claude Code plugin<br>for Replit onboarding.</p>
  <p style="margin-top:2rem; color:#666677; font-size:0.95rem;">Gerardo Collante · April 2026</p>
</div>

---

<div style="display:flex; flex-direction:column; justify-content:center; height:100%;">
  <h1>The <span class="grad">Problem</span></h1>
  <br>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-top:1rem;">
    <div class="card">
      <h3>🔒 Manual access</h3>
      <p>Ping Mario on #ask-mario every time someone needs Replit access</p>
    </div>
    <div class="card">
      <h3>📭 No onboarding</h3>
      <p>No guide, no tutorial — people don't know where to start</p>
    </div>
    <div class="card">
      <h3>😵 Lost developers</h3>
      <p>Multiple people have lost access or can't find the workspace</p>
    </div>
    <div class="card">
      <h3>📉 Low adoption</h3>
      <p>Replit is approved but most Yaleros have never deployed an app</p>
    </div>
  </div>
</div>

---

<div style="display:flex; flex-direction:column; justify-content:center; align-items:center; height:100%; text-align:center;">
  <div class="pill" style="margin-bottom:2rem;">💡 The Idea</div>
  <h1>What if an agent could<br><span class="grad">do the whole thing for you?</span></h1>
  <br>
  <pre style="padding:1.2rem 2rem; font-size:1.3rem; margin-top:1rem;"><code>/yalo-replit:wizard</code></pre>
  <p style="margin-top:1.5rem;">One command. Access check → project setup → deploy → live URL.</p>
</div>

---

<div style="display:flex; flex-direction:column; justify-content:center; height:100%;">
  <h1>What We <span class="grad">Built</span></h1>
  <br>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;">
    <div class="card">
      <p style="color:#8B5CF6; font-size:0.85rem; text-transform:uppercase; letter-spacing:1px;">Onboarding</p>
      <h2 style="margin:0.5rem 0;">/yalo-replit:wizard</h2>
      <p>7-phase flow from access check to live deployment. Handles GitHub, Replit config, and guides the user through every step.</p>
    </div>
    <div class="card">
      <p style="color:#EC4899; font-size:0.85rem; text-transform:uppercase; letter-spacing:1px;">Deploy</p>
      <h2 style="margin:0.5rem 0;">/yalo-replit:deploy</h2>
      <p>Triggered by "ready" or "deploy". Commits, pushes, tells you to click Redeploy. One command to go live.</p>
    </div>
  </div>
  <p style="margin-top:1.5rem; font-size:1rem;"><strong>Stack:</strong> SKILL.md — natively supports dropdowns, Slack MCP, Bash. No Python runtime needed.</p>
</div>

---

<div style="display:flex; flex-direction:column; justify-content:center; height:100%;">
  <h1>Why <span class="grad-teal">SKILL.md</span> over Agent SDK</h1>
  <br>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;">
    <div class="card" style="border-color: rgba(6,182,212,0.3);">
      <h3 style="color:#06B6D4;">SKILL.md ✅</h3>
      <p>Native AskUserQuestion dropdowns</p>
      <p>Native MCP tools (Slack, GitHub)</p>
      <p>Runs inside Claude Code</p>
      <p>Zero runtime dependencies</p>
      <p>Distributable as a plugin</p>
    </div>
    <div class="card" style="opacity: 0.5;">
      <h3>Python Agent SDK</h3>
      <p>Needs Python runtime</p>
      <p>Needs separate packaging</p>
      <p>Needs API keys</p>
      <p>Overkill for a wizard flow</p>
    </div>
  </div>
</div>

---

<div style="display:flex; flex-direction:column; justify-content:center; height:100%;">
  <h1>The <span class="grad">7 Phases</span></h1>
  <br>
  <div class="phase-row"><span class="phase-num">1</span> Access check → Slack to Mario if needed <span class="tag-auto">auto</span></div>
  <div class="phase-row"><span class="phase-num">2</span> Project setup — template or from scratch <span class="tag-auto">auto</span></div>
  <div class="phase-row"><span class="phase-num">3</span> Build together — iterate until happy <span class="tag-auto">auto</span></div>
  <div class="phase-row"><span class="phase-num">4</span> GitHub repo or ZIP for non-GitHub users <span class="tag-auto">auto</span></div>
  <div class="phase-row"><span class="phase-num">5</span> Replit config (.replit + replit.nix) <span class="tag-auto">auto</span></div>
  <div class="phase-row"><span class="phase-num">6</span> Import to Replit <span class="tag-manual">browser</span></div>
  <div class="phase-row"><span class="phase-num">7</span> Click Deploy <span class="tag-manual">browser</span></div>
</div>

---

<div style="display:flex; flex-direction:column; justify-content:center; height:100%;">
  <h1>Build <span class="grad">Together</span></h1>
  <p style="font-size:1.2rem; margin:1rem 0;">The wizard doesn't just set up a pipeline. It helps you build your app.</p>
  <br>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:1rem;">
    <div class="card" style="text-align:center; padding:2rem 1rem;">
      <div style="font-size:2rem;">📊</div>
      <h3 style="margin-top:0.8rem;">Dashboard</h3>
      <p style="font-size:0.9rem;">Charts, metrics, filters</p>
    </div>
    <div class="card" style="text-align:center; padding:2rem 1rem;">
      <div style="font-size:2rem;">🤖</div>
      <h3 style="margin-top:0.8rem;">AI Tool</h3>
      <p style="font-size:0.9rem;">LLM-powered apps</p>
    </div>
    <div class="card" style="text-align:center; padding:2rem 1rem;">
      <div style="font-size:2rem;">🛠️</div>
      <h3 style="margin-top:0.8rem;">Internal Tool</h3>
      <p style="font-size:0.9rem;">Forms & workflows</p>
    </div>
    <div class="card" style="text-align:center; padding:2rem 1rem;">
      <div style="font-size:2rem;">💡</div>
      <h3 style="margin-top:0.8rem;">Your Idea</h3>
      <p style="font-size:0.9rem;">Anything you want</p>
    </div>
  </div>
  <p style="margin-top:1.5rem;">Iterate: write code → preview → tweak → repeat → "looks great, let's publish"</p>
</div>

---

<div style="display:flex; flex-direction:column; justify-content:center; height:100%;">
  <h1>Two Paths to <span class="grad">Replit</span></h1>
  <br>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.5rem;">
    <div class="card" style="border-color: rgba(6,182,212,0.3);">
      <h3 style="color:#06B6D4;">With GitHub</h3>
      <p>Agent creates repo → pushes code</p>
      <p>User imports from GitHub in Replit</p>
      <p><code>git push</code> → Redeploy for updates</p>
      <p style="color:#06B6D4; margin-top:1rem;">Best for ongoing projects</p>
    </div>
    <div class="card" style="border-color: rgba(236,72,153,0.3);">
      <h3 style="color:#EC4899;">Without GitHub</h3>
      <p>Agent creates ZIP file</p>
      <p>User uploads at replit.com/import</p>
      <p>Drag & drop for updates</p>
      <p style="color:#EC4899; margin-top:1rem;">Best for quick one-offs</p>
    </div>
  </div>
</div>

---

<div style="display:flex; flex-direction:column; justify-content:center; height:100%;">
  <h1>Lessons <span class="grad">Learned</span></h1>
  <p style="font-size:1.1rem; margin:1rem 0 2rem;">Things that broke along the way.</p>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem;">
    <div class="card">
      <h3>🐍 Python in Nix</h3>
      <p><code>uv run</code> needs <code>python311Full</code> in the Nix env — it's not there by default.</p>
    </div>
    <div class="card">
      <h3>📦 libstdc++ for numpy</h3>
      <p>numpy/pandas need <code>pkgs.stdenv.cc.cc.lib</code> + <code>LD_LIBRARY_PATH</code>.</p>
    </div>
    <div class="card">
      <h3>🔀 Replit modifies your files</h3>
      <p>Always <code>git pull --rebase</code> before pushing. Replit adds workflows and ports config.</p>
    </div>
    <div class="card">
      <h3>📋 Ship Replit's own config</h3>
      <p>Copy the exact <code>.replit</code> that Replit generates. Don't fight it.</p>
    </div>
  </div>
</div>

---

<div style="display:flex; flex-direction:column; justify-content:center; align-items:center; height:100%; text-align:center;">
  <div class="pill" style="margin-bottom:2rem;">🎬 Live Demo</div>
  <h1>Let's build and deploy<br><span class="grad">something real.</span></h1>
  <br>
  <pre style="padding:1.2rem 2rem; font-size:1.3rem;"><code>/yalo-replit:wizard</code></pre>
  <br>
  <p style="font-size:1.1rem;">Access check → template → dashboard → iterate → publish → live URL</p>
</div>

---

<div style="display:flex; flex-direction:column; justify-content:center; height:100%;">
  <h1>The Deploy <span class="grad-teal">Cycle</span></h1>
  <p style="font-size:1.2rem; margin:1rem 0 2rem;">After initial setup, the daily flow is:</p>
  <div class="card" style="text-align:center; padding:2rem;">
    <p style="font-size:1.3rem; color:#FFFFFF;">
      Edit <code>app.py</code> → say <code>"ready"</code> → agent pushes → click <strong>Redeploy</strong> → live
    </p>
  </div>
  <br>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:1rem;">
    <div class="card" style="text-align:center;">
      <div class="metric-value">5</div>
      <div class="metric-label">phases automated</div>
    </div>
    <div class="card" style="text-align:center;">
      <div class="metric-value">2</div>
      <div class="metric-label">browser steps (one-time)</div>
    </div>
    <div class="card" style="text-align:center;">
      <div class="metric-value">1</div>
      <div class="metric-label">click per deploy</div>
    </div>
  </div>
</div>

---

<div style="display:flex; flex-direction:column; justify-content:center; height:100%;">
  <h1>How to <span class="grad">Install</span></h1>
  <br>
  <div class="card" style="padding:2rem;">

```bash
# One time setup
/plugin marketplace add GerardoYalo/replit-yalo-wizard
/plugin install yalo-replit
/reload-plugins
```

  </div>
  <br>
  <div class="card" style="padding:2rem;">

```bash
# Run the wizard
/yalo-replit:wizard

# Deploy updates
/yalo-replit:deploy
```

  </div>
</div>

---

<div style="display:flex; flex-direction:column; justify-content:center; height:100%;">
  <h1>Build Your Own <span class="grad">Plugin</span></h1>
  <p style="font-size:1.1rem; margin:1rem 0 2rem;">This same pattern works for any internal tool.</p>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem;">
    <div class="card">
      <h3>🎓 Onboarding wizards</h3>
      <p>Replit, GitHub, Datadog, any tool</p>
    </div>
    <div class="card">
      <h3>📊 Data dashboards</h3>
      <p>Looker MCP → Streamlit → Replit → shareable URL</p>
    </div>
    <div class="card">
      <h3>💬 Slack bots</h3>
      <p>Automated messages via MCP</p>
    </div>
    <div class="card">
      <h3>⚡ Code generators</h3>
      <p>Templates, scaffolding, boilerplate</p>
    </div>
  </div>
</div>

---

<div style="display:flex; flex-direction:column; justify-content:center; height:100%;">
  <h1><span class="grad">Key Takeaways</span></h1>
  <br>
  <div style="display:flex; flex-direction:column; gap:1rem;">
    <div class="card" style="display:flex; align-items:center; gap:1rem;">
      <span class="phase-num">1</span>
      <p style="margin:0;"><strong>SKILL.md > Agent SDK</strong> for wizard-style flows in Claude Code</p>
    </div>
    <div class="card" style="display:flex; align-items:center; gap:1rem;">
      <span class="phase-num">2</span>
      <p style="margin:0;"><strong>Plugins are easy to distribute</strong> — marketplace + 2 install commands</p>
    </div>
    <div class="card" style="display:flex; align-items:center; gap:1rem;">
      <span class="phase-num">3</span>
      <p style="margin:0;"><strong>The wizard should own the flow</strong> — do the work, don't just instruct</p>
    </div>
    <div class="card" style="display:flex; align-items:center; gap:1rem;">
      <span class="phase-num">4</span>
      <p style="margin:0;"><strong>Be honest about manual steps</strong> — set expectations upfront</p>
    </div>
    <div class="card" style="display:flex; align-items:center; gap:1rem;">
      <span class="phase-num">5</span>
      <p style="margin:0;"><strong>Ship the config Replit expects</strong> — don't fight the platform</p>
    </div>
  </div>
</div>

---

<div style="display:flex; flex-direction:column; justify-content:center; align-items:center; height:100%; text-align:center;">
  <h1>Questions? <span class="grad">🤔</span></h1>
  <br>
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:1.5rem; margin-top:2rem;">
    <div class="card" style="text-align:center;">
      <p style="color:var(--yalo-muted); font-size:0.8rem; text-transform:uppercase; letter-spacing:1px;">Repo</p>
      <p style="color:#06B6D4;">GerardoYalo/<br>replit-yalo-wizard</p>
    </div>
    <div class="card" style="text-align:center;">
      <p style="color:var(--yalo-muted); font-size:0.8rem; text-transform:uppercase; letter-spacing:1px;">Replit Access</p>
      <p style="color:#EC4899;">#ask-mario</p>
    </div>
    <div class="card" style="text-align:center;">
      <p style="color:var(--yalo-muted); font-size:0.8rem; text-transform:uppercase; letter-spacing:1px;">Ticket</p>
      <p style="color:#8B5CF6;">YI-3728</p>
    </div>
  </div>
</div>

---

<div style="display:flex; flex-direction:column; justify-content:center; align-items:center; height:100%; text-align:center;">
  <h1 style="font-size:4rem;"><span class="grad">Thanks!</span> 🚀</h1>
  <br>
  <p style="font-size:1.2rem;">Built entirely with Claude Code — including this presentation.</p>
</div>

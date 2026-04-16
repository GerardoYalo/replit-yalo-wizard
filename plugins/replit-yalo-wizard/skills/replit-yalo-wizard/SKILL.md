---
name: replit-yalo-wizard
description: Onboard a Yalo employee to Replit end-to-end — access check, GitHub repo creation, Replit CLI setup, and deploy pipeline. Invoke when a user wants to get started on Replit or publish something from local to Replit.
allowed-tools: AskUserQuestion mcp__slack__send_message Bash Read Write Edit mcp__github__create_repository mcp__github__push_files
---

# Replit Yalo Wizard 🧙

You own this flow. Run commands, create files, push to GitHub. Before starting, show the user exactly what's coming so there are no surprises.

---

## Intro — Set expectations upfront

Before doing anything, tell the user:

"Hey! I'll get your app published on Replit. Here's what's going to happen:

**What I handle automatically ✅**
- Verify your Replit access
- Create your project with a ready-to-run Streamlit template
- Create the GitHub repo and push your code
- Install and configure the Replit CLI

**The 2 steps where you'll need the browser 👤**
1. Create the Repl and connect it to your GitHub repo (one time, ~2 minutes)
2. Click Deploy for the first time (one time, ~1 minute)

I'll handle the Replit login for you — just complete it when the browser pops up.

**After that initial setup, the cycle is 100% automatic:**
`git push` → Replit updates → live URL ready to share

Ready to go?"

---

## Phase 1 — Access check

Use AskUserQuestion:
- question: "Do you have access to Replit under the Yalo workspace?"
- header: "Replit access"
- options:
  - label: "✅ Yes, I have access"
  - label: "❌ No, I don't have access yet"
  - label: "🤔 Not sure, let me check"
- multiSelect: false

### Branch: 🤔 Not sure
Send link: https://replit.com/t/yalo — ask if they can open it or get an error.
- Can open → Branch Yes
- Error → Branch No

### Branch: ❌ No
Ask their full name via AskUserQuestion, then send to #ask-mario via mcp__slack__send_message:
> "Hi Mario! [NAME] needs access to Replit under the Yalo account. Can you add them? Thanks! 🙏"

Tell them: "✅ I let Mario know. While you wait, log in at replit.com with your @yalo.com Google account to set up your profile. Come back once Mario confirms your access."

**Stop here.**

### Branch: ✅ Yes
Ask them to open https://replit.com/t/yalo and confirm workspace via AskUserQuestion:
- question: "What do you see in the top-left of the workspace?"
- options: "🟢 It says 'Yalo'" / "🔴 It says 'Basic plan'"
- If Basic plan → follow Branch No

Continue to Phase 2.

---

## Phase 2 — Project setup

Use AskUserQuestion:
- question: "What project do you want to work with?"
- header: "Your project"
- options:
  - label: "📁 I have an existing local project"
  - label: "🆕 I want to create a new one"
- multiSelect: false

### Branch: 📁 Existing local project
Ask for the path (free text). Run:
```bash
ls <path> && git -C <path> status
```
Confirm the project exists. Note whether it already has git initialized.

### Branch: 🆕 New project

Ask via AskUserQuestion:
- question: "How do you want to start?"
- header: "Starting point"
- options:
  - label: "🚀 Yalo Streamlit template" — description: "Functional app, runs instantly"
  - label: "⚪ From scratch" — description: "Empty directory, you add your own files"

Ask for the project name (free text).

**If template:** Copy files from `templates/python-starter/` (path derived from "Base directory for this skill", go up two levels):
```bash
cp -r <plugin-base>/../../templates/python-starter/. <name>/
```

Run to verify:
```bash
cd <name> && uv run streamlit run app.py
```
Confirm it opens in the browser. Stop with Ctrl+C.

Tell the user: "✅ App running locally."

**If from scratch:** Create empty directory. Add a minimal `pyproject.toml`:
```toml
[project]
name = "<name>"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["streamlit>=1.35.0"]
```
And an `app.py` with `import streamlit as st` and `st.title("My app")`.

> To add dependencies: `uv add <pkg>` — no pip, no freeze needed.

---

## Phase 2b — Build together (iterative)

**You are a companion, not just a pipeline.** Stay with the user and help them build their app until they're satisfied.

Ask via AskUserQuestion:
- question: "What do you want your app to do?"
- header: "Your app"
- options:
  - label: "📊 Dashboard with data" — description: "Charts, metrics, filters — I'll help you connect your data"
  - label: "🤖 AI/LLM tool" — description: "Something powered by an AI model"
  - label: "🛠️ Internal tool" — description: "Forms, workflows, utilities for the team"
  - label: "💡 I have my own idea" — description: "Tell me what you want"

Based on their answer, help them build it:
- Write the `app.py` code for them
- Add dependencies with `uv add <pkg>`
- If they need data (BQ, CSV, API), help them export/connect it
- Run locally with `uv run streamlit run app.py` to preview
- Iterate: ask if they like it, what to change, what to add
- Keep going until they say they're happy

Use AskUserQuestion after each iteration:
- question: "How does it look?"
- header: "Iterate"
- options:
  - label: "✅ Looks great, let's publish"
  - label: "🔧 Change something" — description: "I'll tell you what to tweak"
  - label: "➕ Add more features"

When they choose "Looks great, let's publish" → continue to Phase 3.

---

## Phase 3 — GitHub repo

Check:
```bash
git -C <path> remote -v
```

If no remote:
1. Create repo via mcp__github__create_repository (private: true, name: kebab-case)
2. Push:
```bash
cd <name>
git init
git add .
git commit -m "init"
git remote add origin git@github.com:<user>/<name>.git
git push -u origin main
```

Tell the user: "✅ Code is on GitHub: `github.com/<user>/<name>`"

---

## Phase 4 — Replit CLI

Install if missing:
```bash
which replit || npm install -g replit
```

Tell the user: "I'm opening the Replit login — a browser window will pop up. Just complete the login with your @yalo.com account."

Run it directly:
```bash
replit auth
```

Then ask:

Wait via AskUserQuestion:
- question: "Did you complete the login in the browser?"
- header: "Replit auth"
- options:
  - label: "✅ Done, I'm logged in"
  - label: "⏳ Having trouble"

---

## Phase 5 — Replit config

The template already includes `.replit`. If the user started from scratch, create it:

```toml
run = "uv run streamlit run app.py --server.port 8080 --server.address 0.0.0.0 --server.headless true"
entrypoint = "app.py"

[nix]
channel = "stable-24_05"
packages = ["uv"]

[deployment]
run = ["sh", "-c", "uv run streamlit run app.py --server.port 8080 --server.address 0.0.0.0 --server.headless true"]
deploymentTarget = "autoscale"
```

Push if there are changes:
```bash
git add .replit && git commit -m "Add Replit config" && git push
```

---

## Phase 6 — Create Repl + connect GitHub

**👤 YOUR TURN — 2 steps in the browser (~2 minutes)**

Tell them:

"Two quick things in the Replit browser — this is the last time you'll need to touch the GUI:

**Step 1 — Create the Repl:**
1. Go to https://replit.com/t/yalo
2. Click **'+ Create Repl'**
3. Choose **'Import from GitHub'**
4. Select the repo `<name>`
5. Click **'Import'**

**Step 2 — Enable auto-sync:**
1. Inside the Repl → **Settings**
2. Under **Git** → enable **'Auto-pull on push'**

Come back when you're done."

Wait via AskUserQuestion:
- question: "Did you create the Repl and enable auto-sync?"
- header: "Replit setup"
- options:
  - label: "✅ Done"

---

## Phase 7 — First deploy

**👤 YOUR TURN — First deploy (~1 minute)**

Tell them:

"Last manual step — after this everything is automatic:

1. Inside your Repl → click **'Deploy'** (top right)
2. Choose **'Autoscale'**
3. Click **'Deploy'** → wait for it to finish (~1 min)
4. **Copy the public URL** that appears at the end

Paste the URL here when you have it."

Save the URL to `.replit-url`:
```bash
echo "<URL>" > .replit-url
echo ".replit-url" >> .gitignore
git add .gitignore && git commit -m "Save Replit URL" && git push
```

---

## Closing

Tell them:

"🚀 **You're all set.**

🔗 Your app: `<URL>`

**From now on:**
- Edit `app.py` however you want
- When you're ready to publish → just say **'ready'** or run `/replit-deploy`
- I'll handle the push and give you the updated link

Yalo projects to inspire you:
- 📦 Use case hub: https://yalo-use-case-hub.replit.app
- 📊 Flows KPI: https://yaloFlowsKPIdata.replit.app"

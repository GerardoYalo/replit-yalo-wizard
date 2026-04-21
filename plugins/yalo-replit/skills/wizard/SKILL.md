---
name: wizard
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
cd <name> && uv run streamlit run app.py --server.headless true
```

Tell the user exactly where to go:
"✅ App running locally.

👉 **Open this in your browser:** http://localhost:8501

You should see your Streamlit app. Take a look and come back."

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
- **Data access — always via Looker, never direct BigQuery.** Use the Looker MCP connector (`mcp__looker-mcp-toolbox__*`) for every discovery and query step while building. Do not use `bq`, the `google-cloud-bigquery` SDK, or any direct BigQuery client. Static sources (CSV, external API) are fine.
- Before querying Looker for the first time, run **Phase 2c** to verify the MCP connector and `looker-analytics` skill are installed. Skip 2c for AI/LLM, Internal tool, or custom ideas that don't need Looker data.
- If the app needs Looker data at runtime, ask via AskUserQuestion:
  - question: "Does your dashboard need fresh data every load, or is a snapshot enough?"
  - header: "Data freshness"
  - options:
    - label: "📡 Live — query Looker on each load" — description: "Uses Looker API via looker_sdk; needs credentials in Replit Secrets"
    - label: "📸 Snapshot — freeze current data" — description: "Export once via Looker MCP to a CSV bundled with the app"
  - **Live branch:** run `uv add looker_sdk`. In `app.py`, initialize with `looker_sdk.init40()` reading from env vars (`LOOKERSDK_BASE_URL`, `LOOKERSDK_CLIENT_ID`, `LOOKERSDK_CLIENT_SECRET`, `LOOKERSDK_API_VERSION=4.0`). After deploy, tell the user to set those 4 values in Replit → **Secrets**. Never hardcode credentials.
  - **Snapshot branch:** use `mcp__looker-mcp-toolbox__query_looker` to pull rows, save as `data/<name>.csv` inside the project, and load with `pd.read_csv()` in `app.py`. Document the snapshot date in a comment so the user knows when to refresh.
- Run locally with `uv run streamlit run app.py --server.headless true` and tell the user: "👉 Open http://localhost:8501 in your browser to see the changes."
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

## Phase 2c — Looker access setup (only if the app needs Looker data)

**Skip this phase** unless the user picked "📊 Dashboard with data" in Phase 2b. AI/LLM, Internal tool, and custom ideas without Looker data don't need any of this.

**Goal:** ensure the Looker MCP connector and `looker-analytics` skill are installed in the user's Claude Code so build-time queries + snapshot exports work.

### Step 0 — Check current state (silent)

Run:
```bash
claude mcp list 2>/dev/null | grep looker-mcp-toolbox
test -f "$HOME/.claude/skills/looker-analytics/SKILL.md" && echo "skill_ok" || echo "skill_missing"
```

- If both present and `claude mcp list` shows `✓ Connected` → skip to Phase 3.
- If either missing → continue below.

### Step 1 — Download the two files from the Notion guide

Tell the user:

"To let your dashboard pull data from Looker, you need two files. Both live in this Notion guide — download them now:

👉 https://www.notion.so/yalo/How-to-Set-Up-Looker-Analytics-in-Claude-Cowork-325d53382b23812496b5ef272fb4c26d

1. `looker-mcp-connector.mcpb` — the MCP connector bundle
2. `looker-analytics-<version>.skill` — the governance skill that teaches me how to use Looker well

Save both to `~/Downloads`."

Wait via AskUserQuestion:
- question: "Did you download both files to ~/Downloads?"
- header: "Downloads"
- options:
  - label: "✅ Both downloaded"
  - label: "⏳ Having trouble"

### Step 2 — Looker API credentials

Ask via AskUserQuestion:
- question: "Do you already have Looker API credentials (Client ID + Secret)?"
- header: "Looker creds"
- options:
  - label: "✅ Yes, I have them"
  - label: "❌ No, I need them"

**Branch: ❌ No**
Ask for the user's full name (free text), then send via `mcp__slack__send_message` to `#ask-mario`:
> "Hi Mario! [NAME] needs Looker API credentials for the Claude Code integration. Can you set them up? Thanks! 🙏"

Tell them: "✅ I let Mario know. Come back once you have the Client ID and Secret — then re-invoke the wizard." **Stop here.**

**Branch: ✅ Yes**
Ask for the Client ID and Client Secret (free text, one at a time). Treat as sensitive — don't echo them back in chat output.

### Step 3 — Install the MCP server

Extract the bundle to a stable path:
```bash
mkdir -p ~/.claude/mcp-servers
unzip -o ~/Downloads/looker-mcp-connector.mcpb -d ~/.claude/mcp-servers/looker-mcp-toolbox
```

Register with Claude Code (replace `<CLIENT_ID>` / `<CLIENT_SECRET>` with the user's values — do not print them back):
```bash
claude mcp add looker-mcp-toolbox -s user \
  -e LOOKER_BASE_URL=https://yalochat.looker.com \
  -e LOOKER_CLIENT_ID=<CLIENT_ID> \
  -e LOOKER_CLIENT_SECRET=<CLIENT_SECRET> \
  -e LOOKER_PROJECT=arched-photon-194421 \
  -- node "$HOME/.claude/mcp-servers/looker-mcp-toolbox/server/index.js"
```

Verify:
```bash
claude mcp list | grep looker-mcp-toolbox
```
Expect: `looker-mcp-toolbox: ... ✓ Connected`.

If not connected → credentials are likely wrong. Ask the user to re-check them in the Slack thread from Mario and retry Step 3.

### Step 4 — Install the `looker-analytics` skill

```bash
mkdir -p ~/.claude/skills
unzip -o ~/Downloads/looker-analytics-*.skill -d ~/.claude/skills/
```

Verify:
```bash
test -f "$HOME/.claude/skills/looker-analytics/SKILL.md" && echo "OK" || echo "Missing"
```

### Step 5 — Restart Claude Code

Tell the user:

"🔄 **Restart Claude Code now** — exit this session (Ctrl+C) and run `claude` again. The 15 Looker tools and the `looker-analytics` governance skill only load on startup.

When you're back, say **'continue'** and I'll pick up at the dashboard build in Phase 2b."

**Stop here.** The user must restart before Looker tools become callable. When they return, resume Phase 2b with the live/snapshot question.

---

## Phase 3 — Publish to Replit

Ask via AskUserQuestion:
- question: "Do you have a GitHub account?"
- header: "GitHub"
- options:
  - label: "✅ Yes, I use GitHub"
  - label: "❌ No GitHub account"

### Branch: ✅ Yes — GitHub flow

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

Continue to Phase 4 (Replit CLI).

### Branch: ❌ No GitHub — ZIP flow

Create a zip of the project:
```bash
cd <name> && zip -r ../<name>.zip . -x '.venv/*' '__pycache__/*' '.git/*'
```

Tell the user exactly:
"✅ I created a zip file of your project.

👤 **Upload it to Replit:**
1. Go to **https://replit.com/import**
2. Click **'Upload a .zip file'**
3. Upload the file at: `<absolute-path-to-zip>`
4. Click **'Import'**

Your app will be running on Replit in about a minute."

Wait via AskUserQuestion:
- question: "Did you import the zip on Replit?"
- header: "Replit import"
- options:
  - label: "✅ Done, it's running"
  - label: "⏳ Having trouble"

If done → skip Phase 4, 5, 6. Go directly to Phase 7 (first deploy).

> **Note:** Without GitHub, updates require re-uploading a new zip or copy-pasting changed files. Tell the user: "For future updates, you can drag & drop changed files into the Files pane in Replit, or re-upload a new zip."

---

## Phase 4 — Replit CLI (GitHub flow only)

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

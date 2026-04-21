# 🧙 yalo-replit

A Claude Code plugin that takes any Yalo employee from zero to a live Streamlit app on Replit — access check, GitHub repo, Replit config, deploy pipeline. All in one command.

> 🚀 From local to live in ~5 minutes. The wizard stays with you through the whole build, not just the setup.

## 📦 Install

From inside Claude Code:

```
/plugin marketplace add GerardoYalo/replit-yalo-wizard
/plugin                  # 👉 select and enable yalo-replit
/reload-plugins
```

## 🛠️ Skills

| Command | What it does |
|---------|--------------|
| 🪄 `/yalo-replit:wizard` | End-to-end onboarding — access check, project setup, build-together, GitHub, Replit config, first deploy |
| 🚀 `/yalo-replit:deploy` | Commit + push + tell you to click Redeploy. Triggered by "ready", "deploy", "publish", "ship" |

## 📋 The 7 phases

| # | Phase | Who does it |
|---|-------|-------------|
| 1️⃣ | 🔑 Access check → Slack message to Mario if needed | 🤖 Agent |
| 2️⃣ | 📁 Project setup — template or from scratch | 🤖 Agent |
| 2c | 📊 Looker MCP setup (only for data dashboards) | 🤖 Agent |
| 3️⃣ | 🛠️ Build together — write code, iterate, preview | 🤖 Agent + 🧑 You |
| 4️⃣ | 🐙 GitHub repo (or 📦 ZIP for users without GitHub) | 🤖 Agent |
| 5️⃣ | ⚙️ Replit config injection (`.replit` + `replit.nix`) | 🤖 Agent |
| 6️⃣ | 📥 Import into Replit | 🧑 You (browser) |
| 7️⃣ | 🎬 Click Deploy | 🧑 You (browser) |

🔁 After that, the cycle is: ✏️ edit → 💬 say "ready" → `/yalo-replit:deploy` → 🖱️ click Redeploy → 🌐 live.

## 📊 Data: Looker MCP (not BigQuery)

If your app needs data, the wizard routes through the **Looker MCP connector**, never direct BigQuery:

- ✅ Governed semantic layer — no raw SQL scattered around
- 🔒 No service account keys ending up in a public Repl
- 🎯 One-time credentials setup guided by Phase 2c

📘 Setup instructions live in [Notion](https://www.notion.so/yalo/How-to-Set-Up-Looker-Analytics-in-Claude-Cowork-325d53382b23812496b5ef272fb4c26d).

## 🐍 Template: Python + Streamlit + uv

New projects get a Streamlit starter:
- 📄 `app.py` — minimal functional app
- 📦 `pyproject.toml` — `uv`-managed dependencies (no pip, no requirements.txt)
- ⚙️ `.replit` + `replit.nix` — Replit-native config that works out of the box on Replit's Nix environment (Python 3.11, libstdc++ for numpy/pandas, autoscale deployment)

## 🔀 Two paths to Replit

- 🐙 **With GitHub:** agent creates the repo, pushes, you import from GitHub in Replit. Updates are `git push` + Redeploy.
- 📦 **Without GitHub:** agent packs a ZIP, you upload at `replit.com/import`. Updates are drag & drop.

## 🗂️ Project structure

```
replit-yalo-wizard/
├── .claude-plugin/
│   └── marketplace.json              # 🏪 Marketplace metadata
├── plugins/
│   └── yalo-replit/
│       ├── .claude-plugin/
│       │   └── plugin.json           # 🧩 Plugin metadata
│       ├── skills/
│       │   ├── wizard/SKILL.md       # 🪄 Main onboarding flow
│       │   └── deploy/SKILL.md       # 🚀 Push + redeploy cycle
│       └── templates/
│           └── python-starter/       # 🐍 Streamlit + uv + Replit config
├── slides/                           # 🎞️ AI Friday presentation (Slidev)
├── docs/
└── README.md
```

## 🤝 Contributing

1. ✏️ Edit the skills in `plugins/yalo-replit/skills/*/SKILL.md`
2. 🧪 Edit the starter template in `plugins/yalo-replit/templates/python-starter/`
3. 🔢 Bump the version in both `.claude-plugin/marketplace.json` and `plugins/yalo-replit/.claude-plugin/plugin.json`
4. 🔄 Test locally: `/plugin update yalo-replit && /reload-plugins`

## 🔗 Links

- 🎞️ **AI Friday slides:** `slides/replit-yalo-wizard.pdf`
- 🎫 **Linear ticket:** [YI-3728](https://linear.app/yalo/issue/YI-3728)
- 🌐 **Replit workspace:** https://replit.com/t/yalo
- 💬 **Need access?** Ping Mario in `#ask-mario`

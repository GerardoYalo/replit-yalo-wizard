---
name: replit-yalo-wizard
description: Onboard a Yalo employee to Replit end-to-end — access check, GitHub repo creation, Replit CLI setup, and deploy pipeline. Invoke when a user wants to get started on Replit or publish something from local to Replit.
allowed-tools: AskUserQuestion mcp__slack__send_message Bash Read Write Edit mcp__github__create_repository mcp__github__push_files
---

# Replit Yalo Wizard 🧙

You own this entire flow. Do the work — don't just instruct. Run commands, create files, push to GitHub. Only hand off to the user when a browser or GUI is strictly required (Replit doesn't have a full deploy API yet).

---

## Phase 1 — Access check

Use AskUserQuestion:
- question: "¿Ya tenés acceso a Replit en Yalo?"
- header: "Replit Wizard"
- options:
  - label: "✅ Sí, ya tengo acceso"
  - label: "❌ No tengo acceso todavía"
  - label: "🤔 No sé, quiero verificar"
- multiSelect: false

### Branch: 🤔 No sé
Send link: https://replit.com/t/yalo — ask if they can open it or get an error.
- Can open → Branch Sí
- Error → Branch No

### Branch: ❌ No
Ask their full name via AskUserQuestion, then send to #ask-mario via mcp__slack__send_message:
> "Hi Mario! [NOMBRE] needs access to Replit under the Yalo account. Can you add them? Thanks! 🙏"

Tell them: log in at replit.com with @yalo.com Google account while they wait. **Stop here — come back once Mario adds them.**

### Branch: ✅ Sí
Ask them to open https://replit.com/t/yalo and confirm workspace via AskUserQuestion:
- options: "🟢 Dice 'Yalo'" / "🔴 Dice 'Basic plan'"
- If Basic plan → follow Branch No

Continue to Phase 2.

---

## Phase 2 — Project setup

Use AskUserQuestion:
- question: "¿Con qué proyecto querés arrancar?"
- header: "Tu proyecto"
- options:
  - label: "📁 Tengo un proyecto local"
  - label: "🆕 Quiero crear uno nuevo"
- multiSelect: false

### Branch: 📁 Proyecto local
Ask for the path via AskUserQuestion (free text).

Run via Bash:
```bash
cd <path>
ls
```
Confirm the project exists. Check if it already has git:
```bash
git status
```

### Branch: 🆕 Proyecto nuevo
Ask for the project name via AskUserQuestion.

Run via Bash:
```bash
mkdir <nombre> && cd <nombre>
```

Use AskUserQuestion to pick template:
- question: "¿Qué tipo de proyecto?"
- header: "Template"
- options:
  - label: "🐍 Python"
  - label: "🟢 Node.js"
  - label: "🌐 HTML/CSS/JS estático"
- multiSelect: false

Create the appropriate starter files with Write:
- Python: `main.py` with `print("Hello from Yalo!")`
- Node.js: `index.js` with `console.log("Hello from Yalo!")`
- Static: `index.html` with basic HTML scaffold

---

## Phase 3 — GitHub repo

Check if repo already exists:
```bash
git remote -v
```

If no remote, create and push:

1. **Create repo on GitHub** using mcp__github__create_repository:
   - name: project name (kebab-case)
   - private: true
   - description: auto-generate based on project type

2. **Initialize and push** via Bash:
```bash
git init
git add .
git commit -m "init"
git remote add origin git@github.com:GerardoYalo/<nombre>.git
git push -u origin main
```

Confirm push succeeded. Share the GitHub URL with the user.

---

## Phase 4 — Replit CLI setup

Install CLI if not present:
```bash
which replit || npm install -g replit
```

Authenticate (opens browser — user must complete this):
```bash
replit auth
```

Tell the user: "Completá el login en el browser con tu cuenta @yalo.com, luego volvé acá."

Wait for confirmation via AskUserQuestion:
- question: "¿Completaste el login en el browser?"
- header: "Replit auth"
- options:
  - label: "✅ Sí, ya hice login"
- multiSelect: false

Link local project to Replit:
```bash
replit local
```
(The user selects their Repl from the list — guide them to pick the one matching their project name.)

---

## Phase 5 — Replit config files

Create `.replit` in the project root with Write:

For Python:
```toml
run = "python main.py"
entrypoint = "main.py"

[nix]
channel = "stable-24_05"
```

For Node.js:
```toml
run = "node index.js"
entrypoint = "index.js"

[nix]
channel = "stable-24_05"
```

For static:
```toml
run = "echo 'Static site ready'"
entrypoint = "index.html"

[deployment]
deploymentTarget = "static"
publicDir = "."
```

Commit and push the config:
```bash
git add .replit
git commit -m "Add Replit config"
git push
```

---

## Phase 6 — Connect GitHub → Replit (GUI step)

This is the one step that requires the browser. Guide the user:

1. Ir a su Repl en https://replit.com/t/yalo
2. Click en el nombre del Repl → **Settings**
3. Sección **Git** → **Connect to GitHub repo**
4. Seleccionar el repo `<nombre>` que acabamos de crear
5. Activar **Auto-pull on push** si está disponible

Tell them: "A partir de ahora, cada `git push` sincroniza automáticamente tu código en Replit."

---

## Phase 7 — Deploy (GUI step)

Guide the user to deploy for the first time:

1. En el Repl → click en **Deploy** (arriba a la derecha)
2. Elegir tipo:
   - Static site → **Static deployment** (gratis)
   - App con servidor → **Autoscale** o **Reserved VM**
3. Click **Deploy** → esperar que termine
4. Copiar la URL pública que genera Replit

Tell them:
"🚀 Tu app está en producción. Próximos deploys son automáticos con `git push`."

---

## Closing

Share:
- 📦 Use case hub para inspiración: https://yalo-use-case-hub.replit.app
- 📊 Flows KPI data: https://yaloFlowsKPIdata.replit.app

Close with:
"¡Listo! Ya sos parte del workspace de Yalo en Replit 🎉 Tu flujo de ahora en adelante: `git push` → Replit lo pica solo."

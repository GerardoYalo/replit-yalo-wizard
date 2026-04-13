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

"Hola! Voy a guiarte para publicar tu app en Replit. Acá va el resumen de lo que va a pasar:

**Lo que hago yo automáticamente ✅**
- Verificar tu acceso a Replit
- Crear el proyecto con template Streamlit listo para correr
- Crear el repo en GitHub y pushear el código
- Instalar y configurar el Replit CLI

**Los 3 pasos donde vas a necesitar el browser 👤**
1. Login en Replit (una vez, 30 segundos)
2. Crear el Repl y conectarlo a tu repo de GitHub (una vez, ~2 minutos)
3. Clickear Deploy la primera vez (una vez, ~1 minuto)

**Después de ese setup inicial, el ciclo es 100% automático:**
`git push` → Replit actualiza solo → URL pública lista para compartir

¿Arrancamos?"

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

Tell them: "✅ Le avisé a Mario. Mientras esperás, logueate en replit.com con tu cuenta @yalo.com para preparar tu perfil. Volvé cuando Mario te confirme el acceso."

**Stop here.**

### Branch: ✅ Sí
Ask them to open https://replit.com/t/yalo and confirm workspace via AskUserQuestion:
- question: "¿Qué ves arriba a la izquierda?"
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
Ask for the path (free text). Run:
```bash
ls <path> && git -C <path> status
```
Confirm the project exists. Note whether it already has git initialized.

### Branch: 🆕 Proyecto nuevo

Ask via AskUserQuestion:
- question: "¿Arrancás desde cero o usás el template de Yalo?"
- header: "Punto de partida"
- options:
  - label: "🚀 Template Yalo" — description: "Streamlit app funcional, corre al instante"
  - label: "⚪ Desde cero" — description: "Directorio vacío, vos agregás tus archivos"

Ask for the project name (free text).

**If template:** Copy files from `templates/python-starter/` (path derived from "Base directory for this skill", go up two levels):
```bash
cp -r <plugin-base>/../../templates/python-starter/. <nombre>/
```

Run to verify:
```bash
cd <nombre> && uv run streamlit run app.py
```
Confirm it abre en el browser. Cerrá con Ctrl+C.

Tell the user: "✅ App corriendo local. Editá `app.py` cuando quieras. Cuando estés listo para publicar, decime **'listo'**."

**If desde cero:** Crear directorio vacío. Agregar `pyproject.toml` mínimo:
```toml
[project]
name = "<nombre>"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["streamlit>=1.35.0"]
```
Y un `app.py` con `import streamlit as st` y `st.title("Mi app")`.

> Para agregar dependencias: `uv add <pkg>` — sin pip, sin freeze.

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
cd <nombre>
git init
git add .
git commit -m "init"
git remote add origin git@github.com:<usuario>/<nombre>.git
git push -u origin main
```

Tell the user: "✅ Código en GitHub: `github.com/<usuario>/<nombre>`"

---

## Phase 4 — Replit CLI

Install if missing:
```bash
which replit || npm install -g replit
```

**👤 TURNO DEL USUARIO — Login (30 seg)**

Tell them: "Ahora necesito que hagas login en Replit. Voy a abrir el browser — completá el login con tu cuenta @yalo.com y volvé acá."

```bash
replit auth
```

Wait via AskUserQuestion:
- question: "¿Completaste el login en el browser?"
- header: "Replit auth"
- options:
  - label: "✅ Listo, hice login"

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

**👤 TURNO DEL USUARIO — 2 pasos en el browser (~2 min)**

Tell them:

"Necesito que hagas 2 cosas en el browser de Replit — tarda 2 minutos y es la última vez que vas a tocar la GUI:

**Paso 1 — Crear el Repl:**
1. Ir a https://replit.com/t/yalo
2. Click **'+ Create Repl'**
3. Elegir **'Import from GitHub'**
4. Seleccionar el repo `<nombre>`
5. Click **'Import'**

**Paso 2 — Activar auto-sync:**
1. Dentro del Repl → **Settings**
2. Sección **Git** → activar **'Auto-pull on push'**

Cuando termines, volvé acá."

Wait via AskUserQuestion:
- question: "¿Creaste el Repl y activaste el auto-sync?"
- header: "Setup Replit"
- options:
  - label: "✅ Listo"

---

## Phase 7 — First deploy

**👤 TURNO DEL USUARIO — Deploy inicial (~1 min)**

Tell them:

"Último paso manual — después de esto todo es automático:

1. Dentro de tu Repl → click **'Deploy'** (arriba a la derecha)
2. Elegir **'Autoscale'**
3. Click **'Deploy'** → esperar que termine (~1 min)
4. **Copiar la URL pública** que aparece al final

Pegame la URL cuando la tengas."

Save the URL to `.replit-url`:
```bash
echo "<URL>" > .replit-url
echo ".replit-url" >> .gitignore
git add .gitignore && git commit -m "Save Replit URL" && git push
```

---

## Closing

Tell them:

"🚀 **Todo listo.**

🔗 Tu app: `<URL>`

**De ahora en adelante:**
- Editá `app.py` como quieras
- Cuando estés listo para publicar → decime **'listo'** o usá `/replit-deploy`
- Yo me encargo del `git push` y te devuelvo el link actualizado

Proyectos de Yalo para inspirarte:
- 📦 Use case hub: https://yalo-use-case-hub.replit.app
- 📊 Flows KPI: https://yaloFlowsKPIdata.replit.app"

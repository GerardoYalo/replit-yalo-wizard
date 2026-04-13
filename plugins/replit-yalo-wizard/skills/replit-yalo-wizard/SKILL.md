---
name: replit-yalo-wizard
description: Onboard a Yalo employee to Replit — request access, verify workspace, guide first project
allowed-tools: AskUserQuestion mcp__slack__send_message
---

## Step 1 — Check access status

Use AskUserQuestion with exactly these parameters:

- question: "¿Ya tenés acceso a Replit en Yalo?"
- header: "Replit Yalo Wizard 🧙"
- options:
  - label: "✅ Sí, ya tengo acceso"
  - label: "❌ No tengo acceso todavía"
  - label: "🤔 No sé, quiero verificar"
- multiSelect: false

---

## Branch: 🤔 No sé

Send the user this link to check their access:
👉 https://replit.com/t/yalo

Ask: "¿Podés abrirlo o te tira error?"

- If they can open it → continue as Branch "Sí"
- If they get an error → continue as Branch "No"

---

## Branch: ❌ No

Use AskUserQuestion to ask:
- question: "¿Cuál es tu nombre completo?"
- header: "Pedido de acceso a Replit"

Then send this message to Slack channel **#ask-mario** using mcp__slack__send_message:

> "Hi Mario! [NOMBRE] needs access to Replit under the Yalo account. Can you add them? Thanks! 🙏"

(Replace [NOMBRE] with the name the user provided.)

Confirm to the user:
"✅ Le mandé el mensaje a Mario en #ask-mario. Suele responder el mismo día."

While they wait, tell them:
- Go to replit.com and log in with their @yalo.com Google account to prepare their profile.
- Once Mario adds them, they'll get an email notification.

---

## Branch: ✅ Sí (o confirmó acceso)

1. Ask them to open https://replit.com/t/yalo

2. Use AskUserQuestion to ask:
   - question: "¿Qué ves arriba a la izquierda en el workspace?"
   - header: "Verificando workspace"
   - options:
     - label: "🟢 Dice 'Yalo'"
     - label: "🔴 Dice 'Basic plan' o no veo el equipo"
   - multiSelect: false

   - If "Basic plan" or no team → follow Branch "No" (send Slack message to Mario)
   - If "Yalo" → continue below

3. Guide them to create their first project:
   - Click **"+ Create Repl"**
   - Choose a template (Python recommended for starters)
   - Name it descriptively, e.g. `mi-primer-proyecto`
   - Note: projects marked "Internal to Yalo" are visible only to the Yalo team

4. Share existing Yalo projects for inspiration:
   - 📦 Use case hub: https://yalo-use-case-hub.replit.app
   - 📊 Flows KPI data: https://yaloFlowsKPIdata.replit.app

5. Close with:
   "¡Listo! Ya sos parte del workspace de Yalo en Replit 🎉 Si tenés dudas, podés buscar proyectos del equipo directamente desde el workspace."

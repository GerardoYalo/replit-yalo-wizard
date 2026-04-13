# Context

Build `replit-yalo-wizard` — a Claude Code plugin that onboards any Yalero to Replit automatically. The plugin presents a native dropdown (via `AskUserQuestion`), auto-sends a Slack message to #ask-mario if needed, and guides the user step by step.

This will be demonstrated at an AI Friday session as a live example of what you can build with the Claude Code extension stack. Linear ticket: YI-3728.

**Key insight on stack:** The Python Claude Agent SDK is for building *standalone applications*. For a Claude Code plugin that users invoke with `/replit-yalo-wizard`, the right tool is a **SKILL.md** — which natively supports `AskUserQuestion` (dropdown) and MCP tools (Slack). No Python runtime needed.

---

## Project location

`/Users/gerardo-yalo/replit-yalo-wizard/`

---

## Final file structure

```
replit-yalo-wizard/
├── .claude-plugin/
│   └── plugin.json          ← plugin metadata + Slack MCP config
├── skills/
│   └── replit-yalo-wizard/
│       └── SKILL.md         ← main skill: dropdown + branching + Slack
└── README.md
```

---

## File 1: `.claude-plugin/plugin.json`

Plugin metadata and MCP server declaration (Slack):

```json
{
  "name": "replit-yalo-wizard",
  "description": "Onboard any Yalo employee to Replit — handles access request automatically",
  "version": "1.0.0",
  "mcpServers": {
    "slack": {
      "type": "http",
      "url": "https://mcp.slack.com/mcp"
    }
  }
}
```

---

## File 2: `skills/replit-yalo-wizard/SKILL.md`

```markdown
---
name: replit-yalo-wizard
description: Onboard a Yalo employee to Replit — request access, verify workspace, guide first project
allowed-tools: AskUserQuestion mcp__slack__send_message
---

## Step 1 — Check access status

Use AskUserQuestion with exactly these options:

question: "¿Ya tenés acceso a Replit en Yalo?"
header: "Replit Yalo Wizard 🧙"
options:
  - label: "✅ Sí, ya tengo acceso"
  - label: "❌ No tengo acceso todavía"
  - label: "🤔 No sé, quiero verificar"
multiSelect: false

---

## Branch: No sé

Send the user this link to check:
👉 https://replit.com/t/yalo

Ask: "¿Podés abrirlo o te tira error?"
- Puede abrirlo → seguir como branch "Sí"
- Le tira error → seguir como branch "No"

---

## Branch: No

Use AskUserQuestion to ask:
question: "¿Cuál es tu nombre completo?"
header: "Pedido de acceso"

Then send this message to Slack channel #ask-mario using mcp__slack__send_message:
"Hi Mario! [NOMBRE] needs access to Replit under the Yalo account. Can you add them? Thanks! 🙏"

Confirm to the user: "✅ Le mandé el mensaje a Mario en #ask-mario. Suele responder el mismo día."

Tell them: While they wait, they can go to replit.com and log in with their @yalo.com Google account to prepare their profile.

---

## Branch: Sí (o confirmó acceso)

1. Ask them to go to https://replit.com/t/yalo
2. Ask: "¿Arriba a la izquierda dice 'Yalo' o 'Basic plan'?"
   - Basic plan → mandar mensaje a Mario igual (seguir branch "No")
   - Yalo → continuar

3. Guide them to create their first project:
   - Click "+ Create Repl"
   - Choose a template (Python recommended for starters)
   - Name it descriptively (e.g., `mi-primer-proyecto`)
   - Explain: projects marked "Internal to Yalo" are visible only to the Yalo team

4. Share existing Yalo projects for inspiration:
   - 📦 Use case hub: https://yalo-use-case-hub.replit.app
   - 📊 Flows KPI data: https://yaloFlowsKPIdata.replit.app

5. Close with: "¡Listo! Ya sos parte del workspace de Yalo en Replit 🎉"
```

---

## File 3: `README.md`

Documents the plugin: what it does, how to install it, how to contribute.

---

## Distribution (future step — not in scope now)

To publish to `yalochat/claude-plugins` marketplace:

```
yalochat/claude-plugins/
├── .claude-plugin/
│   └── marketplace.json     ← lists replit-yalo-wizard
└── plugins/
    └── replit-yalo-wizard/  ← copy of this repo
```

User install commands (one time):
```bash
/plugin marketplace add yalochat/claude-plugins
/plugin install replit-yalo-wizard@yalo-plugins
```

---

## Build order

1. Create `.claude-plugin/plugin.json`
2. Create `skills/replit-yalo-wizard/SKILL.md`
3. Create `README.md`
4. Test locally: install plugin in Claude Code, run `/replit-yalo-wizard`
5. Verify dropdown appears, Slack message sends, branching works

---

## Verification

- Run `/replit-yalo-wizard` in Claude Code
- Option 1 (Sí): verify it guides to workspace + first project
- Option 2 (No): verify Slack message goes to #ask-mario with correct name
- Option 3 (No sé): verify link is sent + branches correctly after user response
- Confirm Slack MCP sends the real message (check #ask-mario)

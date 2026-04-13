# replit-yalo-wizard

A Claude Code plugin that onboards any Yalo employee to Replit automatically.

## What it does

Invoke `/replit-yalo-wizard` in Claude Code and it will:

1. Show a **native dropdown** asking if you already have Replit access
2. Based on your answer, it will:
   - **✅ Already have access** — verify you're in the Yalo workspace, then guide you to create your first project
   - **❌ No access yet** — ask your name and automatically send a message to Mario in `#ask-mario` on Slack
   - **🤔 Not sure** — send you the workspace link and branch based on what you find

## Installation

From inside your Claude Code session, run:

```bash
/plugin install /path/to/replit-yalo-wizard
```

Or if published to the marketplace:

```bash
/plugin marketplace add yalochat/claude-plugins
/plugin install replit-yalo-wizard@yalo-plugins
```

## Usage

```
/replit-yalo-wizard
```

That's it. The wizard handles everything from there.

## Requirements

- Claude Code with the Slack MCP server configured (included in `plugin.json`)
- Slack authentication to send messages to `#ask-mario`

## Project structure

```
replit-yalo-wizard/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata + Slack MCP config
├── skills/
│   └── replit-yalo-wizard/
│       └── SKILL.md         # Main skill: dropdown + branching + Slack
└── README.md
```

## Contributing

1. Edit `skills/replit-yalo-wizard/SKILL.md` to change wizard behavior
2. Edit `.claude-plugin/plugin.json` to add/modify MCP servers
3. Test locally with `/replit-yalo-wizard` in Claude Code

## Ticket

Linear: YI-3728

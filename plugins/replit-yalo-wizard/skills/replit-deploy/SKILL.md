---
name: replit-deploy
description: Deploy the current project to Replit and return the live URL. Invoke when the user says they are ready to publish, share, or deploy to Replit (e.g. "ready", "deploy", "publish", "ship", "listo", "publicar").
allowed-tools: Bash Read AskUserQuestion
---

# replit-deploy

The user is ready to publish. Take ownership — push, wait for Replit to sync, and return the live URL.

## Steps

1. **Check there's something to push:**
```bash
git status
git diff --stat HEAD
```

If nothing new to commit, skip to step 3.

2. **Commit and push** (always pull first — Replit may have pushed config changes):
```bash
git add .
git commit -m "deploy: ready to share"
git pull --rebase origin main
git push
```

Confirm push succeeded.

3. **Get the Replit URL:**

```bash
cat .replit-url 2>/dev/null || echo "NOT_SET"
```

If the file exists, use that URL.

If NOT_SET, ask via AskUserQuestion:
- question: "What's your Replit app URL? You can find it in the browser bar when you open your Repl."
- header: "Replit URL"

Save it for next time:
```bash
echo "<URL>" > .replit-url
echo ".replit-url" >> .gitignore
```

4. **Tell the user to redeploy:**

Tell the user:
"✅ **Code pushed.** Replit has the latest version in your workspace.

👤 **One last click** — go to your Repl → click **'Redeploy'** (top right) to update the live app.

🔗 Your app: `<URL>`"

Wait via AskUserQuestion:
- question: "Did you click Redeploy?"
- header: "Redeploy"
- options:
  - label: "✅ Done, app is updated"
  - label: "⏳ Having trouble"

If done, tell them:
"🚀 **Live and updated.** Share the link with anyone."

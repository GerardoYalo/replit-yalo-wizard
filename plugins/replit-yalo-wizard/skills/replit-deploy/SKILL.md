---
name: replit-deploy
description: Deploy the current project to Replit and return the live URL. Invoke when the user says they are ready to publish, share, or deploy to Replit (e.g. "listo", "publicar", "deployar", "subir a Replit").
allowed-tools: Bash Read
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

2. **Commit and push:**
```bash
git add .
git commit -m "deploy: ready to share"
git push
```

Confirm push succeeded.

3. **Get the Replit URL:**

Run:
```bash
cat .replit-url 2>/dev/null || echo "NOT_SET"
```

If the file exists, read the URL from it and show it to the user.

If NOT_SET, ask via AskUserQuestion:
- question: "¿Cuál es la URL de tu Repl? La encontrás en la barra del browser cuando abrís tu Repl."
- header: "URL de Replit"

Save it for next time:
```bash
echo "<URL>" > .replit-url
echo ".replit-url" >> .gitignore
```

4. **Confirm deploy:**

Tell the user:
"🚀 **Tu app está publicada.**

🔗 **[Abrir app](<URL>)**

Replit autopull el último push — en ~30 segundos debería estar actualizada. Compartí ese link con quien quieras."

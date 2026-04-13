const express = require("express");
const app = express();
const port = process.env.PORT || 8080;

app.get("/", (req, res) => {
  res.send(`
    <html>
      <head><title>Yalo on Replit 🚀</title></head>
      <body style="font-family:sans-serif;max-width:600px;margin:60px auto;text-align:center">
        <h1>🚀 Yalo on Replit</h1>
        <p>Tu app está viva y funcionando.</p>
        <p><a href="/health">Ver health check →</a></p>
      </body>
    </html>
  `);
});

app.get("/health", (req, res) => {
  res.json({ status: "ok", team: "Yalo" });
});

app.listen(port, () => console.log(`Running on port ${port}`));

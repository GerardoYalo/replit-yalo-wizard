from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head><title>Yalo on Replit 🚀</title></head>
      <body style="font-family:sans-serif;max-width:600px;margin:60px auto;text-align:center">
        <h1>🚀 Yalo on Replit</h1>
        <p>Tu app está viva y funcionando.</p>
        <p><a href="/health">Ver health check →</a></p>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "ok", "team": "Yalo"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

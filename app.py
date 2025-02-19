from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Simple Flask App</title>
        </head>
        <body>
            <h1>Welcome to Your Simple Flask App!</h1>
            <p>This is a basic Flask application deployed on Vercel.</p>
        </body>
        </html>
    """)

if __name__ == "__main__":
    # For local testing only. Vercel will use the app instance directly.
    app.run(host="0.0.0.0", port=5000, debug=True)

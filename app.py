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
            <h1>ITS ME YA BOY CYAN</h1>
            <p>VERCEL SCENES.</p>
        </body>
        </html>
    """)

if __name__ == "__main__":
    # For local testing only. Vercel will use the app instance directly.
    app.run(host="0.0.0.0", port=5000, debug=True)

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
            <h1>ITS ME YA BOY CYAN/ Ahmed Shayan Arsalan 21i1690</h1>
            <p>VERCEL SCENES!!!.</p>
        </body>
        </html>
    """)

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)

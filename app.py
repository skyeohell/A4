from flask import Flask, render_template, request
from dream_ai import analyze_dream, generate_dream_image
import base64

app = Flask(__name__)


# ---------- HOME PAGE ----------
@app.route("/")
def home():
    return render_template("index.html")


# ---------- PROCESS DREAM ----------
@app.route("/interpret", methods=["POST"])
def interpret():

    dream = request.form["dream"]

    if not dream.strip():
        return render_template("index.html", error="Please enter a dream.")

    try:
        interpretation = analyze_dream(dream)
        image_bytes = generate_dream_image(dream)

        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        return render_template(
            "result.html",
            dream=dream,
            interpretation=interpretation,
            image=image_base64
        )

    except Exception as e:
        return render_template("index.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True)
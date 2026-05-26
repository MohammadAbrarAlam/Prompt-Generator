from flask import Flask, render_template, request
from crews import run_prompt_generator
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    style = request.form.get("style")
    media_type = request.form.get("media_type")

    file = request.files["file"]

    if file and file.filename:
        # Create uploads folder if it doesn't exist
        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
        
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        description = f"{media_type} uploaded by user named {file.filename}"

        prompt = run_prompt_generator(description, style)

        return render_template(
            "index.html",
            generated_prompt=prompt
        )

    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
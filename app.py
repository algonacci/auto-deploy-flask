import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Auto deploy Flask"

if __name__ == "__main__":
    app.run(
          port=int(os.environ.get("PORT", 8005))
    )
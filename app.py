import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "status" : {
            "message": "Deployed with Gunicorn",
            "code": 200,
        },
        "data": None,
    })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 7001)),
    )
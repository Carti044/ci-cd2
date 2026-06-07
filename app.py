from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify(message="Hello, DevOps!")


@app.route("/health")
def health():
    # Эндпоинт для healthcheck — пригодится позже в Kubernetes (liveness/readiness)
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    # host=0.0.0.0 обязателен внутри контейнера, иначе порт не виден снаружи
    app.run(host="0.0.0.0", port=8080)

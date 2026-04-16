from flask import Flask, jsonify, request
from flask_migrate import Migrate
from config import Config
from models import db, Bird

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def home():
    return {"message": "Flask + PostgreSQL running"}


@app.route("/birds", methods=["POST"])
def create_bird():
    data = request.get_json()

    bird = Bird(name=data["name"], species=data["species"])
    db.session.add(bird)
    db.session.commit()

    return jsonify(bird.to_dict()), 201


@app.route("/birds", methods=["GET"])
def get_birds():
    birds = Bird.query.all()
    return jsonify([b.to_dict() for b in birds])


@app.route("/birds/<int:id>", methods=["GET"])
def get_bird(id):
    bird = Bird.query.get_or_404(id)
    return jsonify(bird.to_dict())


@app.route("/birds/<int:id>", methods=["DELETE"])
def delete_bird(id):
    bird = Bird.query.get_or_404(id)
    db.session.delete(bird)
    db.session.commit()
    return {"message": "deleted"}


if __name__ == "__main__":
    app.run(debug=True)

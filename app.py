import os
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError

from db import db
from ma import ma
from blocklist import BLOCKLIST


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app.secret_key = os.environ.get("APP_SECRET_KEY")
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400

jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload):
    return jwt_payload["jti"] in BLOCKLIST



if __name__ == "__main__":
    db.init_app(app)
    ma.inti_app(app)
    app.run(port=5000, debug=True)
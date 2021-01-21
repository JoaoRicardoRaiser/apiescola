from flask import Flask, jsonify, request

from data.models.gabarito_model import GabaritoModel
from services.gabarito_service import persistir_gabarito

app = Flask(__name__)


@app.route('/gabarito', methods=["POST"])
def hello_world():
    data = request.json
    gabarito_model = GabaritoModel(**data)
    persistir_gabarito(gabarito_model)
    return jsonify("deu boa"), 200

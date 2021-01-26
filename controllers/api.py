import json

from flask import Flask, jsonify, request

from data.models.gabarito_model import GabaritoModel
from data.models.resposta_model import RespostaModel
from services.buscar_notas_alunos_service import buscar_notas_alunos
from services.gabarito_service import persistir_gabarito
from services.resposta_service import persistir_resposta

app = Flask(__name__)


@app.route('/gabarito', methods=["POST"])
def hello_world():
    data = request.json
    gabarito_model = GabaritoModel(**data)
    persistir_gabarito(gabarito_model)
    return jsonify("deu boa"), 200


@app.route('/resposta', methods=["POST"])
def tratar_resposta():
    data = request.json
    resposta_model = RespostaModel(**data)
    persistir_resposta(resposta_model)
    return jsonify("A persistencia dos dados foram efetuados com sucesso")

@app.route('/notas', methods=["GET"])
def tratar_notas():
    notas_alunos = buscar_notas_alunos()
    resposta = json.dumps([nota.__dict__ for nota in notas_alunos])
    return jsonify(json.loads(resposta))

import json

from flask import Flask, jsonify, request

from data.models.gabarito_model import GabaritoModel
from data.models.resposta_model import RespostaModel
from services.buscar_notas_alunos_service import buscar_notas_alunos
from services.gabarito_service import persistir_gabarito
from services.resposta_service import persistir_resposta
from services.transformar_notas_em_resultado import transformar_notas_em_resultado

app = Flask(__name__)


@app.route('/gabarito', methods=["POST"])
def tratar_gabarito():
    try:
        data = request.json
        gabarito_model = GabaritoModel(**data)
        persistir_gabarito(gabarito_model)
        return jsonify("A persistência do gabarito foi realizada com sucesso!"), 200
    except Exception as exception:
        return jsonify(f"Um erro inesperado ocorreu: {exception}"), 400


@app.route('/resposta', methods=["POST"])
def tratar_resposta():
    try:
        data = request.json
        resposta_model = RespostaModel(**data)
        persistir_resposta(resposta_model)
        return jsonify("A persistência da resposta foi realizada com sucesso!"), 200
    except Exception as exception:
        return jsonify(f"Um erro inesperado ocorreu: {exception}"), 400


@app.route('/notas', methods=["GET"])
def tratar_notas():
    try:
        notas_alunos = buscar_notas_alunos()
        resposta = json.dumps([nota.__dict__ for nota in notas_alunos])
        return jsonify(json.loads(resposta)), 200
    except Exception as exception:
        return jsonify(f"Um erro inesperado ocorreu: {exception}"), 400


@app.route('/aprovados', methods=["GET"])
def tratar_aprovados():
    try:
        aprovados = transformar_notas_em_resultado()
        resposta = json.dumps([aprovado.__dict__ for aprovado in aprovados])
        return jsonify(json.loads(resposta)), 200
    except Exception as exception:
        return jsonify(f"Um erro inesperado ocorreu: {exception}"), 400

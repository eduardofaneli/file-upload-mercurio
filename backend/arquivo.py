from flask import jsonify, request
from arquivo_dao import ArquivoDao
from session import User, check_authorization


class Arquivo(object):
    def __init__(self):
        self.dao = ArquivoDao()


    @check_authorization
    def detalhes(self, id):
        try:
            arquivo = self.dao.obter(id)
        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': "File not found"}), 500
        else:
            return jsonify({'success': True, 'arquivo': arquivo}), 200


    @check_authorization
    def recente(self):
        try:
            arquivos = self.dao.listar()
        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': "Error listing"}), 500
        else:
            return jsonify({'success': True, 'arquivos': arquivos}), 200


    @check_authorization
    def pesquisa(self, texto):
        try:
            arquivos = self.dao.listar()
        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': "Error listing"}), 404
        else:
            return jsonify({'success': True, 'arquivos': arquivos}), 200
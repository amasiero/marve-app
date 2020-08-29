class Heroi(object):

    def __init__(self, imagem, nome, descricao):
        self._imagem = imagem
        self._nome = nome
        self._descricao = descricao

    def get_imagem(self):
        return self._imagem

    def get_nome(self):
        return self._nome
    
    def get_descricao(self):
        return self._descricao

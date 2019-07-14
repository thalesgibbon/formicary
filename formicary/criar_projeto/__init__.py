import os
from formicary.__config__ import path_formiga, path_formiga_cortadora,\
    path_formiga_transportadora, path_formiga_cultivadora, path_produto, path_produto_cortadora,\
    path_produto_transportadora, path_produto_cultivadora


class criar_projeto():
    def __init__(self):
        self.criar_pastas()

    def criar_pastas(self):
        pastas = [
            path_formiga,
            path_formiga_cortadora,
            path_formiga_transportadora,
            path_formiga_cultivadora,
            path_produto,
            path_produto_cortadora,
            path_produto_transportadora,
            path_produto_cultivadora,
        ]

        for diretorio in pastas:
            if not os.path.exists(diretorio):
                os.makedirs(diretorio)


criar_projeto()

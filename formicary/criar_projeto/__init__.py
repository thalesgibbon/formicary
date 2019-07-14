import os


class criar_projeto():
    def __init__(self):
        self.criar_pastas()

    def criar_pastas(self):
        path = os.getcwd()
        path_formiga = os.path.join(path, "formiga")
        path_formiga_cortadora = os.path.join(path_formiga, "cortadora")
        path_formiga_transportadora = os.path.join(path_formiga, "transportadora")
        path_formiga_cultivadora = os.path.join(path_formiga, "cultivadora")

        path_produto = os.path.join(path, "produto")
        path_produto_cortadora = os.path.join(path_produto, "cortadora")
        path_produto_transportadora = os.path.join(path_produto, "transportadora")
        path_produto_cultivadora = os.path.join(path_produto, "cultivadora")

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

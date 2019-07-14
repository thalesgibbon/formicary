"""
    CONFIGURACOES PADRAO
"""
import os


path = os.getcwd()

path_formiga = os.path.join(path, "formiga")
path_formiga_cortadora = os.path.join(path_formiga, "cortadora")
path_formiga_transportadora = os.path.join(path_formiga, "transportadora")
path_formiga_cultivadora = os.path.join(path_formiga, "cultivadora")

path_produto = os.path.join(path, "produto")
path_produto_cortadora = os.path.join(path_produto, "cortadora")
path_produto_transportadora = os.path.join(path_produto, "transportadora")
path_produto_cultivadora = os.path.join(path_produto, "cultivadora")
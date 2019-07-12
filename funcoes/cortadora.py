"""
    FORMIGA CORTADORA

    funcoes principal de cortar os alimentos ou vegetais maiores para o transporte ate o formigueiro
    figura de exemplo que faz a extracao dos dados para os transformadores
"""
import __config__ as config
import pandas as pd
import os
from datetime import date


class cortadora(object):
    def __init__(self):
        self.type = 'U'
        self.sql = None
        self.conexao = None
        self.nome_arquivo = self.__class__.__name__
        self.save_log = False
        self.data_arquivo = date.today().strftime('%Y%m%d')
        self.diretorio_arquivo = os.path.join(config.path_dados, f"{self.nome_arquivo}.pkl")

    def executar(self):
        if self.sql and self.conexao:
            objeto = pd.read_sql(self.sql, self.conexao)
            self.salvar(objeto)
        else:
            print('as variaveis sql e conexao precisam ser preenchidas')

    def abrir(self):
        if self.type == 'U':
            return pd.read_pickle(self.diretorio_arquivo)

    def salvar(self, _objeto, _force=False):
        if self.type == 'U':
            if len(_objeto) > 0 or _force:
                _objeto.to_pickle(self.diretorio_arquivo)
            else:
                print(f'objeto vazio, nao salvo')

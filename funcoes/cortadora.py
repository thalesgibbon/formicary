"""
    FORMIGA CORTADORA

    funcoes principal de cortar os alimentos ou vegetais maiores para o transporte ate o formigueiro
    figura de exemplo que faz a extracao dos dados para os transformadores
"""
import __config__ as config
import pandas as pd
import os
import importlib
from datetime import date, timedelta, datetime
from subprocess import call


class cortadora(object):

    def __init__(self):
        self.type = 'U'
        self.sql = None
        self.conexao = None
        self.nome_arquivo_h5 = self.__class__.__name__
        self.save_log = True
        self.data_arquivo = date.today().strftime('%Y%m%d')

    def executar(self):

        # identifica perioticidade do arquivo
        if self.type == 'D':

            start_date = date(int(self.data_arquivo[:4]), int(self.data_arquivo[4:6]), int(self.data_arquivo[6:8]))
            end_date = (start_date + timedelta(days=1)).strftime('%Y-%m-%d')
            start_date = start_date.strftime('%Y-%m-%d')
            anomesdia_arquivo = '_' + self.data_arquivo

            duas_string = (start_date, end_date)
            tres_string = (nome_do_banco_SQL, start_date, end_date)
            quatro_string = (nome_do_banco_SQL, nome_do_banco_SQL, start_date, end_date)
            lista_string = (None, duas_string, tres_string, quatro_string)
            indice = self.sql.count('{}') - 1
            pick = lista_string[indice]
            new_sql = self.sql.format(*pick)

        else:
            anomesdia_arquivo = ''
            uma_string = (nome_do_banco_SQL,)
            duas_string = (nome_do_banco_SQL, nome_do_banco_SQL)
            lista_string = (uma_string, duas_string)
            indice = self.sql.count('{}') - 1
            pick = lista_string[indice]
            new_sql = self.sql.format(*pick)

        odbc = config.conexao_via_sistema(self.sistema_id)
        objeto = pd.read_sql(new_sql, odbc)
        self.save(objeto, nome_do_banco, anomesdia_arquivo)
        if self.save_log:
            config.salvar_log(etapa=1,
                              text=f'Finalizado... sistema: {self.sistema_id}, script: {self.__class__.__name__}')
        odbc.close()

    def abrir(self):
        if self.type == 'U':
            return pd.read_pickle(os.path.join(config.path_dados, f"{self.__class__.__name__}.pkl"))
        else:
            return pd.read_pickle(os.path.join(config.path_dados, f"{self.__class__.__name__}_{self.data_arquivo}.pkl"))

    def import_from_server(self, flag_salvar=0):
        if config.ip_local == config.ip_server:
            print('você esta no servidor, nao eh possivel realizar esta operacao')
        else:
            if flag_salvar == 1:
                if self.type == 'U':
                    dados = pd.read_pickle(f"{config.path_read_extract}\{config.lista_sistemas_full[self.sistema_id][2]}.{self.__class__.__name__}.pkl")
                    dados.to_pickle(f"{config.path_data_extract}\{config.lista_sistemas_full[self.sistema_id][2]}.{self.__class__.__name__}.pkl")
                    return dados
                else:
                    dados = pd.read_pickle(f"{config.path_read_extract}\{config.lista_sistemas_full[self.sistema_id][2]}.{self.__class__.__name__}_{self.data_arquivo}.pkl")
                    dados.to_pickle(f"{config.path_data_extract}\{config.lista_sistemas_full[self.sistema_id][2]}.{self.__class__.__name__}_{self.data_arquivo}.pkl")
                    return dados
            else:
                if self.type == 'U':
                    return pd.read_pickle(
                        f"{config.path_read_extract}\{config.lista_sistemas_full[self.sistema_id][2]}.{self.__class__.__name__}.pkl")
                else:
                    return pd.read_pickle(
                        f"{config.path_read_extract}\{config.lista_sistemas_full[self.sistema_id][2]}.{self.__class__.__name__}_{self.data_arquivo}.pkl")

    def extract_file_dependencies(self):
        pass

    def extract_file_libraries(self):
        pass

    def edit(self):
        prog = r"C:\Program Files\JetBrains\PyCharm Community Edition 2017.3.3\bin\pycharm64.exe"
        call([prog, f"{config.path_script_extract}\{config.lista_sistemas_full[self.sistema_id][2]}\{self.__class__.__name__}.py"])

    def save(self, objeto2, nome_do_banco2, anomesdia_arquivo2):
        if self.type == 'U':
            if len(objeto2) > 0:
                objeto2.to_pickle(
                    f"{config.path_data_extract}\{nome_do_banco2}.{self.nome_arquivo_h5}{anomesdia_arquivo2}.pkl")
                del objeto2
            else:
                print(f'tabela "{self.nome_arquivo_h5}" vazia, nao atualizada')
        else:
            objeto2.to_pickle(
                f"{config.path_data_extract}\{nome_do_banco2}.{self.nome_arquivo_h5}{anomesdia_arquivo2}.pkl")
            del objeto2

    def analisa_arquivos_diarios(self):
        TOTAL = pd.DataFrame()
        for data in config.range_date(config.d30(), config.d1()):
            for keys in extratores_diarios:
                for values in extratores_diarios[keys]:
                    name = f"{config.lista_sistemas_full[keys][2]}.{values}_{data}"
                    file = f"{config.path_data_extract}\{name}.pkl"
                    data_formatada = '{}-{}-{}'.format(str(data)[:4], str(data)[4:6], str(data)[6:8])
                    TOTAL = pd.concat([TOTAL,
                                       pd.DataFrame([[len(pd.read_pickle(file)), name, pd.to_datetime(data_formatada)]],
                                                    columns=['rows', 'name', 'data'])])
        TOTAL['data'] = TOTAL['data'].values.astype('datetime64[D]')
        TOTAL = TOTAL.reset_index(drop=True)
        TOTAL['domingo'] = TOTAL.data.apply(lambda x: True if datetime.weekday(x) == 6 else False)
        TOTAL = TOTAL.sort_values(['data', 'rows'], ascending=True)
        TOTAL.to_pickle(rf"{config.path_data_system}\rows_for_files.pkl")


sistemas = {}

for root, dirs, files in os.walk(config.path_script_extract):
    if '__pycache__' in root or root == config.path_script_extract:
        pass
    else:
        if files:
            sistemas[root[len(config.path_script_extract) + 1:]] = files

for sistema_desc in sistemas.keys():
    for nome_arquivo in sistemas[sistema_desc]:
        nome_arquivo = nome_arquivo[:-3]
        globals()[f'{sistema_desc}_{nome_arquivo}'] = getattr(
            importlib.import_module(f'script.extract.{sistema_desc}.{nome_arquivo}'), nome_arquivo)

print('Biblioteca de extratores importada!')

if config.ip_local != config.ip_server:
    print(
        '\n \n A extração local não é permitida para o COB. Para os demais sistemas, instalar o SQL Server, o MySQL e os conectores necessários.\n\n')
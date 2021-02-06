import pymysql
from PyQt5.QtCore import QDate

from configBD import ConfigDB
from modelos.eventoModel import EventoModelo


class DaoEvento:

    def __init__(self, db):
        self.db = db
        self.configs = ConfigDB()
        
        # self.configs = ConfigDB()
        # 
        # self.db = pymysql.connect(
        #     host=self.configs.host,
        #     user=self.configs.user,
        #     passwd=self.configs.passwd,
        #     db=self.configs.banco,
        #     port=self.configs.port
        # )

    def insereEvento(self, evento: EventoModelo):

        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            INSERT INTO {self.configs.tblEvento}
            (
                titulo, detalhe, grupoId, dataEvento, dataCadastro, horaInicio, horaFim, diaInteiro
            )
            VALUES
            (
                '{evento.titulo}', '{evento.detalhe}', {evento.grupoId}, '{evento.dataEvento}', NOW(), '{evento.horaInicio}', '{evento.horaFim}', {evento.diaInteiro}
            )
            """

        try:
            cursor.execute(strComando)
            self.db.commit()
        except:
            raise Warning(f'Erro SQL - insereGrupo({evento.titulo}) <INSERT>')
        finally:
            eventoId = cursor.lastrowid
            self.disconectBD(cursor)
            return eventoId


    def findAll(self):

        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""SELECT eventoId, titulo, detalhe, grupoId, 
        dataEvento, horaInicio, horaFim, diaInteiro, dataCadastro FROM {self.configs.tblEvento};"""

        try:
            cursor.execute(strComando)
            return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - findAll({self.configs.tblEvento}) <INSERT>')
        finally:
            self.disconectBD(cursor)

    def findAllDataSelecionada(self, dataEvento):

        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""SELECT eventoId, titulo, detalhe, grupoId, 
         dataEvento, horaInicio, horaFim, diaInteiro, dataCadastro FROM {self.configs.tblEvento} WHERE dataEvento = '{dataEvento}';"""

        try:
            cursor.execute(strComando)
            return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - findAll({self.configs.tblEvento}) <INSERT>')
        finally:
            self.disconectBD(cursor)

    def buscaDatasEventos(self):
        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""SELECT eventoId, dataEvento FROM {self.configs.tblEvento}"""

        try:
            cursor.execute(strComando)
            return dict(cursor.fetchall())
        except:
            raise Warning(f'Erro SQL - buscaDatasEventos({self.configs.tblEvento}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def buscaPorId(self, idEvento=int):
        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""SELECT * FROM {self.configs.tblEvento} WHERE eventoId = {idEvento}"""

        try:
            cursor.execute(strComando)
            return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - buscaDatasEventos({self.configs.tblEvento}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def excluirEvento(self):
        pass

    def disconectBD(self, cursor):
        cursor.close()
        self.db.close()

import pymysql
from PyQt5.QtCore import QDate

from configBD import ConfigDB
from modelos.eventoModel import EventoModelo


class DaoEvento:

    def __init__(self):
        self.configs = ConfigDB()

        self.connection = pymysql.connect(
            host=self.configs.host,
            user=self.configs.user,
            passwd=self.configs.passwd,
            db=self.configs.banco
        )

    def insereEvento(self, evento: EventoModelo):

        self.connection.connect()
        cursor = self.connection.cursor()

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
            print(strComando)
            cursor.execute(strComando)
            self.connection.commit()
        except:
            raise Warning(f'Erro SQL - insereGrupo({evento.titulo}) <INSERT>')
        finally:
            eventoId = cursor.lastrowid
            self.disconectBD(cursor)
            return eventoId


    def findAll(self):

        self.connection.connect()
        cursor = self.connection.cursor()

        strComando = f"""SELECT eventoId, titulo, detalhe, grupoId, 
        dataEvento, horaInicio, horaFim, diaInteiro, dataCadastro FROM {self.configs.tblEvento};"""

        try:
            cursor.execute(strComando)
            return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - findAll({self.configs.tblEvento}) <INSERT>')
        finally:
            self.disconectBD(cursor)

    def buscaDatasEventos(self):
        self.connection.connect()
        cursor = self.connection.cursor()

        strComando = f"""SELECT eventoId, dataEvento FROM {self.configs.tblEvento}"""

        try:
            cursor.execute(strComando)
            return dict(cursor.fetchall())
        except:
            raise Warning(f'Erro SQL - buscaDatasEventos({self.configs.tblEvento}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def buscaPorId(self, idEvento=int):
        self.connection.connect()
        cursor = self.connection.cursor()

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
        self.connection.close()

import pymysql

from configBD import ConfigDB
from modelos.grupoModel import GrupoModelo


class DaoGrupo():

    def __init__(self):
        self.configs = ConfigDB()

        self.connection = pymysql.connect(
            host=self.configs.host,
            user=self.configs.user,
            passwd=self.configs.passwd,
            db=self.configs.banco
        )

    def insereGrupo(self, grupo: GrupoModelo):

        self.connection.connect()
        cursor = self.connection.cursor()

        strComando = f"""
            INSERT INTO {self.configs.tblGrupo}
            (
                titulo, descricao, dataCadastro, dataUltAlt
            )
            VALUES
            (
                '{grupo.titulo}', '{grupo.descricao}', NOW(), NOW()
            )
            """
        try:
            cursor.execute(strComando)
            self.connection.commit()
            cursor.close()
        except:
            raise Warning(f'Erro SQL - insereGrupo({grupo.titulo}) <INSERT>')
        finally:
            grupoId = cursor.lastrowid
            self.disconectBD(cursor)
            return grupoId

    def findAll(self):

        self.connection.connect()
        cursor = self.connection.cursor()

        strComando = f"""SELECT grupoId, titulo, descricao, dataCadastro, dataUltAlt FROM {self.configs.tblGrupo};"""

        try:
            cursor.execute(strComando)
            return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - findAll({self.configs.tblGrupo}) <INSERT>')
        finally:
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        self.connection.close()

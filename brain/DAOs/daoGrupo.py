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

    def buscaParticipantesGrupo(self, eventoId: int):

        self.connection.connect()
        cursor = self.connection.cursor()

        strComando = f"""
            SELECT 
                c.clienteId, 
                c.nomeCliente, 
                c.sobrenomeCliente
            FROM {self.configs.tblParticipantes} p
                JOIN {self.configs.tblGrupo} g 
                    ON p.eventoId = g.grupoId
                JOIN {self.configs.tblCliente} c
                    ON c.clienteId = p.clienteId
                WHERE p.eventoId = {eventoId}"""

        try:
            cursor.execute(strComando)
            return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - buscaParticipantesGrupo({self.configs.tblParticipantes}, {self.configs.tblGrupo}, {self.configs.tblCliente}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def excluirGrupoEParticipantes(self, eventoId: int):

        self.connection.connect()
        cursor = self.connection.cursor()

        strComando = f"""DELETE FROM {self.configs.tblGrupo} WHERE grupoId = {eventoId}"""

        try:
            cursor.execute(strComando)

            strComando = f"""DELETE FROM {self.configs.tblParticipantes} WHERE eventoId = {eventoId}"""

            cursor.execute(strComando)
            self.connection.commit()
        except:
            raise Warning(f'Erro SQL - excluirGrupo({self.configs.tblGrupo}, {self.configs.tblParticipantes}) <DELETE>')
        finally:
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        self.connection.close()

import pymysql

from configBD import ConfigDB
from modelos.grupoModel import GrupoModelo


class DaoGrupo:

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

    def insereGrupo(self, grupo: GrupoModelo):

        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            INSERT INTO {self.configs.tblGrupo}
            (
                titulo, descricao, categoria, dataCadastro, dataUltAlt
            )
            VALUES
            (
                '{grupo.titulo}', '{grupo.descricao}', '{grupo.categoria}', NOW(), NOW()
            )
            """
        try:
            cursor.execute(strComando)
            self.db.commit()
        except:
            raise Warning(f'Erro SQL - insereGrupo({grupo.titulo}) <INSERT>')
        finally:
            grupoId = cursor.lastrowid
            self.disconectBD(cursor)
            return grupoId

    def findAll(self):

        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""SELECT grupoId, titulo, descricao, dataCadastro, dataUltAlt FROM {self.configs.tblGrupo};"""

        try:
            cursor.execute(strComando)
            return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - findAll({self.configs.tblGrupo}) <INSERT>')
        finally:
            self.disconectBD(cursor)

    def buscaParticipantesGrupo(self, eventoId: int):

        self.db.connect()
        cursor = self.db.cursor()

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

        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""DELETE FROM {self.configs.tblGrupo} WHERE grupoId = {eventoId}"""

        try:
            cursor.execute(strComando)

            strComando = f"""DELETE FROM {self.configs.tblParticipantes} WHERE eventoId = {eventoId}"""

            cursor.execute(strComando)
            self.db.commit()
        except:
            raise Warning(f'Erro SQL - excluirGrupo({self.configs.tblGrupo}, {self.configs.tblParticipantes}) <DELETE>')
        finally:
            self.disconectBD(cursor)

    def atualizarGrupo(self, grupo: GrupoModelo):

        self.db.connect()
        cursor = self.db.cursor()


        strComando = f"""
            UPDATE {self.configs.tblGrupo} SET 
                titulo = '{grupo.titulo}',
                descricao = '{grupo.descricao}',
                dataUltAlt = NOW()
            WHERE
                grupoId = {grupo.grupoId}"""

        try:
            cursor.execute(strComando)
            self.db.commit()
        except:
            raise Warning(f'Erro SQL - atualizarGrupo({self.configs.tblGrupo}) <UPDATE>')
        finally:
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        self.db.close()

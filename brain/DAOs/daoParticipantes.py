import pymysql

from configBD import ConfigDB


class DaoParticipantes:

    def __init__(self, db):
        self.db = db
        self.configs = ConfigDB()

        # self.db = pymysql.connect(
        #     host=self.configs.host,
        #     user=self.configs.user,
        #     passwd=self.configs.passwd,
        #     db=self.configs.banco,
        #     port=self.configs.port
        # )

    def findAll(self, select='Id, eventoId, grupoId, clienteId'):
        self.db.connect()
        cursor = self.db.cursor()

        strComando = f" SELECT {select} FROM {self.configs.tblParticipantes} ORDER BY clienteId"

        try:
            # Busca todos os participantes
            cursor.execute(strComando)
            return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - findAll({self.configs.tblParticipantes}) <INSERT>')
        finally:
            cursor.close()

    def insereParticipantesEvento(self, eventoId, grupoId=None, participantesEventoList: list=None ):

        self.db.connect()
        cursor = self.db.cursor()

        if grupoId:
            strComando = f" INSERT INTO {self.configs.tblParticipantes} ( eventoId, grupoId, clienteId ) VALUES "
            # Relaciona o evento a um grupo formado já com participantes
            for cliente in range(len(participantesEventoList)):
                if cliente == 0:
                    strComando += f"""( '{eventoId}', {grupoId}, '{participantesEventoList[cliente][0]}' )"""
                else:
                    strComando += f""",( '{eventoId}', {grupoId}, '{participantesEventoList[cliente][0]}' )"""
        else:
            # TODO: Implementar add participantes sem grupo ao evento  e os dois na tabela sem participantes
            strComando = f" INSERT INTO {self.configs.tblParticipantes} (eventoId, clienteId) VALUES ({eventoId}) "
            pass

        try:
            # Insere todos os participantes de um evento no banco de dados
            cursor.execute(strComando)
            self.db.commit()
        except:
            raise Warning(f'Erro SQL - teste() <INSERT>')
        finally:
            cursor.close()

    def insereParticipantes(self, participantesList: list):

        self.db.connect()
        cursor = self.db.cursor()

        strComando = f" INSERT INTO {self.configs.tblParticipantes} ( grupoId, clienteId ) VALUES "

        for i in range(0, len(participantesList)):
            if i == 0:
                strComando += f"""( '{participantesList[i].grupoId}', '{participantesList[i].clienteId}' )"""
            else:
                strComando += f""",( '{participantesList[i].grupoId}', '{participantesList[i].clienteId}' )"""

        try:
            # Insere todos os participantes de um evento no banco de dados
            cursor.execute(strComando)
            self.db.commit()
        except:
            raise Warning(f'Erro SQL - insereParticipantes({participantesList[0].grupoId}) <INSERT>')
        finally:
            cursor.close()

    def deletarParticipantesEvento(self, grupoId):

        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""DELETE FROM {self.configs.tblParticipantes} WHERE grupoId = {grupoId}"""

        try:
            cursor.execute(strComando)
            self.db.commit()
        except:
            raise Warning(f'Erro SQL - deletarParticipantesGrupo({grupoId}) <DELETE>')
        finally:
            cursor.close()

    def disconectBD(self, cursor):
        cursor.close()
        self.db.close()

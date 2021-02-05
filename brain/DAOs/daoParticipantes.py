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

    def insereParticipantes(self, participantesList: list):

        self.db.connect()
        cursor = self.db.cursor()

        strComando = f" INSERT INTO {self.configs.tblParticipantes} ( eventoId, clienteId ) VALUES "

        for i in range(0, len(participantesList)):
            if i == 0:
                strComando += f"""( '{participantesList[i].eventoId}', '{participantesList[i].clienteId}' )"""
            else:
                strComando += f""",( '{participantesList[i].eventoId}', '{participantesList[i].clienteId}' )"""

        try:
            # Insere todos os participantes de um evento no banco de dados
            cursor.execute(strComando)
            self.db.commit()
        except:
                raise Warning(f'Erro SQL - insereParticipantes({participantesList[0].eventoId}) <INSERT>')
        finally:
            cursor.close()

    def deletarParticipantesEvento(self, grupoId):

        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""DELETE FROM {self.configs.tblParticipantes} WHERE eventoId = {grupoId}"""

        try:
            cursor.execute(strComando)
            self.db.commit()
        except:
            raise Warning(f'Erro SQL - deletarParticipantesEvento({grupoId}) <DELETE>')
        finally:
            cursor.close()



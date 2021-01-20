import pymysql

from configBD import ConfigDB


class DaoParticipantes:

    def __init__(self):
        self.configs = ConfigDB()

        self.connection = pymysql.connect(
            host=self.configs.host,
            user=self.configs.user,
            passwd=self.configs.passwd,
            db=self.configs.banco
        )

    def insereParticipantes(self, participantesList: list):

        self.connection.connect()
        cursor = self.connection.cursor()

        strComando = f" INSERT INTO {self.configs.tblParticipantes} ( eventoId, clienteId ) VALUES "

        for i in range(0, len(participantesList)):
            if i == 0:
                strComando += f"""( '{participantesList[i].eventoId}', '{participantesList[i].clienteId}' )"""
            else:
                strComando += f""",( '{participantesList[i].eventoId}', '{participantesList[i].clienteId}' )"""

        try:
            # Insere todos os participantes de um evento no banco de dados
            cursor.execute(strComando)
            self.connection.commit()
        except:
                raise Warning(f'Erro SQL - insereParticipantes({participantesList[0].eventoId}) <INSERT>')
        finally:
            cursor.close()

    def deletarParticipantesEvento(self, grupoId):

        self.connection.connect()
        cursor = self.connection.cursor()

        strComando = f"""DELETE FROM {self.configs.tblParticipantes} WHERE eventoId = {grupoId}"""

        try:
            cursor.execute(strComando)
            self.connection.commit()
        except:
            raise Warning(f'Erro SQL - deletarParticipantesEvento({grupoId}) <DELETE>')
        finally:
            cursor.close()



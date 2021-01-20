import pymysql

from configBD import ConfigDB


class DaoCategoria:

    def __init__(self):
        self.configs = ConfigDB()

        self.connection = pymysql.connect(
            host=self.configs.host,
            user=self.configs.user,
            passwd=self.configs.passwd,
            db=self.configs.banco
        )

    def getAll(self):

        self.connection.connect()
        cursor = self.connection.cursor()

        strComando = f"""SELECT nome FROM {self.configs.tblCategoria}"""

        try:
            cursor.execute(strComando)

            return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - getAll({self.configs.tblCategoria}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        self.connection.close()
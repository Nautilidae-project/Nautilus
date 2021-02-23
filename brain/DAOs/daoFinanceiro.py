from pymysql import *

from configBD import ConfigDB


class DaoFinanceiro:

    def __init__(self, db: connect):
        self.db = db
        self.configs = ConfigDB()

    def getFaturamentoMensal(self):
        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""SELECT p.valor, c.dataCadastro FROM {self.configs.tblPlanos} p
                            JOIN {self.configs.tblCliente} c
                                ON c.plano = p.planoId;"""
        try:
            cursor.execute(strComando)
            return cursor.fetchall()
        except:
            raise Warning(
                f'Erro SQL - getFaturamentoMensal({self.configs.tblPlanos}, {self.configs.tblCliente})<SELECT>')
        finally:
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        self.db.close()

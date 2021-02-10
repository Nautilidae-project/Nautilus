import pymysql

from configBD import ConfigDB

from modelos.categoriaModel import CategoriaModel


class DaoCategoria:

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

    def getAll(self):

        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""SELECT nome FROM {self.configs.tblCategoria}"""

        try:
            cursor.execute(strComando)

            return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - getAll({self.configs.tblCategoria}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def insereCategoria(self, categoria: CategoriaModel):
        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""INSERT INTO {self.configs.tblCategoria} (nome, cor) VALUES ('{categoria.nome}', '{categoria.cor}')"""

        try:
            cursor.execute(strComando)
        except:
            raise Warning(f'Erro SQL - insereCategoria({self.configs.tblCategoria}) <SELECT>')
        finally:
            self.db.commit()
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        self.db.close()
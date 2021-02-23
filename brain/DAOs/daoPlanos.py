from configBD import ConfigDB
from modelos.eventoModel import EventoModelo
from modelos.planoModel import PlanoModelo


class DaoPlanos:

    def __init__(self, db):
        self.db = db
        self.configs = ConfigDB()

    def getAll(self, ativo: bool = True):
        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""SELECT planoId, nomePlano, valor, descricao, periodoUnidade, dataInicio, dataFim, presencial FROM {self.configs.tblPlanos}"""

        if not ativo:
            strComando += f""" WHERE ativo = TRUE"""

        try:
            cursor.execute(strComando)
            return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - getAll({ativo})({self.configs.tblPlanos}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def getAllPlanosId(self):
        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""SELECT 
                            planoId, nomePlano 
                        FROM {self.configs.tblPlanos}
                            WHERE ativo = TRUE;"""

        try:
            cursor.execute(strComando)
            return cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - getAllPlanosId({self.configs.tblPlanos}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def inserePlano(self, plano: PlanoModelo):
        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""INSERT INTO {self.configs.tblPlanos} 
                            (nomePlano, valor, descricao, periodoUnidade, 
                            dataInicio, dataFim, presencial, dataCadastro, dataUltAlt) 
                        VALUES 
                            ('{plano.nomePlano}', {plano.valor}, '{plano.descricao}', '{plano.periodoUnidade}', 
                            '{plano.dataInicio}', '{plano.dataFim}', '{plano.presencial}', NOW(), NOW());"""
        try:
            if cursor.execute(strComando) == 1:
                self.db.commit()
                return True
            else:
                return False
        except:
            raise Warning(f'Erro SQL - inserePlano({self.configs.tblPlanos}) <INSERT>')
        finally:
            self.disconectBD(cursor)

    def buscaPlanoPorId(self, planoId: int):
        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""SELECT 
                            planoId, nomePlano, valor, descricao, periodoUnidade, dataInicio, dataFim, presencial
                        FROM 
                            {self.configs.tblPlanos} 
                        WHERE 
                            planoId = {planoId}"""

        try:
            cursor.execute(strComando)
            return cursor.fetchone()
        except:
            raise Warning(f'Erro SQL - buscaPlanoPorId({planoId})({self.configs.tblPlanos}) <SELECT>')
        finally:
            self.disconectBD(cursor)



    def disconectBD(self, cursor):
        cursor.close()
        self.db.close()


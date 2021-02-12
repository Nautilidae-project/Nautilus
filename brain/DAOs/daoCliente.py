from configBD import ConfigDB
from modelos.clienteModel import Cliente
import pymysql


class DaoCliente:

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

    def cadastraCliente(self, cliente: Cliente):

        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            INSERT INTO cliente
            (
                nomeCliente, sobrenomeCliente, telefone,
                email, cpf, endereco, complemento , cep, bairro,
                meioPagamento, ativo, dataCadastro, dataUltAlt
            )
            VALUES
            (
                '{cliente.nomeCliente}', '{cliente.sobrenomeCliente}', '{cliente.telefone}',
                '{cliente.email}', '{cliente.cpf}', '{cliente.endereco}', '{cliente.complemento}', '{cliente.cep}',
                '{cliente.bairro}', 'CC', {cliente.ativo}, NOW(), NOW()
            )
            """
        try:
            cursor.execute(strComando)
            self.db.commit()
            cursor.close()
        except:
            raise Warning(f'Erro SQL - insereCliente({cliente.clienteId}) <INSERT>')
        finally:
            cursor.close()

    def findAll(self, all= False):

        self.db.connect()
        cursor = self.db.cursor()

        if not all:
            strComando = f"SELECT clienteId, nomeCliente, sobrenomeCliente, telefone, meioPagamento, ativo FROM {self.configs.tblCliente} ORDER BY ativo DESC, nomeCliente ASC"

        else:
            strComando = f"SELECT * FROM {self.configs.tblCliente} ORDER BY ativo DESC, nomeCliente ASC"

        cursor.execute(strComando)

        clientesList = cursor.fetchall()
        cursor.close()

        return clientesList

    def findAllNomeSobrenome(self, letra=None):

        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""SELECT 
                            clienteId, nomeCliente, sobrenomeCliente, ativo
                        FROM {self.configs.tblCliente}
                            WHERE ativo = 1"""

        if letra is not None:
            strComando += f""" AND nomeCliente LIKE '{letra}%' """

        strComando += """ ORDER BY nomeCliente;"""

        cursor.execute(strComando)

        clientesList = cursor.fetchall()
        cursor.close()

        return clientesList

    def buscaCliente(self, busca):

        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"SELECT clienteId, nomeCliente, telefone, meioPagamento, ativo  FROM cliente where " \
                     f"nomeCliente LIKE '%{busca}%' OR " \
                     f"sobrenomeCliente like '%{busca}%' OR " \
                     f"telefone like '%{busca}%' ORDER BY ativo DESC"

        cursor.execute(strComando)
        clientesList = cursor.fetchall()

        cursor.close()

        return clientesList

    def buscaPorId(self, clienteId: int):
        listCliente = []

        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""SELECT * FROM {self.configs.tblCliente} WHERE clienteId = {clienteId} """

        try:
            cursor.execute(strComando)
            listCliente = cursor.fetchall()
        except:
            raise Warning(f'Erro SQL - buscaPorId({clienteId}) <SELECT>')
        finally:
            cursor.close()
            if len(listCliente) == 0:
                return []
            else:
                return listCliente

    def atualizaInfoCliente(self, cliente):

        self.db.connect()
        cursor = self.db.cursor()

        strComando = f""" UPDATE {self.configs.tblCliente} SET 
                            nomeCliente = '{cliente.nomeCliente}', 
                            sobrenomeCliente = '{cliente.sobrenomeCliente}', 
                            telefone = '{cliente.telefone}',
                            email = '{cliente.email}', 
                            cpf = '{cliente.cpf}', 
                            endereco = '{cliente.endereco}', 
                            complemento = '{cliente.complemento}', 
                            cep = '{cliente.cep}', 
                            bairro = '{cliente.bairro}',
                            meioPagamento = '{cliente.meioPagamento}', 
                            ativo = {cliente.ativo},
                            dataUltAlt = NOW()
                        WHERE
                            clienteId = {cliente.clienteId}
                    
                    """
        try:
            cursor.execute(strComando)
            self.db.commit()
        except:
            raise Warning(f'Erro SQL - atualizaInfoCliente({cliente.clienteId}) <UPDATE>')
        finally:
            self.disconectBD(cursor)

    def contaTotal(self, where=None):

        self.db.connect()
        cursor = self.db.cursor()

        if where is None:
            strComando = f''' SELECT COUNT(*) FROM {self.configs.tblCliente} '''
        else:
            strComando = f''' SELECT COUNT(*) FROM {self.configs.tblCliente} {where} '''

        cursor.execute(strComando)

        total = cursor.fetchone()[0]
        self.disconectBD(cursor)

        return total

    def contaCliente(self, condicao="clienteId"):
        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"SELECT COUNT(clienteId) FROM cliente where {condicao}"

        try:
            cursor.execute(strComando)

            clientesList = cursor.fetchall()
            return str(clientesList[0][0])
        except:
            raise Warning(f'Erro SQL - contaCliente({self.configs.tblCliente}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def buscaClientesAtuaisMesAno(self, mesAno='ano') -> int:
        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""SELECT COUNT(*) FROM cliente WHERE YEAR(dataCadastro) = YEAR(NOW())"""

        if mesAno.upper() == 'MES' or mesAno.upper() == 'M' or mesAno.upper() == 'MENSAL':
            strComando += f""" AND MONTH(dataCadastro) = MONTH(NOW());"""
        else:
            strComando += ';'

        try:
            print(strComando)
            cursor.execute(strComando)
            intClientes = cursor.fetchone()
            if intClientes is not None:
                return int(intClientes[0])
            else:
                return -1
        except:
            raise Warning(f'Erro SQL - buscaClientesAtuaisMesAno({self.configs.tblCliente}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def buscaClientePeridoPassado(self, mesAno='ano'):
        self.db.connect()
        cursor = self.db.cursor()

        if mesAno.upper() == 'MES' or mesAno.upper() == 'M' or mesAno.upper() == 'MENSAL':
            strComando = f"""SELECT COUNT(*) FROM cliente WHERE MONTH(DATE_SUB(NOW(), INTERVAL 1 MONTH)) = MONTH(dataCadastro);"""
        else:
            strComando = f"""SELECT COUNT(*) FROM cliente WHERE YEAR(DATE_SUB(NOW(), INTERVAL 1 YEAR)) = YEAR(dataCadastro);"""
        try:
            cursor.execute(strComando)
            intClientes = cursor.fetchone()
            if intClientes is not None:
                return int(intClientes[0])
            else:
                return -1
        except:
            raise Warning(f'Erro SQL - buscaClientePeridoPassado({self.configs.tblCliente}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        self.db.close()

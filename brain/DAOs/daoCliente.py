from configBD import ConfigDB
import pymysql

from modelos.clienteModel import Cliente


class DaoCliente():

    def __init__(self):
        self.configs = ConfigDB()

        self.connection = pymysql.connect(
            host=self.configs.host,
            user=self.configs.user,
            passwd=self.configs.passwd,
            db=self.configs.banco
        )

    def cadastraCliente(self, cliente):

        cursor = self.connection.cursor()

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
            self.connection.commit()
            # self.connection.close()
        except:
            raise Warning(f'Erro SQL - insereCliente({cliente.clienteId}) <INSERT>')

    def findAll(self):

        cursor = self.connection.cursor()

        # strComando = f"SELECT * FROM {configs.tblCliente}"
        strComando = f"SELECT clienteId, nomeCliente, telefone, meioPagamento, ativo FROM {self.configs.tblCliente} ORDER BY ativo DESC"

        cursor.execute(strComando)

        return cursor.fetchall()

    def buscaCliente(self, busca):

        cursor = self.connection.cursor()

        strComando = f"SELECT clienteId, nomeCliente, telefone, meioPagamento, ativo  FROM cliente where " \
                     f"nomeCliente LIKE '%{busca}%' OR " \
                     f"sobrenomeCliente like '%{busca}%' OR " \
                     f"telefone like '%{busca}%' ORDER BY ativo DESC"

        cursor.execute(strComando)

        return cursor.fetchall()

    def buscaPorId(self, clienteId: int):
        listCliente = []

        cursor = self.connection.cursor()

        strComando = f"""SELECT * FROM {self.configs.tblCliente} WHERE clienteId = {clienteId} """

        try:
            cursor.execute(strComando)
            listCliente = cursor.fetchall()
            # connection.close()
        except:
            raise Warning(f'Erro SQL - buscaPorId({clienteId}) <SELECT>')
        finally:
            if len(listCliente) == 0:
                return []
            else:
                return listCliente

    def atualizaInfoCliente(self, cliente):

        cursor = self.connection.cursor()

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

        print(strComando)

        try:
            cursor.execute(strComando)
            self.connection.commit()

        except:
            raise Warning(f'Erro SQL - atualizaInfoCliente({cliente.clienteId}) <UPDATE>')

import pymysql
from configBD import ConfigDB
from os.path import join, dirname
from os import listdir
from bcrypt import checkpw
from modelos.estadosModel import EstadosModelo


class DaoConfiguracoes:
    def __init__(self):
        self.configs = ConfigDB()

        self.connection = pymysql.connect(
            host=self.configs.host,
            user=self.configs.user,
            passwd=self.configs.passwd,
            db=self.configs.banco
        )

        self.cursor = self.connection.cursor()

    def criaTblUsuario(self):

        try:
            self.cursor.execute(self.configs.sqlCreateUsuario)
            self.connection.commit()
            return True
        except:
            raise Warning(f'Erro SQL - criaTblUsuario({self.configs.banco}) <CREATE TABLE ({self.configs.tblUsuario})>')

    def criaTblCliente(self):

        try:
            self.cursor.execute(self.configs.sqlCreateCliente)
            self.connection.commit()
            return True
        except:
            raise Warning(f'Erro SQL - criaTblCliente({self.configs.banco}) <CREATE TABLE {self.configs.tblCliente}>')

    def criaTblTurma(self):

        try:
            self.cursor.execute(self.configs.sqlCreateTurma)
            self.connection.commit()
            return True
        except:
            raise Warning(f'Erro SQL - criaTblTurma({self.configs.banco}) <CREATE TABLE {self.configs.tblTurma}>')

    def criaTblEvento(self):

        try:
            self.cursor.execute(self.configs.sqlCreateEvento)
            self.connection.commit()
            return True
        except:
            raise Warning(f'Erro SQL - criaTblEvento({self.configs.banco}) <CREATE TABLE {self.configs.tblEvento}>')

    def criaTblParticipantes(self):

        try:
            self.cursor.execute(self.configs.sqlCreateParticipantes)
            self.connection.commit()
            return True
        except:
            raise Warning(f'Erro SQL - criaTblParticipantes({self.configs.banco}) <CREATE TABLE {self.configs.tblParticipantes}>')

    def criaTblEstado(self):

        try:
            self.cursor.execute(self.configs.sqlCreateEstado)
            self.connection.commit()
            return True
        except:
            raise Warning(f'Erro SQL - criaBanco({self.configs.banco}) <CREATE TABLE {self.configs.tblEstados}>')

    def addEstados(self):

        listaEstados = EstadosModelo().toDict()

        for extenso, sigla in listaEstados.items():
            strComando = f"""INSERT INTO estados
                                    (sigla, extenso)
                                VALUES
                                    ('{sigla}', '{extenso}')"""

            self.cursor.execute(strComando)
        self.connection.commit()
        return True

    def getEstados(self, *args):

        if args != ():
            if len(args[0]) > 2:
                strComando = f"""SELECT sigla FROM {self.configs.tblEstados} WHERE extenso = '{args[0]}'"""
            else:
                strComando = f"""SELECT extenso FROM {self.configs.tblEstados} WHERE sigla = '{args[0]}'"""
        else:
            strComando = f"""SELECT extenso FROM {self.configs.tblEstados} ORDER BY extenso"""

        self.cursor.execute(strComando)

        return [estado[0] for estado in self.cursor.fetchall()]

    def cadastreUsuario(self, usuario):

        strComando = f"""
            INSERT INTO usuario
            (
                 nomeUsuario, nomeEmpresa, nomeFantasia,
                 cnpj, email, tel,
                 endereco, cep, senha, dataCadastro
            )
            VALUES
            (
                '{usuario.nomeUsuario}', '{usuario.nomeEmpresa}', '{usuario.nomeFantasia}',
                '{usuario.cnpj}', '{usuario.email}', {usuario.tel},
                '{usuario.endereco}', '{usuario.cep}', '{usuario.senha}', NOW()
            )
            """
        try:
            self.cursor.execute(strComando)
            self.connection.commit()
            return True
        except:
            raise Exception(f'Erro SQL - cadastreUsuario({usuario.userId}) <CREATE TABLE>')

    def buscaUsuario(self, strUsuario):

        strComando = f"""
                    SELECT * 
                    FROM {self.configs.tblUsuario}
                    WHERE 
                        nomeUsuario = '{strUsuario}'
                    OR
                        email = '{strUsuario}'
                    OR
                        nomeEmpresa = '{strUsuario}'
                    OR
                        cnpj = '{strUsuario}'
                    """

        self.cursor.execute(strComando)

        if self.cursor.fetchone() is None:
            return False
        else:
            return True

    def confereSenha(self, strUsuario, password):

        strComando = f'''
                    SELECT senha 
                    FROM {self.configs.tblUsuario}
                    WHERE 
                        nomeUsuario = '{strUsuario}'
                    OR
                        email = '{strUsuario}'
                    OR
                        nomeEmpresa = '{strUsuario}'
                    OR
                        cnpj = '{strUsuario}'
        '''

        try:
            self.cursor.execute(strComando)
            senha = self.cursor.fetchall()[0][0]
            strPassword = str(password)
            return checkpw(strPassword.encode('utf-8'), senha)
        except:
            raise Exception(f'Erro SQL - confereSenha({self.configs.tblUsuario}) <SELECT>')

    def verificaEstados(self):

        strComando = """ SELECT COUNT(*) FROM estados"""

        self.cursor.execute(strComando)

        if self.cursor.fetchone()[0] != 27:
            strComando = " DROP TABLE estados"
            self.cursor.execute(strComando)
            return False
        else:
            return True

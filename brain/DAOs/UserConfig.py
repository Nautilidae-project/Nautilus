import pymysql
from configBD import ConfigDB
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

    def criaTblUsuario(self):

        self.connection.connect()
        cursor = self.connection.cursor()

        try:
            cursor.execute(self.configs.sqlCreateUsuario)
            self.connection.commit()
            # cursor.close()
            return True
        except:
            raise Warning(f'Erro SQL - criaTblUsuario({self.configs.banco}) <CREATE TABLE ({self.configs.tblUsuario})>')
        finally:
            cursor.close()
            self.connection.close()

    def criaTblCliente(self):

        self.connection.connect()
        cursor = self.connection.cursor()

        try:
            cursor.execute(self.configs.sqlCreateCliente)
            self.connection.commit()
            # cursor.close()
            return True
        except:
            raise Warning(f'Erro SQL - criaTblCliente({self.configs.banco}) <CREATE TABLE {self.configs.tblCliente}>')
        finally:
            cursor.close()
            self.connection.close()

    def criaTblGrupo(self):

        self.connection.connect()
        cursor = self.connection.cursor()

        try:
            cursor.execute(self.configs.sqlCreateGrupo)
            self.connection.commit()
            # cursor.close()
            return True
        except:
            raise Warning(f'Erro SQL - criaTblGrupo({self.configs.banco}) <CREATE TABLE {self.configs.tblGrupo}>')
        finally:
            cursor.close()
            self.connection.close()

    def criaTblEvento(self):

        self.connection.connect()
        cursor = self.connection.cursor()

        try:
            cursor.execute(self.configs.sqlCreateEvento)
            self.connection.commit()
            # cursor.close()
            return True
        except:
            raise Warning(f'Erro SQL - criaTblEvento({self.configs.banco}) <CREATE TABLE {self.configs.tblEvento}>')
        finally:
            cursor.close()
            self.connection.close()

    def criaTblParticipantes(self):

        self.connection.connect()
        cursor = self.connection.cursor()

        try:
            cursor.execute(self.configs.sqlCreateParticipantes)
            self.connection.commit()
            # cursor.close()
            return True
        except:
            raise Warning(
                f'Erro SQL - criaTblParticipantes({self.configs.banco}) <CREATE TABLE {self.configs.tblParticipantes}>')
        finally:
            cursor.close()
            self.connection.close()

    def criaTblEstado(self):

        self.connection.connect()
        cursor = self.connection.cursor()

        try:
            cursor.execute(self.configs.sqlCreateEstado)
            self.connection.commit()
            # cursor.close()
            return True
        except:
            raise Warning(f'Erro SQL - criaBanco({self.configs.banco}) <CREATE TABLE {self.configs.tblEstados}>')
        finally:
            self.disconectBD(cursor)

    def addEstados(self):

        self.connection.connect()
        cursor = self.connection.cursor()

        listaEstados = EstadosModelo().toDict()

        for extenso, sigla in listaEstados.items():
            strComando = f"""INSERT INTO estados
                                    (sigla, extenso)
                                VALUES
                                    ('{sigla}', '{extenso}')"""
            try:
                cursor.execute(strComando)
            except:
                raise Warning(f'Erro SQL - addEstados({self.configs.banco}) <INSERT {self.configs.tblEstados}>')

        self.connection.commit()
        self.disconectBD(cursor)
        return True

    def getEstados(self, *args):

        self.connection.connect()
        cursor = self.connection.cursor()

        if args != ():
            if len(args[0]) > 2:
                strComando = f"""SELECT sigla FROM {self.configs.tblEstados} WHERE extenso = '{args[0]}'"""
            else:
                strComando = f"""SELECT extenso FROM {self.configs.tblEstados} WHERE sigla = '{args[0]}'"""
        else:
            strComando = f"""SELECT extenso FROM {self.configs.tblEstados} ORDER BY extenso"""

        try:
            cursor.execute(strComando)
            listaEstados = [estado[0] for estado in cursor.fetchall()]
            return listaEstados
        except:
            raise Warning(f'Erro SQL - getEstados({self.configs.banco}) <SELECT {self.configs.tblEstados}>')
        finally:
            self.disconectBD(cursor)

    def cadastreUsuario(self, usuario):

        self.connection.connect()
        cursor = self.connection.cursor()

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
            cursor.execute(strComando)
            self.connection.commit()
            return True
        except:
            raise Exception(f'Erro SQL - cadastreUsuario({usuario.userId}) <CREATE TABLE>')
        finally:
            cursor.close()
            self.connection.close()

    def buscaUsuario(self, strUsuario):

        self.connection.connect()
        cursor = self.connection.cursor()

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

        try:
            cursor.execute(strComando)

            if cursor.fetchone() is None:
                return False
            else:
                return True
        except:
            raise Exception(f'Erro SQL - buscaUsuario({strUsuario}) <SELECT {self.configs.tblUsuario}>')
        finally:
            self.disconectBD(cursor)

    def confereSenha(self, strUsuario, password):

        self.connection.connect()
        cursor = self.connection.cursor()

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
            cursor.execute(strComando)
            senha = cursor.fetchall()[0][0]
            strPassword = str(password)
            return checkpw(strPassword.encode('utf-8'), senha)
        except:
            raise Exception(f'Erro SQL - confereSenha({self.configs.tblUsuario}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def verificaEstados(self):

        self.connection.connect()
        cursor = self.connection.cursor()

        strComando = """ SELECT COUNT(*) FROM estados"""

        cursor.execute(strComando)

        if cursor.fetchone()[0] != 27:
            strComando = " DROP TABLE estados"
            cursor.execute(strComando)
            self.disconectBD(cursor)
            return False
        else:
            self.disconectBD(cursor)
            return True

    def disconectBD(self, cursor):
        cursor.close()
        self.connection.close()

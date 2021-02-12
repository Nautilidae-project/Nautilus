import pymysql
from configBD import ConfigDB
from bcrypt import checkpw
from modelos.estadosModel import EstadosModelo


class DaoConfiguracoes:

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

    def criaTblUsuario(self):

        self.db.connect()
        cursor = self.db.cursor()

        try:
            cursor.execute(self.configs.sqlCreateUsuario)
            self.db.commit()
            # cursor.close()
            return True
        except:
            raise Warning(f'Erro SQL - criaTblUsuario({self.configs.banco}) <CREATE TABLE ({self.configs.tblUsuario})>')
        finally:
            cursor.close()
            self.db.close()

    def criaTblCliente(self):

        self.db.connect()
        cursor = self.db.cursor()

        try:
            cursor.execute(self.configs.sqlCreateCliente)
            self.db.commit()
            # cursor.close()
            return True
        except:
            raise Warning(f'Erro SQL - criaTblCliente({self.configs.banco}) <CREATE TABLE {self.configs.tblCliente}>')
        finally:
            cursor.close()
            self.db.close()

    def criaTblGrupo(self):

        self.db.connect()
        cursor = self.db.cursor()

        try:
            cursor.execute(self.configs.sqlCreateGrupo)
            self.db.commit()
            # cursor.close()
            return True
        except:
            raise Warning(f'Erro SQL - criaTblGrupo({self.configs.banco}) <CREATE TABLE {self.configs.tblGrupo}>')
        finally:
            cursor.close()
            self.db.close()

    def criaTblEvento(self):

        self.db.connect()
        cursor = self.db.cursor()

        try:
            cursor.execute(self.configs.sqlCreateEvento)
            self.db.commit()
            # cursor.close()
            return True
        except:
            raise Warning(f'Erro SQL - criaTblEvento({self.configs.banco}) <CREATE TABLE {self.configs.tblEvento}>')
        finally:
            cursor.close()
            self.db.close()

    def criaTblParticipantes(self):

        self.db.connect()
        cursor = self.db.cursor()

        try:
            cursor.execute(self.configs.sqlCreateParticipantes)
            self.db.commit()
            # cursor.close()
            return True
        except:
            raise Warning(
                f'Erro SQL - criaTblParticipantes({self.configs.banco}) <CREATE TABLE {self.configs.tblParticipantes}>')
        finally:
            cursor.close()
            self.db.close()

    def criaTblEstado(self):

        self.db.connect()
        cursor = self.db.cursor()

        try:
            cursor.execute(self.configs.sqlCreateEstado)
            self.db.commit()
            # cursor.close()
            return True
        except:
            raise Warning(f'Erro SQL - criaBanco({self.configs.banco}) <CREATE TABLE {self.configs.tblEstados}>')
        finally:
            self.disconectBD(cursor)

    def criaTblCategoria(self):
        self.db.connect()
        cursor = self.db.cursor()

        try:
            cursor.execute(self.configs.sqlCreateCategoria)
            self.db.commit()
            return True
        except:
            raise Warning(f'Erro SQL - criaBanco({self.configs.banco}) <CREATE TABLE {self.configs.tblCategoria}>')
        finally:
            self.disconectBD(cursor)

    def addEstados(self):

        self.db.connect()
        cursor = self.db.cursor()

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

        self.db.commit()
        self.disconectBD(cursor)
        return True

    def getEstados(self, *args):

        self.db.connect()
        cursor = self.db.cursor()

        if args != ():
            if len(args[0]) > 2:
                strComando = f"""SELECT sigla FROM {self.configs.tblEstados} WHERE extenso = '{args[0]}'"""
            else:
                strComando = f"""SELECT extenso FROM {self.configs.tblEstados} WHERE sigla = '{args[0]}'"""
        else:
            strComando = f"""SELECT extenso FROM {self.configs.tblEstados} ORDER BY extenso"""

        try:
            cursor.execute(strComando)
            estadosEncontrados = cursor.fetchall()
            listaEstados = [estado[0] for estado in estadosEncontrados]
            return listaEstados
        except:
            raise Warning(f'Erro SQL - getEstados({self.configs.banco}) <SELECT {self.configs.tblEstados}>')
        finally:
            self.disconectBD(cursor)

    # def cadastreUsuario(self, usuario):
    #
    #     self.db.connect()
    #     cursor = self.db.cursor()
    #
    #     strComando = f"""
    #         INSERT INTO usuario
    #         (
    #              nomeUsuario, nomeEmpresa, nomeFantasia,
    #              cnpj, email, tel,
    #              endereco, cidade, cep, senha, dataCadastro
    #         )
    #         VALUES
    #         (
    #             '{usuario.nomeUsuario}', '{usuario.nomeEmpresa}', '{usuario.nomeFantasia}',
    #             '{usuario.cnpj}', '{usuario.email}', {usuario.tel},
    #             '{usuario.endereco}', '{usuario.cidade}', '{usuario.cep}', '{usuario.senha}', NOW()
    #         )
    #         """
    #     try:
    #         cursor.execute(strComando)
    #         self.db.commit()
    #         return True
    #     except:
    #         raise Exception(f'Erro SQL - cadastreUsuario({usuario.userId}) <CREATE TABLE>')
    #     finally:
    #         cursor.close()
    #         self.db.close()
    #
    # def verificaUsuario(self, strUsuario):
    #
    #     self.db.connect()
    #     cursor = self.db.cursor()
    #
    #     strComando = f"""
    #                    SELECT *
    #                    FROM {self.configs.tblUsuario}
    #                    WHERE
    #                        nomeUsuario = '{strUsuario}'
    #                    OR
    #                        email = '{strUsuario}'
    #                    OR
    #                        nomeEmpresa = '{strUsuario}'
    #                    OR
    #                        cnpj = '{strUsuario}'
    #                    """
    #
    #     try:
    #         cursor.execute(strComando)
    #
    #         if cursor.fetchone() is None:
    #             return False
    #         else:
    #             return True
    #     except:
    #         raise Exception(f'Erro SQL - verificaUsuario({strUsuario}) <SELECT {self.configs.tblUsuario}>')
    #     finally:
    #         self.disconectBD(cursor)
    #
    # def confereSenha(self, strUsuario, password):
    #
    #     self.db.connect()
    #     cursor = self.db.cursor()
    #
    #     strComando = f'''
    #                    SELECT senha
    #                    FROM {self.configs.tblUsuario}
    #                    WHERE
    #                        nomeUsuario = '{strUsuario}'
    #                    OR
    #                        email = '{strUsuario}'
    #                    OR
    #                        nomeEmpresa = '{strUsuario}'
    #                    OR
    #                        cnpj = '{strUsuario}'
    #        '''
    #     try:
    #         cursor.execute(strComando)
    #         senha = cursor.fetchall()[0][0]
    #         strPassword = str(password)
    #         return checkpw(strPassword.encode('utf-8'), senha)
    #     except:
    #         raise Exception(f'Erro SQL - confereSenha({self.configs.tblUsuario}) <SELECT>')
    #     finally:
    #         self.disconectBD(cursor)
    #
    # def buscaUsuarioAtivo(self):
    #
    #     self.db.connect()
    #     cursor = self.db.cursor()
    #
    #     strComando = f'SELECT * FROM {self.configs.tblUsuario} LIMIT 1'
    #
    #     try:
    #         cursor.execute(strComando)
    #         return cursor.fetchone()
    #     except:
    #         raise Exception(f'Erro SQL - buscaUsuarioAtivo()) <SELECT {self.configs.tblUsuario}>')
    #     finally:
    #         self.disconectBD(cursor)

    def verificaEstados(self):

        self.db.connect()
        cursor = self.db.cursor()

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
        self.db.close()


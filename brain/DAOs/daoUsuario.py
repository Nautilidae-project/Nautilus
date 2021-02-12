from bcrypt import checkpw

from configBD import ConfigDB
from modelos.usuarioModel import UsuarioModel


class DaoUsuario:

    def __init__(self, db):
        self.db = db
        self.configs = ConfigDB()

    def carregaUsrAtual(self, id):
        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""SELECT 
                            userId, nomeUsuario, nomeEmpresa, 
                            nomeFantasia, caminhoLogo, cnpj, 
                            email, tel, endereco, 
                            cidade, complemento, cep, 
                            bairro, dataCadastro
                        FROM 
                            {self.configs.tblUsuario}
                        WHERE
                            userId = {id}"""
        try:
            cursor.execute(strComando)
            usuarioModel = UsuarioModel().fromList(cursor.fetchone())
            if usuarioModel is not None:
                return usuarioModel
            else:
                return None
        except:
            raise Exception(f'Erro SQL - carregaUsrAtual({self.configs.tblUsuario}) <SELECT>')

    def cadastreUsuario(self, usuario: UsuarioModel):

        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""
            INSERT INTO usuario
            (
                 nomeUsuario, nomeEmpresa, nomeFantasia,
                 cnpj, email, tel,
                 endereco, cidade, complemento, 
                 cep, bairro, senha, 
                 dataUltAlt, dataCadastro
            )
            VALUES
            (
                '{usuario.nomeUsuario}', '{usuario.nomeEmpresa}', '{usuario.nomeFantasia}',
                '{usuario.cnpj}', '{usuario.email}', '{usuario.tel}',
                '{usuario.endereco}', '{usuario.cidade}', '{usuario.complemento}', 
                '{usuario.cep}', '{usuario.bairro}', '{usuario.senha}', 
                NOW(), NOW()
            )
            """
        try:
            cursor.execute(strComando)
            self.db.commit()
            return True
        except:
            raise Exception(f'Erro SQL - cadastreUsuario({usuario.userId}) <CREATE TABLE>')
        finally:
            cursor.close()
            self.db.close()

    def verificaUsuario(self, strUsuario):

        self.db.connect()
        cursor = self.db.cursor()

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
            raise Exception(f'Erro SQL - verificaUsuario({strUsuario}) <SELECT {self.configs.tblUsuario}>')
        finally:
            self.disconectBD(cursor)

    def confereSenha(self, strUsuario, password):

        self.db.connect()
        cursor = self.db.cursor()

        strComando = f'''
                       SELECT senha, userId
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

            usrEncontrado = cursor.fetchall()[0]
            id = usrEncontrado[1]
            senha = usrEncontrado[0]
            strPassword = str(password)

            if checkpw(strPassword.encode('utf-8'), senha):
                return id
            else:
                return None
        except:
            raise Exception(f'Erro SQL - confereSenha({self.configs.tblUsuario}) <SELECT>')
        finally:
            self.disconectBD(cursor)

    def buscaUsuarioAtivo(self):

        self.db.connect()
        cursor = self.db.cursor()

        strComando = f'SELECT * FROM {self.configs.tblUsuario} LIMIT 1'

        try:
            cursor.execute(strComando)
            return cursor.fetchone()
        except:
            raise Exception(f'Erro SQL - buscaUsuarioAtivo()) <SELECT {self.configs.tblUsuario}>')
        finally:
            self.disconectBD(cursor)

    def buscaLogoPath(self, userId):
        self.db.connect()
        cursor = self.db.cursor()

        strComando = f""" SELECT caminhoLogo FROM {self.configs.tblUsuario} WHERE userId = {userId}"""

        try:
            cursor.execute(strComando)
            return cursor.fetchone()[0]
        except:
            raise Exception(f'Erro SQL - buscaLogoPath()) <SELECT {self.configs.tblUsuario}>')
        finally:
            self.disconectBD(cursor)

    def atualizaLogoPath(self, logoPath: str, idUsuario: int):
        self.db.connect()
        cursor = self.db.cursor()

        strComando = f"""UPDATE {self.configs.tblUsuario} 
                         SET caminhoLogo = '{logoPath}',
                             dataUltAlt = NOW()
                         WHERE userId = {idUsuario}"""

        try:
            cursor.execute(strComando)
            self.db.commit()
        except:
            raise Exception(f'Erro SQL - atualizaLogoPath()) <SELECT {self.configs.tblUsuario}>')
        finally:
            self.disconectBD(cursor)

    def disconectBD(self, cursor):
        cursor.close()
        self.db.close()

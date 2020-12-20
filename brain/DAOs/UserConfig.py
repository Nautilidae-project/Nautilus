import pymysql
from configBD import ConfigDB
from os.path import join, dirname
from os import listdir
from bcrypt import checkpw
from modelos.estadosModel import EstadosModelo


def criaBanco():
    configs = ConfigDB()

    connection = pymysql.connect(
        host=configs.host,
        user=configs.user,
        passwd=configs.passwd,
        db=configs.banco
    )
    cursor = connection.cursor()

    try:
        cursor.execute(configs.sqlCreateUsuario)
        connection.commit()
        return True
    except:
        raise Warning(f'Erro SQL - criaBanco({configs.banco}) <CREATE TABLE ({configs.tblUsuario})>')
    finally:
        try:
            cursor.execute(configs.sqlCreateEstado)
            connection.commit()
            return True
        except:
            raise Warning(f'Erro SQL - criaBanco({configs.banco}) <CREATE TABLE {configs.tblEstados}>')
        finally:
            try:
                cursor.execute(configs.sqlCreateCliente)
                connection.commit()
                return True
            except:
                raise Warning(f'Erro SQL - criaBanco({configs.banco}) <CREATE TABLE {configs.tblCliente}>')
            finally:
                connection.close()


def addEstados():
    configs = ConfigDB()

    connection = pymysql.connect(
        host=configs.host,
        user=configs.user,
        passwd=configs.passwd,
        db=configs.banco
    )
    cursor = connection.cursor()

    strComando = '''SELECT * FROM estados LIMIT 1'''

    cursor.execute(strComando)
    if len(cursor.fetchall()) != 0:
        return False

    listaEstados = EstadosModelo().toDict()

    for extenso, sigla in listaEstados.items():
        strComando = f"""INSERT INTO estados
                                (sigla, extenso)
                            VALUES
                                ('{sigla}', '{extenso}')"""
        cursor.execute(strComando)
    connection.commit()
    connection.close()
    return True


def getEstados(*args):
    configs = ConfigDB()

    connection = pymysql.connect(
        host=configs.host,
        user=configs.user,
        passwd=configs.passwd,
        db=configs.banco
    )
    cursor = connection.cursor()
    if args != ():
        if len(args[0]) > 2:
            strComando = f"""SELECT sigla FROM {configs.tblEstados} WHERE extenso = '{args[0]}'"""
        else:
            strComando = f"""SELECT extenso FROM {configs.tblEstados} WHERE sigla = '{args[0]}'"""
    else:
        strComando = f"""SELECT extenso FROM {configs.tblEstados} ORDER BY extenso"""

    cursor.execute(strComando)

    return [estado[0] for estado in cursor.fetchall()]


def cadastreUsuario(usuario):
    configs = ConfigDB()

    connection = pymysql.connect(
        host=configs.host,
        user=configs.user,
        passwd=configs.passwd,
        db=configs.banco
    )
    cursor = connection.cursor()

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
        connection.commit()
        connection.close()
        return True
    except:
        raise Exception(f'Erro SQL - cadastreUsuario({usuario.userId}) <CREATE TABLE>')


def buscaUsuario(strUsuario):
    configs = ConfigDB()

    connection = pymysql.connect(
        host=configs.host,
        user=configs.user,
        passwd=configs.passwd,
        db=configs.banco
    )
    cursor = connection.cursor()

    strComando = f"""
                SELECT * 
                FROM {configs.tblUsuario}
                WHERE 
                    nomeUsuario = '{strUsuario}'
                OR
                    email = '{strUsuario}'
                OR
                    nomeEmpresa = '{strUsuario}'
                OR
                    cnpj = '{strUsuario}'
                """

    cursor.execute(strComando)

    if cursor.fetchone() is None:
        return False
    else:
        return True


def confereSenha(strUsuario, password):
    configs = ConfigDB()

    connection = pymysql.connect(
        host=configs.host,
        user=configs.user,
        passwd=configs.passwd,
        db=configs.banco
    )
    cursor = connection.cursor()

    strComando = f'''
                SELECT senha 
                FROM {configs.tblUsuario}
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
        raise Exception(f'Erro SQL - confereSenha({configs.tblUsuario}) <SELECT>')

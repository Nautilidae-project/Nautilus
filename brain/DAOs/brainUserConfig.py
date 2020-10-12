import sqlite3
from os.path import join, dirname
from os import listdir


def criaBanco(nomeBanco):
    conn = sqlite3.connect(join(dirname(__file__), f'{nomeBanco}.db'))
    cursor = conn.cursor()

    strComando = """CREATE TABLE IF NOT EXISTS usuario(
	                    userId INTEGER PRIMARY KEY AUTOINCREMENT,
                        nomeUsuario VARCHAR(20) NOT NULL,
                        nomeEmpresa VARCHAR(30) NOT NULL,
                        nomeFantasia VARCHAR(30) NULL,
                        cnpj VARCHAR(15) NOT NULL,
                        email VARCHAR(30) NOT NULL,
                        tel INTEGER NOT NULL,
                        endereco VARCHAR(30) NOT NULL,
                        cep INTEGER NOT NULL,
                        senha VARBINARY(80) NOT NULL
                    );"""

    try:
        cursor.executescript(strComando)
        conn.commit()
        return True
    except:
        raise Exception(f'Erro SQL - criaBanco({nomeBanco}) <CREATE TABLE>')
    # finally:
    #     return False


def cadastreUsuario(usuario):
    try:
        criaBanco(usuario.nomeEmpresa)
    except:
        return False

    conn = sqlite3.connect(join(dirname(__file__), f'{usuario.nomeEmpresa}.db'))
    cursor = conn.cursor()

    strComando = f'''
        INSERT INTO usuario
        (
             nomeUsuario, nomeEmpresa, nomeFantasia,
             cnpj, email, tel,
             endereco, cep, senha                       
        )
        VALUES
        (
            'Sem nome', '{usuario.nomeEmpresa}', '{usuario.nomeFantasia}',
            '{usuario.cnpj}', '{usuario.email}', {usuario.tel},
            '{usuario.endereco}', {usuario.cep}, '{usuario.senha}'          
        )
        '''
    try:
        cursor.executescript(strComando)
        conn.commit()
        return True
    except:
        raise Exception(f'Erro SQL - cadastreUsuario({usuario.userId}) <CREATE TABLE>')
    # finally:
    #     return False


def buscaBanco(nomeBanco):
    listCurrentDir = listdir(dirname(__file__))
    for dir in listCurrentDir:
        if dir.endswith('.db'):
            if dir[:len(dir) - 3] == nomeBanco:
                return True
    print(f'Nenhum banco de dados com o nome {nomeBanco} listado')
    return False

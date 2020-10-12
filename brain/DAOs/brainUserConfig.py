import sqlite3
from os.path import join, dirname
from os import listdir
from bcrypt import checkpw


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
                        cep VARCHAR(8) NOT NULL,
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
        criaBanco(usuario.nomeUsuario)
    except:
        return False

    conn = sqlite3.connect(join(dirname(__file__), f'{usuario.nomeUsuario}.db'))
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
            '{usuario.nomeUsuario}', '{usuario.nomeEmpresa}', '{usuario.nomeFantasia}',
            '{usuario.cnpj}', '{usuario.email}', {usuario.tel},
            '{usuario.endereco}', '{usuario.cep}', '{usuario.senha}'          
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

def confereSenha(banco, password):

    conn = sqlite3.connect(join(dirname(__file__), f'{banco}.db'))
    cursor = conn.cursor()

    strComando = f'''
        SELECT senha FROM usuario;
    '''

    cursor.execute(strComando)

    senha = cursor.fetchone()[0]

    return checkpw(password.encode('utf-8'), senha.encode('utf-8'))

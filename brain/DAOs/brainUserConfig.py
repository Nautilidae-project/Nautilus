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

def criaBancoEstados():
    conn = sqlite3.connect(join(dirname(__file__), 'estados.db'))
    cursor = conn.cursor()

    strComando = """CREATE TABLE IF NOT EXISTS estados(
                    estados VARCHAR(20) NOT NULL);"""

    cursor.executescript(strComando)


def addEstados():
    conn = sqlite3.connect(join(dirname(__file__), 'estados.db'))
    cursor = conn.cursor()

    listaEstados = {
        'Acre',
        'Alagoas',
        'Amapá',
        'Amazonas',
        'Bahia',
        'Ceará',
        'Distrito Federal',
        'Espírito Santo',
        'Goiás',
        'Maranhão',
        'Mato Grosso',
        'Mato Grosso do Sul',
        'Minas Gerais',
        'Pará',
        'Paraíba',
        'Paraná',
        'Pernambuco',
        'Piauí',
        'Rio de Janeiro',
        'Rio Grande do Norte',
        'Rio Grande do Sul',
        'Rondônia',
        'Roraima',
        'Santa Catarina',
        'São Paulo',
        'Sergipe',
        'Tocantins'
    }

    for estado in listaEstados:
        strComando = f"""INSERT INTO estados (estados) VALUES ('{estado}')"""
        cursor.executescript(strComando)


def getEstados():
    listaEstados = []
    conn = sqlite3.connect(join(dirname(__file__), 'estados.db'))
    cursor = conn.cursor()

    strComando = cursor.execute(f"""SELECT estados From estados""")

    for estado in strComando:
        listaEstados.append(estado[0])

    return listaEstados


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

# criaBanco('Renan')
# criaBancoEstados()
# addEstados()
def confereSenha(banco, password):

    conn = sqlite3.connect(join(dirname(__file__), f'{banco}.db'))
    cursor = conn.cursor()

    strComando = f'''
        SELECT senha FROM usuario;
    '''

    cursor.execute(strComando)

    senha = cursor.fetchone()[0]

    return checkpw(password.encode('utf-8'), senha.encode('utf-8'))

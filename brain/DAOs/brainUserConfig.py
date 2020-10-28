import sqlite3
from os.path import join, dirname
from os import listdir
from bcrypt import checkpw
from modelos.estadosModelo import EstadosModelo


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


def criaBancoEstados():
    conn = sqlite3.connect(join(dirname(__file__), 'estados.db'))
    cursor = conn.cursor()

    strComando = """CREATE TABLE IF NOT EXISTS estados(
                    extenso VARCHAR(20) NOT NULL,
                    sigla VARCHAR(2) NOT NULL
                    );"""

    cursor.executescript(strComando)


def addEstados():
    conn = sqlite3.connect(join(dirname(__file__), 'estados.db'))
    cursor = conn.cursor()

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
        cursor.executescript(strComando)
    return True


def getEstados():
    conn = sqlite3.connect(join(dirname(__file__), 'estados.db'))
    cursor = conn.cursor()

    listaEstados = cursor.execute(f"""SELECT extenso FROM estados ORDER BY extenso""")

    return [estado[0] for estado in listaEstados]


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

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
                        tel INT NOT NULL,
                        endereco VARCHAR(30) NOT NULL,
                        cep INT NOT NULL,
                        senha VARCHAR(20)
                    );"""

    cursor.executescript(strComando)

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


def buscaBanco(nomeBanco):
    listCurrentDir = listdir(dirname(__file__))
    for dir in listCurrentDir:
        if dir.endswith('.db'):
            if dir[:len(dir)-3] == nomeBanco:
                return True
    print(f'Nenhum banco de dados com o nome {nomeBanco} listado')
    return False

# criaBanco('Renan')
# criaBancoEstados()
# addEstados()

from configBD import ConfigDB
import pymysql

def cadastraCliente(cliente):
    configs = ConfigDB()

    connection = pymysql.connect(
        host=configs.host,
        user=configs.user,
        passwd=configs.passwd,
        db=configs.banco
    )
    print(cliente)

    cursor = connection.cursor()

    strComando = f"""
        INSERT INTO cliente
        (
            nomeCliente, sobrenomeCliente, telefone,
            email, cpf, endereco, complemento , cep, bairro,
            meioPagamento, ativo, dataCadastro, dataUltAlt
        )
        VALUES
        (
            '{cliente.nomeCliente}', '{cliente.sobrenomeCliente}', '{cliente.telefone}',
            '{cliente.email}', '{cliente.cpf}', '{cliente.endereco}', '{cliente.complemento}', '{cliente.cep}',
            '{cliente.bairro}', 'CC', {cliente.ativo}, NOW(), NOW()
)
        """
    try:
        cursor.execute(strComando)
        connection.commit()
        connection.close()
    except:
        raise Warning(f'Erro SQL - insereCliente({cliente.clienteId}) <INSERT>')

def findAll():
    configs = ConfigDB()

    connection = pymysql.connect(
        host=configs.host,
        user=configs.user,
        passwd=configs.passwd,
        db=configs.banco
    )

    cursor = connection.cursor()

    # strComando = f"SELECT * FROM {configs.tblCliente}"
    strComando = f"SELECT nomeCliente, telefone, meioPagamento, ativo FROM {configs.tblCliente}"

    cursor.execute(strComando)

    return cursor.fetchall()
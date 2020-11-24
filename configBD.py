class ConfigDB:
    def __init__(self):
        self.__host = 'localhost'
        self.__user = 'NAUTILUS'
        self.__passwd = '!Nautilidae2020!'
        self.__banco = 'NAUTILIDAE'
        self.__tblUsuario = 'usuario'
        self.__tblEstados = 'estados'
        self.__tblCliente = 'cliente'
        self.__sqlCreateUsuario = f"""CREATE TABLE IF NOT EXISTS {self.tblUsuario}(
	                    userId INT AUTO_INCREMENT,
                        nomeUsuario VARCHAR(20) NOT NULL,
                        nomeEmpresa VARCHAR(30) NOT NULL,
                        nomeFantasia VARCHAR(30) NULL,
                        cnpj VARCHAR(15) NOT NULL,
                        email VARCHAR(40) NOT NULL,
                        tel VARCHAR(11) NOT NULL,
                        endereco VARCHAR(30) NOT NULL,
                        complemento VARCHAR(30) NULL, 
                        cep VARCHAR(8) NOT NULL,
                        bairro VARCHAR(30) NULL,
                        senha VARBINARY(80) NOT NULL,
                        dataCadastro DATETIME NOT NULL,
                        PRIMARY KEY (userId)
                    );"""
        self.__sqlCreateEstado = f"""CREATE TABLE IF NOT EXISTS {self.tblEstados}(
                        extenso VARCHAR(20) NOT NULL,
                        sigla VARCHAR(2) NOT NULL
                        );"""
        self.__sqlCreateCliente = f"""CREATE TABLE IF NOT EXISTS {self.tblCliente}(
	                    clienteId INT AUTO_INCREMENT,
                        nomeCliente VARCHAR(20) NOT NULL,
                        sobrenomeCliente VARCHAR(30) NOT NULL,
                        telefone VARCHAR(30) NULL,
                        email VARCHAR(40) NOT NULL,
                        cpf VARCHAR(11) NULL,
                        endereco VARCHAR(30) NOT NULL,
                        complemento VARCHAR(30) NULL, 
                        cep VARCHAR(8) NOT NULL,
                        bairro VARCHAR(30) NULL,
                        meioPagamento VARCHAR(2) DEFAULT 'CC',
                        ativo BIT(1) DEFAULT 1,
                        dataCadastro DATETIME NOT NULL,
                        dataUltAlt DATETIME NOT NULL,
                        PRIMARY KEY (clienteId)
                    );"""

    @property
    def sqlCreateUsuario(self):
        return self.__sqlCreateUsuario

    @property
    def sqlCreateEstado(self):
        return self.__sqlCreateEstado

    @property
    def sqlCreateCliente(self):
        return self.__sqlCreateCliente

    @property
    def host(self):
        return self.__host

    @property
    def user(self):
        return self.__user

    @property
    def passwd(self):
        return self.__passwd

    @property
    def banco(self):
        return self.__banco

    @property
    def tblUsuario(self):
        return self.__tblUsuario

    @property
    def tblEstados(self):
        return self.__tblEstados

    @property
    def tblCliente(self):
        return self.__tblCliente

    def __repr__(self):
        return f'''
                   host: {self.__host}
                   user: {self.__user}
                   passwd: {self.__passwd[:3]}
                   banco: {self.__banco}
                   tabela usuário: {self.__tblUsuario}
                   tabela estados: {self.__tblEstados}'''
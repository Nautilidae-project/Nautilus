class ConfigDB:
    def __init__(self):
        self.__host = 'mysql742.umbler.com' #localhost
        self.__user = 'nautilus' #NAUTILUS
        self.__passwd = 'Nautilidae2020' #!Nautilidae2020!
        self.__banco = 'nautilus' #NAUTILIDAE
        self.__port = 41890
        self.__tblUsuario = 'usuario'
        self.__tblEstados = 'estados'
        self.__tblCliente = 'cliente'
        self.__tblEvento = 'evento'
        self.__tblParticipantes = 'participantes'
        self.__tblGrupo = 'grupo'
        self.__tblCategoria = 'categoria'

        # Comando SQL para criar tabela de usuários
        self.__sqlCreateUsuario = f"""CREATE TABLE IF NOT EXISTS {self.tblUsuario}(
	                    userId INT AUTO_INCREMENT,
                        nomeUsuario VARCHAR(20) NOT NULL,
                        nomeEmpresa VARCHAR(30) NOT NULL,
                        nomeFantasia VARCHAR(30) NULL,
                        cnpj VARCHAR(15) NOT NULL,
                        email VARCHAR(40) NOT NULL,
                        tel VARCHAR(11) NOT NULL,
                        endereco VARCHAR(30) NOT NULL,
                        cidade VARCHAR(30) NULL,
                        complemento VARCHAR(30) NULL, 
                        cep VARCHAR(8) NOT NULL,
                        bairro VARCHAR(30) NULL,
                        senha VARBINARY(80) NOT NULL,
                        dataCadastro DATETIME NOT NULL,
                        PRIMARY KEY (userId)
                    );"""

        # Comando SQL para criar tabela de Estados
        self.__sqlCreateEstado = f"""CREATE TABLE IF NOT EXISTS {self.tblEstados}(
                        extenso VARCHAR(20) NOT NULL,
                        sigla VARCHAR(2) NOT NULL
                        );"""

        # Comando SQL para criar tabela de clientes
        self.__sqlCreateCliente = f"""CREATE TABLE IF NOT EXISTS {self.tblCliente}(
	                    clienteId INT AUTO_INCREMENT,
                        nomeCliente VARCHAR(20) NOT NULL,
                        sobrenomeCliente VARCHAR(30) NOT NULL,
                        telefone VARCHAR(11) NULL,
                        email VARCHAR(40) NOT NULL,
                        cpf VARCHAR(11) NULL,
                        endereco VARCHAR(50) NOT NULL,
                        complemento VARCHAR(30) NULL, 
                        cep VARCHAR(8) NOT NULL,
                        bairro VARCHAR(30) NULL,
                        meioPagamento VARCHAR(2) DEFAULT 'CC',
                        ativo BIT(1) DEFAULT 1,
                        dataCadastro DATETIME NOT NULL,
                        dataUltAlt DATETIME NOT NULL,
                        PRIMARY KEY (clienteId)
                    );"""

        # Comando SQL para criar tabela de eventos
        self.__sqlCreateEvento = f"""CREATE TABLE IF NOT EXISTS {self.tblEvento} (		
                        eventoId INT AUTO_INCREMENT,
                        titulo VARCHAR(19) NOT NULL,
                        detalhe VARCHAR(500) NULL,
                        grupoId INT NULL,
                        dataEvento DATETIME NOT NULL,
                        dataCadastro DATETIME NOT NULL,
                        horaInicio DATETIME NULL,
                        horaFim DATETIME NULL,
                        diaInteiro BOOL NOT NULL DEFAULT FALSE,
                        PRIMARY KEY (eventoId)
                    );"""

        # Comando SQL para criar tabela de participantes de um evento
        self.__sqlCreateParticipantes = f"""CREATE TABLE IF NOT EXISTS {self.tblParticipantes} (
                        Id INT AUTO_INCREMENT,
                        eventoId INT NOT NULL,
                        clienteId INT NOT NULL,
                        PRIMARY KEY (Id)
                    );"""

        # Comando SQL para criar tabela de grupos
        self.__sqlCreateGrupo = f"""CREATE TABLE IF NOT EXISTS {self.tblGrupo} (
                        grupoId INT AUTO_INCREMENT,
                        titulo VARCHAR(30) NOT NULL,
                        descricao VARCHAR(700) NULL,
                        categoria VARCHAR(30) NULL,
                        dataCadastro DATETIME NOT NULL,
                        dataUltAlt DATETIME NOT NULL,
                        PRIMARY KEY (grupoId)
                    );"""

        # Comando SQL para criar tabela de categorias
        self.__sqlCreateCategoria = f"""CREATE TABLE IF NOT EXISTS {self.tblCategoria} (
                                categoriaId INT AUTO_INCREMENT,
                                nome VARCHAR(30) NOT NULL,
                                PRIMARY KEY (categoriaId)
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
    def sqlCreateEvento(self):
        return self.__sqlCreateEvento

    @property
    def sqlCreateParticipantes(self):
        return self.__sqlCreateParticipantes

    @property
    def sqlCreateGrupo(self):
        return self.__sqlCreateGrupo

    @property
    def sqlCreateCategoria(self):
        return self.__sqlCreateCategoria

    @property
    def host(self):
        return self.__host

    @property
    def port(self):
        return self.__port

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

    @property
    def tblEvento(self):
        return self.__tblEvento

    @property
    def tblParticipantes(self):
        return self.__tblParticipantes

    @property
    def tblGrupo(self):
        return self.__tblGrupo

    @property
    def tblCategoria(self):
        return self.__tblCategoria


    def __repr__(self):
        return f'''
                   host: {self.__host}
                   user: {self.__user}
                   passwd: {self.__passwd[:3]}
                   banco: {self.__banco}
                   tabela usuário: {self.__tblUsuario}
                   tabela estados: {self.__tblEstados}'''
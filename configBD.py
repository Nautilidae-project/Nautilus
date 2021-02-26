import json
import os

class ConfigDB:

    def __init__(self, carregaBanco=False):

        self.__host = None
        self.__user = None
        self.__passwd = None
        self.__banco = None
        self.__port = None

        if carregaBanco:
            # Servidores Local e Cloud
            # self.getDatabase('Cloud')
            self.getDatabase('Local')

        self.__tblUsuario = 'usuario'
        self.__tblEstados = 'estados'
        self.__tblCliente = 'cliente'
        self.__tblEvento = 'evento'
        self.__tblParticipantes = 'participantes'
        self.__tblGrupo = 'grupo'
        self.__tblCategoria = 'categoria'
        self.__tblPlanos = 'planos'
        self.__tblPagamentos = 'pagamentos'

        # Comando SQL para criar tabela de usuários
        self.__sqlCreateUsuario = f"""CREATE TABLE IF NOT EXISTS {self.tblUsuario}(
	                    userId INT AUTO_INCREMENT,
                        nomeUsuario VARCHAR(20) NOT NULL,
                        nomeEmpresa VARCHAR(30) NOT NULL,
                        nomeFantasia VARCHAR(30) NULL,
                        caminhoLogo VARCHAR(120) NULL,
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
                        dataUltAlt DATETIME NOT NULL,
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
                        plano VARCHAR(20) NULL,
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
                        eventoId INT NULL,
                        grupoId INT NULL,
                        clienteId INT NOT NULL,
                        PRIMARY KEY (Id)
                    );"""

        # Comando SQL para criar tabela de grupos
        self.__sqlCreateGrupo = f"""
                CREATE TABLE IF NOT EXISTS {self.tblGrupo} (
                    grupoId INT AUTO_INCREMENT,
                    titulo VARCHAR(30) NOT NULL,
                    descricao VARCHAR(700) NULL,
                    categoria VARCHAR(30) NULL,
                    dataCadastro DATETIME NOT NULL,
                    dataUltAlt DATETIME NOT NULL,
                    PRIMARY KEY (grupoId)
                );"""

        # Comando SQL para criar tabela de categorias
        self.__sqlCreateCategoria = f"""
                CREATE TABLE IF NOT EXISTS {self.tblCategoria} (
                    nome VARCHAR(30) NOT NULL,
                    cor VARCHAR(7) NOT NULL,
                    PRIMARY KEY (nome)
                );"""

        # Comando SQL para criar tabela de planos
        self.__sqlCreatePlanos = f"""
                CREATE TABLE IF NOT EXISTS {self.tblPlanos} (
                    planoId INT AUTO_INCREMENT NOT NULL,
                    nomePlano VARCHAR(30) NOT NULL,
                    valor FLOAT NOT NULL,
                    descricao VARCHAR(500) NOT NULL,
                    periodoUnidade VARCHAR(10) NOT NULL,
                    qtdInscritos INT NOT NULL DEFAULT 0,
                    dataInicio DATETIME NOT NULL,
                    dataFim DATETIME NOT NULL,
                    dataCadastro DATETIME NOT NULL,
                    dataUltAlt DATETIME NOT NULL,
                    presencial BOOL NOT NULL DEFAULT FALSE,
                    ativo BOOL NOT NULL DEFAULT TRUE,
                    PRIMARY KEY (planoId)
                );"""

        # Comando SQL para criar tabela de pagamentos
        self.__sqlCreatePagamentos = f"""
                       CREATE TABLE IF NOT EXISTS {self.tblPagamentos} (
                           pagId INT AUTO_INCREMENT NOT NULL,
                           clientId INT NOT NULL,
                           planoId INT NOT NULL,
                           valorPlano FLOAT NOT NULL,
                           valorRecebido FLOAT NULL,
                           formaPagamento VARCHAR(15) NOT NULL,
                           dataVencimento DATETIME NOT NULL,
                           dataPagamento DATETIME NULL,
                           situacao VARCHAR(20) NOT NULL,
                           dataCadastro DATETIME NOT NULL,
                           PRIMARY KEY (pagId)
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
    def sqlCreatePlanos(self):
        return self.__sqlCreatePlanos

    @property
    def sqlCreatePagamentos(self):
        return self.__sqlCreatePagamentos

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

    @property
    def tblPlanos(self):
        return self.__tblPlanos

    @property
    def tblPagamentos(self):
        return self.__tblPagamentos

    def getDatabase(self, servidor: str):
        dataSourcesDir = os.path.join(os.path.dirname(__file__), 'datasources')
        if servidor == 'Local':
            dbPath = os.path.join(dataSourcesDir, 'databaseLocal.json')
        else:
            dbPath = os.path.join(dataSourcesDir, 'databaseCloud.json')


        with open(dbPath) as arquivo:
            config = json.load(arquivo)
            self.__host = config['host']
            self.__user = config['user']
            self.__passwd = config['passwd']
            self.__banco = config['banco']
            self.__port = int(config['port'])
            arquivo.close()

    def __repr__(self):
        return f'''
                   host: {self.__host}
                   user: {self.__user}
                   passwd: {self.__passwd[:3]}
                   banco: {self.__banco}
                   tabela usuário: {self.__tblUsuario}
                   tabela estados: {self.__tblEstados}'''
class ConfigDB:
    def __init__(self):
        self.__host = 'localhost'
        self.__user = 'NAUTILUS'
        self.__passwd = '!Nautilidae2020!'
        self.__banco = 'NAUTILIDAE'
        self.__tblUsuario = 'usuario'
        self.__tblEstados = 'estados'

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

    def __repr__(self):
        return f'''
                   host: {self.__host}
                   user: {self.__user}
                   passwd: {self.__passwd[:3]}
                   banco: {self.__banco}
                   tabela usuário: {self.__tblUsuario}
                   tabela estados: {self.__tblEstados}'''
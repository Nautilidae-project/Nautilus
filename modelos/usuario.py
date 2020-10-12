
class Usuario:

    def __init__(self):
        self.userId = None
        self.nomeUsuario = None
        self.nomeEmpresa = None
        self.nomeFantasia = None
        self.cnpj = None
        self.email = None
        self.tel = None
        self.endereco = None
        self.cep = None
        self.senha = None

    def __repr__(self):
        return f'Usuario(userId: {self.userId}, nomeUsuario: {self.nomeUsuario}, nomeEmpresa: {self.nomeEmpresa}, ' \
               f'nomeFantasia: {self.nomeFantasia}), cnpj: {self.cnpj}, email: {self.email}, tel: {self.tel}, ' \
               f'endereco: {self.endereco}, cep: {self.cep}, senha: ***** '
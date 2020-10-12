
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

    def toDict(self):
        dictUsuario = {
            'userId': self.userId,
            'nomeUsuario': self.nomeUsuario,
            'nomeEmpresa': self.nomeEmpresa,
            'nomeFantasia': self.nomeFantasia,
            'cnpj': self.cnpj,
            'email': self.email,
            'tel': self.tel,
            'endereco': self.endereco,
            'cep': self.cep,
            'senha': self.senha
        }
        return dictUsuario

    def fromDict(self, dictUsuario):
        self.userId = dictUsuario['userId']
        self.nomeUsuario = dictUsuario['nomeUsuario']
        self.nomeEmpresa = dictUsuario['nomeEmpresa']
        self.nomeFantasia = dictUsuario['nomeFantasia']
        self.cnpj = dictUsuario['cnpj']
        self.email = dictUsuario['email']
        self.tel = dictUsuario['tel']
        self.endereco = dictUsuario['endereco']
        self.cep = dictUsuario['cep']
        self.senha = dictUsuario['senha']

    def __repr__(self):
        return f'Usuario(userId: {self.userId}, nomeUsuario: {self.nomeUsuario}, nomeEmpresa: {self.nomeEmpresa}, ' \
               f'nomeFantasia: {self.nomeFantasia}, cnpj: {self.cnpj}, email: {self.email}, tel: {self.tel}, ' \
               f'endereco: {self.endereco}, cep: {self.cep}, senha: {self.senha}'
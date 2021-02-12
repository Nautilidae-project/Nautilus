
class UsuarioModel:

    def __init__(self):
        self.userId = None
        self.nomeUsuario = None
        self.nomeEmpresa = None
        self.nomeFantasia = None
        self.cnpj = None
        self.email = None
        self.tel = None
        self.endereco = None
        self.cidade = None
        self.cep = None
        self.bairro = None
        self.complemento = None
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
            'cidade': self.cidade,
            'cep': self.cep,
            'senha': self.senha
        }
        return dictUsuario

    def fromDict(self, dictUsuario: dict):
        self.userId = dictUsuario['userId']
        self.nomeUsuario = dictUsuario['nomeUsuario']
        self.nomeEmpresa = dictUsuario['nomeEmpresa']
        self.nomeFantasia = dictUsuario['nomeFantasia']
        self.cnpj = dictUsuario['cnpj']
        self.email = dictUsuario['email']
        self.tel = dictUsuario['tel']
        self.endereco = dictUsuario['endereco']
        self.cidade = dictUsuario['cidade']
        self.cep = dictUsuario['cep']
        self.senha = dictUsuario['senha']

        return self

    def fromList(self, usuarioList: list):
        self.userId = usuarioList[0]
        self.nomeUsuario = usuarioList[1]
        self.nomeEmpresa = usuarioList[2]
        self.nomeFantasia = usuarioList[3]
        self.caminhoLogo = usuarioList[4]
        self.cnpj = usuarioList[5]
        self.email = usuarioList[6]
        self.tel = usuarioList[7]
        self.endereco = usuarioList[8]
        self.cep = usuarioList[9]
        self.senha = usuarioList[10]

        return self

    def __repr__(self):
        return f"""Usuario(userId: {self.userId}, nomeUsuario: {self.nomeUsuario}, nomeEmpresa: {self.nomeEmpresa}, 
                    nomeFantasia: {self.nomeFantasia}, caminhoLogo: {self.caminhoLogo}, cnpj: {self.cnpj}, 
                    email: {self.email}, tel: {self.tel}, endereco: {self.endereco}, cep: {self.cep}, senha: {self.senha})"""
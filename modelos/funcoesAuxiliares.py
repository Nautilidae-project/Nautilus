def mascaraCelular(celular):
    return f'({celular[0:2]}) {celular[2:3]}.{celular[3:7]}-{celular[7:]}'

def mascaraCNPJ(cnpj):
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'

def mascaraCep(cep):
    return f'{cep[:5]}-{cep[5:]}'
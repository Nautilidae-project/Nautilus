class EstadosModelo:
    def __init__(self):
        self.__estados = {
        'Acre': 'AC',
        'Alagoas': 'AL',
        'Amapá': 'AP',
        'Amazonas': 'AM',
        'Bahia': 'BA',
        'Ceará': 'CE',
        'Distrito Federal': 'DF',
        'Espírito Santo': 'ES',
        'Goiás': 'GO',
        'Maranhão': 'MA',
        'Mato Grosso': 'MT',
        'Mato Grosso do Sul': 'MS',
        'Minas Gerais': 'MG',
        'Pará': 'PA',
        'Paraíba': 'PB',
        'Paraná': 'PR',
        'Pernambuco': 'PE',
        'Piauí': 'PI',
        'Rio de Janeiro': 'RJ',
        'Rio Grande do Norte': 'RN',
        'Rio Grande do Sul': 'RS',
        'Rondônia': 'RO',
        'Roraima': 'RR',
        'Santa Catarina': 'SC',
        'São Paulo': 'SP',
        'Sergipe': 'SE',
        'Tocantins' : 'TO'
    }


    def toDict(self):
        return self.__estados

    def __repr__(self):
        return '''
        Acre: AC,\n
        Alagoas: AL,\n
        Amapá: AP,\n
        Amazonas: AM,\n
        Bahia: BA,\n
        Ceará: CE,\n
        Distrito Federal: DF,\n
        Espírito Santo: ES,\n
        Goiás: GO,\n
        Maranhão: MA,\n
        Mato Grosso: MT,\n
        Mato Grosso do Sul: MS,\n
        Minas Gerais: MG,\n
        Pará: PA,\n
        Paraíba: PB,\n
        Paraná: PR,\n
        Pernambuco: PE,\n
        Piauí: PI,\n
        Rio de Janeiro: RJ,\n
        Rio Grande do Norte: RN,\n
        Rio Grande do Sul: RS,\n
        Rondônia: RO,\n
        Roraima: RR,\n
        Santa Catarina: SC,\n
        São Paulo: SP,\n
        Sergipe: SE\n
        Tocantins : TO\n'''
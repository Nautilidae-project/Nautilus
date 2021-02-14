from configBD import ConfigDB
from modelos.eventoModel import EventoModelo


class DaoPlanos:

    def __init__(self, db):
        self.db = db
        self.configs = ConfigDB()


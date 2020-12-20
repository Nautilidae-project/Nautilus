import pymysql

from configBD import ConfigDB


class DaoParticipantes():

    def __init__(self):
        self.configs = ConfigDB()

        self.connection = pymysql.connect(
            host=self.configs.host,
            user=self.configs.user,
            passwd=self.configs.passwd,
            db=self.configs.banco
        )

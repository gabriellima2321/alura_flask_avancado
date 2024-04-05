class DBInfo():
    def __init__(self):
        self._dbj = 'mysql'
        self._username = 'root'
        self._password = 'rcvry'
        self._host = 'localhost'
        self._schema = 'jogoteca'

    def __str__(self):
        return f'{self._dbj}://{self._username}:{self._password}@{self._host}/{self._schema}'
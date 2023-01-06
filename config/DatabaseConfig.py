DB_USERNAME = ''
DB_PASSWORD = ''
DB_HOST = ''
DB_SCHEMA = ''
DB_PORT = ''

SQLALCHEMY_TRACK_MODIFICATIONS = False

def getURI():
    return 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USERNAME, DB_PASSWORD,
                                                                DB_HOST, DB_PORT, DB_SCHEMA)
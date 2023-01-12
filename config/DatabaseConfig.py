DB_USERNAME = ''
DB_PASSWORD = ''
DB_HOST = ''
DB_SCHEMA = ''
DB_PORT = ''

def getURI():
    return 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USERNAME, DB_PASSWORD,
                                                                DB_HOST, DB_PORT, DB_SCHEMA)
SQLALCHEMY_DATABASE_URI = getURI()
SQLALCHEMY_TRACK_MODIFICATIONS = False
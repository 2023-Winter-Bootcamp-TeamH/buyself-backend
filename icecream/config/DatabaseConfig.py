DB_USERNAME = 'Junsu'
DB_PASSWORD = 'qkrwnstn012'
DB_HOST = 'mydbinstance.chqyfsatxj72.us-east-1.rds.amazonaws.com'
DB_SCHEMA = 'icecreamysql'
DB_PORT = '3306'

SQLALCHEMY_TRACK_MODIFICATIONS = False


def getURI():
    return 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USERNAME, DB_PASSWORD,
                                                                DB_HOST, DB_PORT, DB_SCHEMA)
SQLALCHEMY_DATABASE_URI = getURI()
SQLALCHEMY_TRACK_MODIFICATIONS = False
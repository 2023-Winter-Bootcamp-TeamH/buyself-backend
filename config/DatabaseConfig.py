import os

DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_SCHEMA = os.environ.get('DB_SCHEMA')
DB_PORT = os.environ.get('DB_PORT')

def getURI():
    return 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USERNAME, DB_PASSWORD,
                                                                DB_HOST, DB_PORT, DB_SCHEMA)
SQLALCHEMY_DATABASE_URI = getURI()
SQLALCHEMY_TRACK_MODIFICATIONS = False
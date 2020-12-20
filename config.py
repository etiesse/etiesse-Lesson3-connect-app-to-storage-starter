import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'server-west-database.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'west-database'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'lesson3admin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'AdminLesson3'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'exolesson3'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'UWbqnk2+qmnnhDxF1OpOaTsfYlyE2Tafjyh8FctxdeFW/YgbkXz1D2tH1Di15lkZog98BPOLS4D8GsGfOsuhVQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images003'

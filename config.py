import os 
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY =  os.environ.get('SECRET_KEY') or 'you-will-never-guess'


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    # SQL Server connection string for localhost
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or (
        "mssql+pyodbc://sqladmin:password123@localhost/empDB"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False  

class ProductionConfig(Config):

    def __init__(self):
        super().__init__()
    
    DEBUG = False
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


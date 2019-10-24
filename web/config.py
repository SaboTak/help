# config.py


import os


class BaseConfig(object):
    SECRET_KEY ='seb'
    DEBUG = 'True'
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']
    DB_SERVICE = os.environ['DB_SERVICE']
    DB_PORT = os.environ['DB_PORT']
    FLASK_ENV='development'
    DATABASE_URL= 'postgres://eitubfyrpusaqp:702bc447eb316d1fbc59d18ed937783fc4e9bcdd21889cf3f96e01d3e6d745b2@ec2-50-19-221-38.compute-1.amazonaws.com:5432/d4thqinpmk7a8d'
    SQLALCHEMY_DATABASE_URI = 'postgres://eitubfyrpusaqp:702bc447eb316d1fbc59d18ed937783fc4e9bcdd21889cf3f96e01d3e6d745b2@ec2-50-19-221-38.compute-1.amazonaws.com:5432/d4thqinpmk7a8d'


# class BaseConfig(object):
#     SECRET_KEY = 'hi'
#     DEBUG = True
#     DB_NAME = 'postgres'
#     DB_SERVICE = 'localhost'
#     DB_PORT = 5432
#     SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}/{2}'.format(
#         DB_SERVICE, DB_PORT, DB_NAME
#     )

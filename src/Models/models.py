from peewee import *

#db = SqliteDatabase('teste_vinny.bd')

from playhouse.pool import PooledPostgresqlExtDatabase

db = PooledPostgresqlExtDatabase(
        'pokemon',
        max_connections=8,
        stale_timeout=60,  # 1 minutes.
        user='postgres',
        password='example'
    )

class BaseModel(Model):
    class Meta:
        database = db


class Habilidade(BaseModel):
    AP = IntegerField()
    tipo = CharField(max_length=50)
    nome = CharField(max_length=50)
    desc = CharField(max_length=50)

class Pokemon(BaseModel):
    num_id = IntegerField()
    nome = CharField(max_length=50)
    tipo_1 = CharField(max_length=50)
    tipo_2 = CharField(max_length=50,null=False)
    skill = ForeignKeyField(Habilidade)

# @app.before_request
# def before_request():
#     database.connect()

# @app.after_request
# def after_request(response):
#     database.close()
#     return response

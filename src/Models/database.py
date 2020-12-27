from src.Models.models import *
from typing import NewType


def criar_tabelas():
    db.connect()
    db.create_tables(
        [
            Pokemon,
            Habilidade
        ]
    )
    db.close()

def popular_habilitade(hab):
    print(f'poke: {hab}')
    db.connect()
    hab.save()
    db.close()

def popular_pokemon(poke):
    print(f'skill: {poke}')
    db.connect()
    poke.save()
    db.close()

def destroi_tabela():
    db.connect()
    db.drop_tables(
        [
            Pokemon,
            Habilidade
        ]
    )
    db.close()
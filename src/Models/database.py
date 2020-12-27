from src.Models.models import *
from typing import NewType
from src.Models.models import Pokemon,Habilidade


def criar_tabelas():
    db.connect()
    db.create_tables(
        [
            Pokemon,
            Habilidade
        ]
    )
    db.close()

def popular_habilidade(hab):
    #print(f'poke: {hab}')
    #db.connect()
    #hab.save()
    #db.close()
    db.connect()
    for index,num_move in enumerate(hab):
        habilidade = Habilidade(
            id=int(index)+1,
            nome=hab[num_move][0],
            tipo=hab[num_move][1],
            #kind=hab[num_move][3],
            #power=hab[num_move][4]
            #accuracy=hab[num_move][5]
            AP=hab[num_move][5],
            desc='batata'
        )      
        habilidade.save(force_insert=True)
        #pokemon.save()
    # print(pokemon.nome)
    db.close()

def popular_pokemon(poke): #Dataframe
    db.connect()
    for index,num_poke in enumerate(poke):
        pokemon = Pokemon(
            id=int(index)+1,
            nome=poke[num_poke][1],
            tipo_1=poke[num_poke][2],
            tipo_2=poke[num_poke][3],
            skill_id=1
        )
        pokemon.save(force_insert=True)
        #pokemon.save()
    # print(pokemon.nome)
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

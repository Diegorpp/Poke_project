from src.Models import database,models
from src.Models.models import Habilidade,Pokemon
import pandas as pd

if __name__ == "__main__":
#    skill_a = Habilidade(
#        AP=60,
#        tipo='Normal',
#        nome='fast attack',
#        desc='Habilidade pica que bate rapidao brabamente'
#    )
    
    database.destroi_tabela()
    print('Tabelas destruidas')

    database.criar_tabelas()
    print('Criar tabelas')

#    database.popular_habilidade(skill_a)
#    print('Tabela skill populada')

    df = pd.read_csv('C:/Users/Coud/Documents/Projetos/CRUD/Poke_project/src/Utilts/moves.csv', sep = ',', encoding="ISO-8859-1")
    dic_moves = df.set_index('#').T.to_dict('list')
    database.popular_habilidade(dic_moves)
    print('Tabela pokemon populada')

    df = pd.read_csv('C:/Users/Coud/Documents/Projetos/CRUD/Poke_project/src/Utilts/kanto.csv', sep = ',', encoding="ISO-8859-1")
    dic_pokes = df.set_index('#').T.to_dict('list')
    database.popular_pokemon(dic_pokes)
    print('Tabela pokemon populada')

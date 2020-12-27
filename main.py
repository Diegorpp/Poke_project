from src.Models import database,models
from src.Models.models import Habilidade,Pokemon

if __name__ == "__main__":
    skill_a = Habilidade(
        AP=60,
        tipo='Normal',
        nome='fast attack',
        desc='Habilidade pica que bate rapidao brabamente'
    )

    poke_a = Pokemon(
        num_id=200,
        nome='Aegislash',
        tipo_1='PIKA',
        tipo_2='batata',
        skill=skill_a
    )

    # database.destroi_tabela()
    # print('Tabelas destruidas')

    # database.criar_tabelas()
    # print('Criar tabelas')

    database.popular_habilitade(skill_a)
    print('Tabela skill populada')


    database.popular_pokemon(poke_a)
    print('Tabela poke populada')

from fastapi import FastAPI
from src.Models.database import Pokemon,Habilidade
from src.Models.models import db

app = FastAPI()

@app.get("/pokemon/{item_id}")
def consulta_pokemon(item_id: str):
    item_id = int(item_id)
    db.connect()
    #try:
    pokemon = Pokemon.select(Pokemon.id == item_id).get()
    print(f'pokemon: {pokemon}')
    #except:
    print('deu ruim')
    #finally:
    db.close()
    return {'pokemon':pokemon}
    


@app.get('/authors')
def get_authors():
    authors = Pokemon.select()
    return authors
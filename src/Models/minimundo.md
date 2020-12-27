### Sistema online de vendas de pokemon

#### Minimundo
    "Pericles, o atum monstro" está precisando montar um sistema em que tenhamos compra e venda de pokemons e itens, além disso precisaremos registrar quem fez o pedido e a compra.
    Para saber quem é o cliente precisamos do nick e data de nascimento, numero da pokedex e email.
    Os produtos devem possuir data de entrada, data de validade, preço, quantidade, dono e categoria.
    Deve ser possível realizar uma oferta para qualquer um dos pedidos no market.

## Tabelas

### Cliente
 

### Usuario
- nick - varchar(60) - [PK]
- nasc - Datetime
- pokedex_num - int
- email - varchar(20)
- saldo - int

### Produto
- nome - varchar(60)
- item_id - int
- validade - Datetime
- nick_dono - varchar(60) 
- preco - float
- categoria - varchar(60)
- quantidade - int
- descricao - varchar(100)

### Pedido
- Produto_id - int
- compra - 
- venda -
- troca -

### Vender
- Usuario_nick - varchar(60)
- prod_id - int

### Comprar
- Usuario_nick - varchar(60)
- prod_id - Int
 
### 

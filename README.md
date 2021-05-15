PETSHOW API 

API para uso na aplicação da loja PETSHOW. Utiliza framework Flask (linguagem Python) e banco de dados PostgreSQL. Também implementa classes utilizando ORM Flask-SQLAlchemy. 

Está dividida em 4 componentes denominados ‘Usuários’, ‘Clientes’, ‘Produtos’ e ‘Pedidos’, definidos nas rotas a seguir: 

 

Usuários: 

GET ‘/usuarios/’ 

Função: buscar a listagem de usuários. 

Exemplo de entrada: 

{ 

"nome":"usuario", 

"senha":"senha", 

"login":"usuario", 

"tipo":"funcionario" 

} 

Resposta esperada: Lista de usuários. 

Exemplo de resposta: 

[ 

{ 

"id": 1, 

"login": "jose", 

"nome": "Jose", 

"tipo": "funcionario" 

}, 

{ 

"id": 2, 

"login": "maria", 

"nome": "Maria", 

"tipo": "gerente" 

} 

] 

 

Mensagens de erro:  

Problemas de comunicação com o banco: ‘Não foi possível acessar os dados’ 

 

GET ‘/usuarios/<login>’ 

Função: buscar os dados de usuário específico em função do seu login 

Resposta esperada: detalhes do usuário 

Exemplo de resposta: 

{ 

"id": 2, 

"login": "jose", 

"nome": "Jose", 

"tipo": "funcionario" 

} 

 

Mensagens de erro: 

Usuário inexistente: ‘Usuário não encontrado’ 

Problemas de comunicação com o banco: ‘Não foi possível acessar os dados’ 

 

POST ‘/usuarios/autenticar’ 

Função: autenticar usuário comparando login e senha recebidos no body da requisição. 

Exemplo de entrada: 

{ 

"login":"usuario", 

"senha":"senha" 

} 

Resposta esperada: ‘Usuário autenticado’ 

Mensagens de erro: 

Usuário ou senha incorreta: ‘Usuário ou senha incorretos’ 

Problemas de comunicação com o banco: ‘Não foi possível acessar os dados’ 

 

POST ‘/usuarios/novo’ 

Função: cadastrar novo usuário passando os dados no body da requisição 

Exemplo de entrada: 

{ 

"nome":"usuario", 

"senha":"senha", 

"login":"usuario", 

"tipo":"funcionario" 

} 

 

Resposta esperada: ‘Usuário cadastrado’ 

Mensagens de erro: 

Falta de dados: ‘Os dados do usuário não foram inseridos’ 

Usuário existente: ‘Usuário já cadastrado’ 

 

PATCH ‘/usuarios/alterar_senha 

Função: alterar a senha de usuário passando login e nova senha no body da requisição 

Exemplo de entrada: 

{ 

"login":"usuario", 

"senha":"senha" 

} 

Resposta esperada: ‘Senha alterada’ 

Mensagens de erro: 

Erro de integridade: ‘Não foi possível fazer a alteração’ 

Falta de dados: ‘Os dados do usuário não foram inseridos’ 

 

PATCH ‘/usuarios/alterartipo’ 

Função: alterar tipo de usuário (Gerente ou Funcionário) passando login e tipo no body da requisição 

Exemplo de entrada: 

{ 

"login":"usuario", 

"tipo":"gerente" 

} 

 

Resposta esperada: ‘Tipo alterado’ 

Mensagens de erro: 

Falta de dados: ‘Os dados do usuário não foram inseridos’ 

Erro de integridade: ‘Não foi possível fazer a alteração’ 

 

 

Clientes: 

GET ‘/clientes/pets/’ 

Função: lista os pets cadastrados no sistema 

Resposta esperada: lista de pets 

Exemplo de resposta: 

[ 

{ 

"animal_id": 1, 

"genero": "m", 

"id": 1, 

"nome": "Floquinho", 

"porte": "pequeno", 

"raca": "Vira-Lata" 

}, 

{ 

"animal_id": 2, 

"genero": "m", 

"id": 2, 

"nome": "Soft Kitty", 

"porte": "medio", 

"raca": "Siamês" 

} 

] 

Mensagens de erro: 

Problemas de comunicação com o banco: ‘Não foi possível acessar os dados’ 

 

GET ‘/clientes/’ 

Função: listar todos os clientes com seus detalhes 

Resposta esperada: lista dos clientes 

Exemplo de resposta: 

{ 

"clientes": [ 

{ 

"cliente": { 

"cpf": "10000000001", 

"email": "beakiddo@kiddo.com", 

"endereco": { 

"bairro": "Vila Frente", 

"cep": "060000-160", 

"cidade": "Osasco", 

"id": 1, 

"numero": "23", 

"rua": "Rua 01", 

"uf": "SP" 

}, 

"id": 1, 

"nome": "Beatrix Kiddo", 

"pets": [ 

{ 

"animal_id": 1, 

"genero": "m", 

"id": 1, 

"nome": "Floquinho", 

"porte": "pequeno", 

"raca": "Vira-Lata" 

}, 

{ 

"animal_id": 2, 

"genero": "m", 

"id": 2, 

"nome": "Soft Kitty", 

"porte": "medio", 

"raca": "Siamês" 

} 

], 

"telefones": [ 

{ 

"cliente_id": 1, 

"id": 1, 

"telefone": "01199938884" 

}, 

{ 

"cliente_id": 1, 

"id": 2, 

"telefone": "01199882244" 

} 

] 

} 

}, 

{ 

"cliente": { 

"cpf": "10000000009", 

"email": "bill@kill.com", 

"endereco": { 

"bairro": "Vila Ré", 

"cep": "060020-161", 

"cidade": "Barueri", 

"id": 2, 

"numero": "43", 

"rua": "Rua 02", 

"uf": "SP" 

}, 

"id": 2, 

"nome": "Bill", 

"pets": [ 

{ 

"animal_id": 1, 

"genero": "m", 

"id": 1, 

"nome": "Floquinho", 

"porte": "pequeno", 

"raca": "Vira-Lata" 

} 

], 

"telefones": [ 

{ 

"cliente_id": 2, 

"id": 3, 

"telefone": "01199238884" 

}, 

{ 

"cliente_id": 2, 

"id": 4, 

"telefone": "01199882244" 

} 

] 

} 

}, 

{ 

"cliente": { 

"cpf": "10000000011", 

"email": "lorelai@kill.com", 

"endereco": { 

"bairro": "Vila Vazia", 

"cep": "060001-162", 

"cidade": "Mauá", 

"id": 3, 

"numero": "63", 

"rua": "Rua 03", 

"uf": "SP" 

}, 

"id": 3, 

"nome": "Rory", 

"pets": [ 

{ 

"animal_id": 2, 

"genero": "f", 

"id": 4, 

"nome": "Garfilda", 

"porte": "grande", 

"raca": "Zebrado" 

} 

], 

"telefones": [ 

{ 

"cliente_id": 3, 

"id": 5, 

"telefone": "01199966884" 

}, 

{ 

"cliente_id": 3, 

"id": 6, 

"telefone": "01199886644" 

} 

] 

} 

} 

] 

} 

Mensagens de erro: 

Problemas de comunicação com o banco: ‘Não foi possível acessar os dados’ 

 

POST ‘/clientes/’ 

Função: cadastrar novo cliente passando os dados, seus pets e telefones no body da requisição 

Exemplo de entrada: 

{ 

"nome":"Fulano", 

"email":"fulano@det.al", 

"cpf":"2", 

"endereco":{ 

"rua":"rua quinze", 

"numero":"25 fundos", 

"cep":"06000-000", 

"bairro":"Jardim Europa", 

"cidade":"Osasco", 

"uf":"AC" 

}, 

"telefones": [{ 

"telefone":"4545-4665" 

}, 

{ 

"telefone":"4545-4699" 

}], 

"pets": [{ 

"nome":"Spike", 

"raca":"Pequines", 

"porte":"pequeno", 

"genero":"m", 

"animal_id":1 

}, 

{ 

"nome":"Garfield", 

"raca":"vira lata", 

"porte":"medio", 

"genero":"m", 

"animal_id":2 

}] 

} 

Resposta esperada: ‘Cliente cadastrado’ 

Mensagens de erro:  

Falta de dados: ‘Os dados do cliente não foram inseridos’ 

Problemas com dados de telefone: ‘Nao foi possivel cadastrar o telefone’ 

Problemas com dados de pet: ‘Nao foi possivel cadastrar o pet’ 

Problemas com dados de cliente: ‘Não foi possível cadastrar o cliente’ 

Problemas com dados de endereço: ‘Nao foi possivel cadastrar o endereço’ 

 

PUT ‘/clientes/<id>/alterar/’ 

Função: alterar dados cadastrais de cliente, passando os dados no body da requisição 

Observação: Para o atributo ‘pets’, o body deve receber seus respectivos ids. Caso seja cadastrado um novo pet na requisição, o id deverá receber o valor 0 (‘zero’). No caso de remoção de todos os pets ou telefones do cadastro, basta passar uma lista vazia para o atributo. 

Exemplo de entrada: 

{ 

"nome":"Fulano", 

"email":"fulano@det.al", 

"cpf":"3", 

"endereco":{ 

"rua":"rua quinze", 

"numero":"25 fundos", 

"cep":"06000-000", 

"bairro":"Jardim Europa", 

"cidade":"Osasco", 

"uf":"AC" 

}, 

"telefones": [{ 

"telefone":"9999-4665" 

}, 

{ 

"telefone":"4545-4699" 

}, 

{ 

"telefone":"2335-4699" 

}], 

"pets": [{ 

"id": 5, 

"nome":"Spike", 

"raca":"Pequines", 

"porte":"pequeno", 

"genero":"m", 

"animal_id":1 

}, 

{ 

"id": 6, 

"nome":"Garfield", 

"raca":"vira lata", 

"porte":"medio", 

"genero":"m", 

"animal_id":2 

}] 

} 

Resposta esperada: ‘Cliente alterado’ 

Mensagens de erro: 

Falta de dados: ‘Os dados do cliente não foram inseridos’ 

Cliente inexistente: ‘Cliente não encontrado’ 

 

 

Produtos: 

GET ‘/produtos/’ 

Função: listar todos os produtos 

Resposta esperada: lista dos produtos 

Exemplo de resposta: 

[ 

{ 

"animal_id": 1, 

"cod_barras": 39232839, 

"descricao": "Azul", 

"foto": "", 

"id": 1, 

"marca_id": 1, 

"modelo": "Pullover", 

"nome": "Blusa Cão", 

"porcentagem": 10.0, 

"preco_custo": 100.0, 

"preco_venda": 120.0, 

"quantidade": 10, 

"tamanho_id": 1, 

"usuario_id": 1 

}, 

{ 

"animal_id": 1, 

"cod_barras": 39232831, 

"descricao": "Azul", 

"foto": "", 

"id": 2, 

"marca_id": 1, 

"modelo": "Pullover", 

"nome": "Blusa Cão", 

"porcentagem": 10.0, 

"preco_custo": 100.0, 

"preco_venda": 120.0, 

"quantidade": 10, 

"tamanho_id": 2, 

"usuario_id": 1 

}, 

{ 

"animal_id": 1, 

"cod_barras": 39232834, 

"descricao": "Azul", 

"foto": "", 

"id": 3, 

"marca_id": 1, 

"modelo": "Pullover", 

"nome": "Blusa Cão", 

"porcentagem": 10.0, 

"preco_custo": 100.0, 

"preco_venda": 120.0, 

"quantidade": 10, 

"tamanho_id": 3, 

"usuario_id": 1 

}, 

{ 

"animal_id": 2, 

"cod_barras": 39232849, 

"descricao": "Vermelha", 

"foto": "", 

"id": 4, 

"marca_id": 2, 

"modelo": "Pullover", 

"nome": "Blusa Gato", 

"porcentagem": 10.0, 

"preco_custo": 100.0, 

"preco_venda": 120.0, 

"quantidade": 30, 

"tamanho_id": 2, 

"usuario_id": 2 

} 

] 

Mensagens de erro: 

Problemas de comunicação com o banco: ‘Não foi possível acessar os dados’ 

 

POST ‘/produtos/’ 

Função: cadastrar novo produto passando seus dados no body da requisição 

Exemplo de entrada: 

{ 

"nome":"blusinha de ossos", 

"descricao":"blusinha de ossos", 

"modelo":"0205050", 

"cod_barras": 101012, 

"porcentagem": 20, 

"preco_custo":15, 

"preco_venda":20, 

"quantidade":10, 

"foto":"foto.jpg", 

"marca_id":1, 

"animal_id":1, 

"tamanho_id":2, 

"usuario_id": 1 

} 

Resposta esperada: ‘Produto cadastrado’ 

Mensagens de erro: 

Erro de integridade: ‘Produto já cadastrado’ 

Problemas de comunicação com o banco: ‘Não foi possível acessar os dados’ 

Falta de dados: ‘Os dados do produto não foram inseridos’ 

 

 

PUT ‘/produtos/<id>/alterar/’ 

Função: alterar dados de produto 

Exemplo de entrada: 

{ 

"nome":"blusinha de ossos", 

"descricao":"blusinha de ossos", 

"modelo":"0205050", 

"cod_barras": 101012, 

"porcentagem": 20, 

"preco_custo":15, 

"preco_venda":20, 

"quantidade":10, 

"foto":"foto.jpg", 

"marca_id":1, 

"animal_id":1, 

"tamanho_id":2, 

"usuario_id": 1 

} 

Resposta esperada: ‘Produto alterado’ 

Mensagens de erro: 

Erro de integridade: ‘Não foi possível fazer a alteração’ 

Falta de dados: ‘Os dados do produto não foram inseridos’ 

Problemas de comunicação com o banco: ‘Não foi possível acessar os dados’ 

 

GET ‘/produtos/marcas/’ 

Função: listar marcas 

Resposta esperada: lista de marcas 

Exemplo de resposta: 

[ 

{ 

"id": 1, 

"marca": "PetDog" 

}, 

{ 

"id": 2, 

"marca": "PetCat" 

} 

] 

Mensagens de erro: 

Problemas de comunicação com o banco: ‘Não foi possível acessar os dados’ 

 

POST ‘/produtos/marcas/’ 

Funçao: cadastrar nova marca 

Exemplo de entrada: 

{ 

"marca":"Pet Fashions" 

} 

Resposta esperada: ‘Marca cadastrada’ 

Mensagens de erro: 

Erro de integridade: ‘Marca já cadastrada’ 

Falta de dados: ‘Os dados da marca não foram inseridos’ 

 

 

GET ‘/produtos/tamanhos/’ 

Função: listar tamanhos 

Resposta esperada: lista de tamanhos 

Exemplo de resposta: 

[ 

{ 

"id": 1, 

"tamanho": "P" 

}, 

{ 

"id": 2, 

"tamanho": "M" 

}, 

{ 

"id": 3, 

"tamanho": "G" 

} 

] 

Mensagens de erro: 

Problemas de comunicação com o banco: ‘Não foi possível acessar os dados’ 

 

POST ‘/produtos/animais/’ 

Funçao: cadastrar novo tamanho 

Exemplo de entrada: 

{ 

"tamanho":"G" 

} 

 

Resposta esperada: Animal cadastrado’ 

Mensagens de erro: 

Erro de integridade: ‘Animal já cadastrado’ 

Falta de dados: ‘Os dados do animal não foram inseridos’ 

 

GET ‘/produtos/animais/’ 

Função: listar animais 

Resposta esperada: lista de animais 

Exemplo de resposta: 

[ 

{ 

"animal": "cachorro", 

"id": 1 

}, 

{ 

"animal": "gato", 

"id": 2 

} 

] 

Mensagens de erro: 

Problemas de comunicação com o banco: ‘Não foi possível acessar os dados’ 

 

POST ‘/produtos/animais/’ 

Funçao: cadastrar novo animal 

Exemplo de entrada: 

{ 

"animal":"Porquinho" 

} 

Resposta esperada: ‘Animal cadastrado’ 

Mensagens de erro: 

Erro de integridade: 'Animal já cadastrado’ 

Falta de dados: ‘Os dados de animl não foram inseridos’ 

 

 

 

Pedidos: 

 

GET ‘/pedidos/’ 

Função: listar pedidos 

Exemplo de resposta: 

{ 

"pedidos": [ 

{ 

"cliente": { 

"cpf": "3", 

"email": "fulano@det.al", 

"endereco": { 

"bairro": "Jardim Europas", 

"cep": "06000-000", 

"cidade": "Osasco", 

"id": 1, 

"numero": "25 fundos", 

"rua": "rua quinze", 

"uf": "AC" 

}, 

"id": 1, 

"nome": "Fulanou" 

}, 

"itens": [ 

{ 

"id": 1, 

"pedido_id": 1, 

"preco": 120.0, 

"produto_id": 1, 

"quantidade": 1, 

"total": 120.0 

}, 

{ 

"id": 2, 

"pedido_id": 1, 

"preco": 120.0, 

"produto_id": 2, 

"quantidade": 1, 

"total": 120.0 

} 

], 

"pedido": { 

"cliente_id": 1, 

"data": "Tue, 04 May 2021 13:45:47 GMT", 

"id": 1, 

"observacao": "separado", 

"situacao_id": 1, 

"usuario_id": 2 

}, 

"situacao": "recebido" 

}, 

{ 

"cliente": { 

"cpf": "3", 

"email": "fulano@det.al", 

"endereco": { 

"bairro": "Jardim Europas", 

"cep": "06000-000", 

"cidade": "Osasco", 

"id": 1, 

"numero": "25 fundos", 

"rua": "rua quinze", 

"uf": "AC" 

}, 

"id": 1, 

"nome": "Fulanou" 

}, 

"itens": [ 

{ 

"id": 3, 

"pedido_id": 2, 

"preco": 120.0, 

"produto_id": 1, 

"quantidade": 2, 

"total": 240.0 

}, 

{ 

"id": 4, 

"pedido_id": 2, 

"preco": 120.0, 

"produto_id": 2, 

"quantidade": 1, 

"total": 120.0 

} 

], 

"pedido": { 

"cliente_id": 1, 

"data": "Tue, 04 May 2021 13:45:47 GMT", 

"id": 2, 

"observacao": "", 

"situacao_id": 2, 

"usuario_id": 2 

}, 

"situacao": "concluido" 

}, 

{ 

"cliente": { 

"cpf": "10000000009", 

"email": "bill@kill.com", 

"endereco": { 

"bairro": "Vila Ré", 

"cep": "060020-161", 

"cidade": "Barueri", 

"id": 2, 

"numero": "43", 

"rua": "Rua 02", 

"uf": "SP" 

}, 

"id": 2, 

"nome": "Bill" 

}, 

"itens": [ 

{ 

"id": 5, 

"pedido_id": 3, 

"preco": 120.0, 

"produto_id": 4, 

"quantidade": 1, 

"total": 120.0 

} 

], 

"pedido": { 

"cliente_id": 2, 

"data": "Tue, 04 May 2021 13:45:47 GMT", 

"id": 3, 

"observacao": "cheque sem fundos", 

"situacao_id": 3, 

"usuario_id": 3 

}, 

"situacao": "cancelado" 

} 

] 

} 

Mensagens de erro: 

Problemas de comunicação com o banco: ‘Não foi possível acessar os dados’ 

 

 

POST ‘/pedidos/’ 

Função: cadastrar novo pedido 

Exemplo de entrada: 

{ 

"cliente_id": 1, 

"usuario_id": 1, 

"observacao": "mostruarios", 

"itens": [ 

{ 

"produto_id": 1, 

"quantidade": 1 

}, 

{ 

"produto_id": 4, 

"quantidade": 1 

} 

] 

} 

Mensagens de erro: 

Problemas de comunicação com o banco: ‘Não foi possível acessar os dados’ 

 

PUT ‘/pedidos/<id>/situacao/’ 

Função: atualizar a situação e observações de um pedido 

Exemplo de entrada: 

{ 

"situacao_id": 1, 

"observacao": "itens de mostruario", 

} 

Resposta esperada: ‘Pedido alterado’, ‘Pedido concluído’ ou ‘Pedido cancelado’ 

Mensagens de erro: 

Falta de dados: ‘Os dados do pedido não foram inseridos’ 

Problemas de comunicação com o banco: ‘Não foi possível acessar os dados’ 

Quantidade: ‘Quantidade insuficiente de produto em estoque’ 

 

PUT ‘/pedidos/<id>/itens/’ 

Função: atualiza a lista de produtos de um pedido 

Exemplo de entrada: 

{ 

"itens": [ 

{ 

"produto_id": 1, 

"quantidade": 1 

}, 

{ 

"produto_id": 4, 

"quantidade": 2 

} 

] 

} 

 

Resposta esperada: ‘Pedido alterado’ 

Mensagens de erro: 

Pedido não habilitado para alteração: ‘Pedido não pode ser alterado’ 

Falta de dados: ‘Os dados do pedido não foram inseridos’ 

Problemas de comunicação com o banco: ‘Não foi possível acessar os dados’ 

# Teste_Tecnico_HMZ_TECH

Projeto com objetivo de disponibilizar uma API Rest para expor clientes com seus respectivos dados e informações. Os relacionamentos das entidades precisam obedecer a regras mencionadas abaixo:

•	Um cliente possui nome, cnpj, endereço (logradouro, bairro, cidade, estado, país)

•	Um cliente possui mais de um contato (nome, cargo, telefone, e-mail)

•	Um cliente possui um status, representando se ele está como Ativo ou Inativo.
<hr>

<h2>Plano organizacional</h2>

Após verificar todas as regras, construí um fluxograma para mapear o passo a passo do que fazer; 

A tecnologia escolhida para compor esse projeto foi Python com o framework FastApi, visano desempenho com agilidade.

O software usado para realizar os testes foi o <a href="https://insomnia.rest/download">Insomnia</a>.

<h2>Requisitos e instalações</h2>

Antes de executar o projeto, você precisará ter o Python e o framework FastAPI instalados em sua máquina.

•	Python: <a href="https://www.python.org/downloads/">Link para download do Python</a>;

•	FastAPI: pip install fastapi;

•	Instale a Uvicorn (é uma implementação de servidor web ASGI para Python): pip install uvicorn;

•	Para executar o projeto, utilize o seguinte comando: uvicorn main:app --reload.

<hr>

<h2>Uso da Api</h2>

•	Para a documentação da API(insira o "/docs" no final da url): http://127.0.0.1:8000/docs

![Docs](https://github.com/lpereira1025/Teste_Tecnico_HMZ_TECH/assets/69816562/a767d652-0278-4f38-980a-5872c68f652f)


•	GET /clientes/: Retorna uma lista de todos os clientes cadastrados.

![Get(all)](https://github.com/lpereira1025/Teste_Tecnico_HMZ_TECH/assets/69816562/3edd3be5-9d9c-497a-88ba-62af2ec434d9)


•	GET /clientes/{cliente_id}: Retorna os detalhes de um cliente específico com base no ID.

![Get(2)](https://github.com/lpereira1025/Teste_Tecnico_HMZ_TECH/assets/69816562/59b0123e-2842-46fc-90f2-c91959a83273)


•	POST /clientes/: Cria um novo cliente com base nos dados fornecidos.

![Post](https://github.com/lpereira1025/Teste_Tecnico_HMZ_TECH/assets/69816562/b84a0c55-70bd-4908-80d3-b8ef3ddb1bf8)


•	PUT /clientes/{cliente_id}: Atualiza os dados de um cliente existente com base no ID.

![Put](https://github.com/lpereira1025/Teste_Tecnico_HMZ_TECH/assets/69816562/1b37ddfc-3d6a-4617-a427-8963131b6bda)


•	PATCH /clientes/{cliente_id}: Atualiza parcialmente os dados de um cliente existente com base no ID.

![Patch](https://github.com/lpereira1025/Teste_Tecnico_HMZ_TECH/assets/69816562/bf677169-149f-4825-a9c5-06294974a23a)


•	DELETE /clientes/{cliente_id}: Exclui um cliente existente com base no ID.

![Delete](https://github.com/lpereira1025/Teste_Tecnico_HMZ_TECH/assets/69816562/3c1ec098-322f-4017-aa5c-2d32f417b583)

<hr>

<h2>Desafio de Implementação de autenticação e autorização da API</h2>

Na API em micro serviço que foi construída, não foram implementadas estratégias de autenticação e autorização. A API está configurada como um serviço público, o que significa que qualquer cliente pode fazer solicitações para as rotas disponíveis sem a necessidade de autenticação prévia.

Por padrão, a API FastAPI não possui autenticação ou controle de acesso integrado. Isso é algo que deve ser adicionado manualmente, caso seja necessário garantir a segurança e proteção dos recursos da API.

Como solução, escolheria duas opções:

1° - Através das bibliotecas fastapi.security e fastapi_users: Fornece suporte para esquemas de autenticação comuns, como OAuth2 e Basic Authentication. Ela permite que você proteja rotas específicas em sua API, exigindo que os clientes autentiquem-se antes de acessar recursos protegidos além de gerenciamento de usuários de alto nível que se integra perfeitamente com o FastAPI. Ela facilita a criação de rotas de autenticação e gerenciamento de usuários em sua API.

2° - Através do JWT: Ser autocontido (todas as informações necessárias estão no próprio token) e ser facilmente verificável pelo servidor sem precisar fazer consultas adicionais ao banco de dados. Quando o cliente envia uma solicitação com um token JWT no cabeçalho, o servidor pode verificar a validade do token usando a chave secreta para garantir que ele não tenha sido adulterado e que o usuário seja autenticado corretamente.

<hr>

<h2>Arquivo SQL</h2>

Conforme solicitado, o arquivo do banco de dados para <a href="https://drive.google.com/file/d/1V50WMNOqBQ1C30ENeWcCzK9Pot7uaLF0/view?usp=drive_link">Download</a>. 

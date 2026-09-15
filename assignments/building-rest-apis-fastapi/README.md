# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a construir uma REST API usando o framework FastAPI, organizando endpoints, validando dados com modelos Pydantic e implementando operações CRUD em memória.

## 📝 Tasks

### 🛠️ Create the First API Endpoint

#### Descrição
Configure uma aplicação FastAPI e crie endpoints básicos para apresentar informações sobre a API e listar os livros disponíveis.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI no arquivo `starter-code.py`.
- Implementar um endpoint `GET /` que retorne uma mensagem indicando que a API está funcionando.
- Implementar um endpoint `GET /books` que retorne a lista de livros cadastrados.
- Iniciar a aplicação com um servidor compatível, como Uvicorn, e permitir o acesso à documentação automática em `/docs`.

### 🛠️ Validate and Add Books

#### Descrição
Defina um modelo Pydantic para representar um livro e crie um endpoint para adicionar novos livros à coleção.

#### Requisitos
O programa concluído deve:

- Criar um modelo `Book` com, no mínimo, os campos `title`, `author` e `year`.
- Usar o modelo `Book` para validar o corpo das requisições.
- Implementar um endpoint `POST /books` que adicione um livro válido à coleção.
- Retornar o livro criado e uma resposta HTTP apropriada.
- Rejeitar requisições com campos ausentes ou tipos de dados inválidos.

### 🛠️ Implement CRUD Operations

#### Descrição
Complete a API implementando operações para consultar, atualizar e remover livros individualmente por identificador.

#### Requisitos
O programa concluído deve:

- Atribuir um identificador único a cada livro.
- Implementar `GET /books/{book_id}` para buscar um livro específico.
- Implementar `PUT /books/{book_id}` para atualizar os dados de um livro.
- Implementar `DELETE /books/{book_id}` para remover um livro.
- Retornar o status HTTP `404` quando o identificador solicitado não existir.
- Demonstrar as rotas e os códigos de resposta na documentação interativa do FastAPI.

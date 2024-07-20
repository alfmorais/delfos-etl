# Projeto ETL Delfos

Projeto consiste em buscar os dados de uma API, fazer um tratamento nos dados conforme as especificações do projeto e salvar no banco de dados.

## Tecnologias:

- Python 3.11.2
- Poetry (version 1.8.2)
- Docker Compose version v2.27.1-desktop.1

## Como rodar o projeto:

- Renome o arquivo `.env.example` para -> `.env`
- Instale as dependências do projeto com o comando `poetry shell` e `poetry install`
- Suba o serviço do Banco de Dados com o comando `docker compose up`
- Rode as migrações do banco de dados: `poetry run alembic upgrade head`
- Certifique que o projeto [project-delfos](https://github.com/alfmorais/project-delfos/) esteja rodando corretamente. Siga instruções do README.
- Rode o ETL com o comando `poetry run python -m src.run 1721489906 1722437306 AlfredoMoraisNeto`

OBS:

O comando para rodar o ETL recebe como paramêtros `start_time`, `end_time` e `signal`: 

- Comando Python: `poetry run python -m src.run`
- start_time: `1721489906`
- end_time: `1722437306`
- signal: `AlfredoMoraisNeto`

A saída do ETL será essa:
```bash
1580 objetos inserido com sucesso
```
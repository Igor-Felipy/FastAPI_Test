# FastAPI_Test

## Ferramentas usadas para o projeto:

- virtual enironment
- Docker
- PostgreSQL
- FastAPI
- Ruff
- Pytest
- Taskpy

## Como rodar:

- rode o comando: fastapi dev api/app.py

## Documentação:

- localhost:8080/docs
- localhost:8080/redoc

# Padronização/Estilização:

- checar a padronização: ruff check .
- reescrever a padronização: ruff format .

# Rodar Tests:

- Rodar testes: pytest
- Ver extensão da cobertura de testes: pytest --cov=api -vv
- Gerar html de cobertura: coverage html

# Prisma FastApi

[![CI](https://github.com/prisma-korea/prisma-fastapi/actions/workflows/main.yml/badge.svg)](https://github.com/prisma-korea/prisma-fastapi/actions/workflows/main.yml)

## Blog post
- [Medium](https://medium.com/dooboolab/prisma-with-python-and-fastapi-33bf25bb20c0)

## Setup virtual environment

```sh
python -m venv .venv
source .venv/bin/activate
```

## Install requirements

```sh
pip install -r requirements.txt
```

## Setup environment
1. cp `.env.sample` `.env`
2. Include `DATABASE_URL`
   ```
   DATABASE_URL="postgresql://<user>:<password>@<url>:5432/postgres?schema=<scheme>"
   ```
   > Note that you should change appropriate values in `user`, `password`, `url`, `scheme` fields. Or you can even use other database. More about [connection urls](https://www.prisma.io/docs/reference/database-connectors/connection-urls)

## Generate Prisma Client and Nexus

```sh
prisma generate
```

## Start server

```sh
uvicorn main:app --reload
```

## Notes

> After installing packages

```sh
pip freeze > requirements.txt
```

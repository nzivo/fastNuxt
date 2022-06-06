# FASTAPI meets NUXTJS

Here is a fun project I[^1] am doing so as to learn NuxtJS and Fast API.

## Nuxt Documentation[^2]

Nuxt.js is a free and open source JavaScript library based on Vue.js, Node.js, Webpack and Babel.js. Nuxt is inspired by Next.js, which is a framework of similar purpose, based on React.js.

Initially install plugins

```
yarn install
```

Run the server

```
yarn dev
```

## FastAPI Documentation[^3]

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

The key features are:

1. Fast.
2. Fast to code.
3. Fewer bugs.
4. Intuitive.
5. Easy to use and learn.
6. Short.
7. Fewer bugs.
8. Robust.
9. Standards-based.

I will be using git for my commands, please check official documentaion for powershell, cmd and other OS commands to access the `venv`

access `venv` on terminal **avoid $**

```
$ cd <server>\Scripts
$ . activate
```

to install pip dependencies since I will use Postgres henceforth

```
pip install -r requirements.txt
```

### Older Version

Install pip dependencies **Using mysql DB**

```
pip install fastapi sqlalchemy pymysql uvicorn
```

Incase of a warning to update pip, run

```
python.exe -m pip install --upgrade pip
```

## Docker Commands

To run a **postgres container**

```
docker run --name postgresDB -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres
```

To install a mysql container

```
docker run --name mysqldb -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=fastapi -d -p 3306:3306 mysql:latest
```

[^1]: [John Nzivo](https://github.com/nzivo)
[^2]: [Nuxt JS](https://nuxtjs.org/)
[^3]: [Fast API](https://fastapi.tiangolo.com/)

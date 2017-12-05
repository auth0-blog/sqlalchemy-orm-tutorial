# SQLAlchemy ORM Tutorial for Python Developers

This repository accompanies the [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers)
article on Auth0's blog. Head there to learn about SQLAlchemy ORM.

## External Dependencies

The code in this repository depends on two things: Python itself and [`pipenv`](https://github.com/kennethreitz/pipenv).
Having at least Python on our machine developement, we can install `pipenv` as follows:

```bash
# pip or pip3, which ever points to Python 3
pip3 install pipenv
```

After that, we can install the dependencies of this project by issuing:

```bash
# activate virtual env
pipenv shell

# install dependencies
pipenv install
```

## Useful Commands

```bash
# starting a dockerized instance of PostgreSQL
docker run --name sqlalchemy-orm-psql \
    -e POSTGRES_PASSWORD=dbpassword \
    -e POSTGRES_USER=dbuser \
    -e POSTGRES_DB=sqlalchemy-orm-tutorial \
    -p 5432:5432 \
    -d postgres

# running basic example
python -m examples.basic

# running one to one example
python -m examples.onetoone
```
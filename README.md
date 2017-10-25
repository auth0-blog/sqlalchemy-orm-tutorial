# SQLAlchemy ORM Tutorial for Python Developers

This repository accompanies the [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers)
article on Auth0's blog. Head there to learn about SQLAlchemy ORM.

## Useful Commands


```bash
# starting a dockerized instance of PostgreSQL
docker run --name sqlalchemy-orm-psql \
    -e POSTGRES_PASSWORD=dbpassword \
    -e POSTGRES_USER=dbuser \
    -e POSTGRES_DB=sqlalchemy-orm-tutorial \
    -p 5432:5432 \
    -d postgres

# running inserts
python inserts.py
```
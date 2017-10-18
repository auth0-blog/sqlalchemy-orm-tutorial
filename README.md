# SQLAlchemy ORM Tutorial for Python Developers

This repository accompanies the [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers)
article on Auth0's blog. Head there to learn about SQLAlchemy ORM.

## Useful Commands

Starting a dockerized instance of PostgreSQL.

```bash
docker run --name cashman-psql \
    -e POSTGRES_PASSWORD=dbpassword \
    -e POSTGRES_USER=dbuser \
    -e POSTGRES_DB=sqlalchemy-tutorial \
    -p 5432:5432 \
    -d postgres
```
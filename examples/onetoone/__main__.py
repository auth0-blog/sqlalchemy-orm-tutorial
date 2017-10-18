# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .mobile import Mobile
from .user import User
from ..common.base import Base

engine = create_engine('postgresql://dbuser:dbpassword@localhost:5432/sqlalchemy-orm-tutorial')
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


def populate_database():
    session = Session()

    bruno = User("Bruno Krebs")
    john = User("John Doe")

    brunos_mobile = Mobile("android", "99991111", bruno)
    johns_mobile = Mobile("iphone", "55554444", john)

    session.add(brunos_mobile)
    session.add(johns_mobile)

    session.commit()
    session.close()


def query_database():
    session = Session()
    users = session.query(User)
    session.close()
    return users.all()


if __name__ == "__main__":
    users = query_database()
    if len(users) == 0:
        populate_database()
    users = query_database()
    print(users)

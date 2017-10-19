# coding=utf-8

from .mobile import Mobile
from .user import User
from ..common.base import session_factory


def populate_database():
    session = session_factory()

    bruno = User("Bruno Krebs")
    john = User("John Doe")

    brunos_mobile = Mobile("android", "99991111", bruno)
    johns_mobile = Mobile("iphone", "55554444", john)

    session.add(brunos_mobile)
    session.add(johns_mobile)

    session.commit()
    session.close()


def query_users():
    session = session_factory()
    users_query = session.query(User)
    session.close()
    return users_query.all()


def query_mobiles():
    session = session_factory()
    mobiles_query = session.query(Mobile)
    session.close()
    return mobiles_query.all()


if __name__ == "__main__":
    users = query_users()
    if len(users) == 0:
        populate_database()

    users = query_users()
    for user in users:
        print(f'{user.name} has an {user.mobile.model} with number {user.mobile.number}')

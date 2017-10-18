from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .base import Base
from .person import Person


engine = create_engine('postgresql://dbuser:dbpassword@localhost:5432/sqlalchemy-orm-tutorial')
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


def create_people():
    session = Session()
    bruno = Person("Bruno Krebs", date(1984, 10, 20), 182, 84.5)
    john = Person("John Doe", date(1990, 5, 17), 173, 90)
    session.add(bruno)
    session.add(john)
    session.commit()
    session.close()


def get_people():
    session = Session()
    people = session.query(Person)
    session.close()
    return people.all()


if __name__ == "__main__":
    people = get_people()
    if len(people) == 0:
        create_people()
    people = get_people()
    print(people)

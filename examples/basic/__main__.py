from datetime import date

from .person import Person
from ..common.base import Session


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
    people_query = session.query(Person)
    session.close()
    return people_query.all()


if __name__ == "__main__":
    people = get_people()
    if len(people) == 0:
        create_people()
    people = get_people()
    print(people)

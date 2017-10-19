# coding=utf-8

from .student import Student
from .course import Course
from ..common.base import session_factory


def populate_database():
    session = session_factory()

    bruno = Student("Bruno Krebs")
    john = Student("John Doe")
    serena = Student("Serena Williams")
    jennifer = Student("Jennifer Garner")

    tenis = Course("Tenis Introduction", "Learn the basic rules of tenis", [bruno, john])
    chess = Course("Advanced Chess", "Learn advanced strategies", [serena])
    python = Course("Python Development", "Learn the basic concepts of Python", [serena, jennifer, john])

    session.add(tenis)
    session.add(chess)
    session.add(python)

    session.commit()
    session.close()


def query_courses():
    session = session_factory()
    course_query = session.query(Course)
    session.close()
    return course_query.all()


if __name__ == "__main__":
    courses = query_courses()
    if len(courses) == 0:
        populate_database()

        courses = query_courses()
    for course in courses:
        print(f'"{course.title}" has the following students: ', end="")

        for student in course.students:
            print(f'{student.name}; ', end="")

        print('')

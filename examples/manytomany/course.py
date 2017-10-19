# coding=utf-8

from sqlalchemy import Column, String, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship

from ..common.base import Base

association_table = Table(
    'association', Base.metadata,
    Column('course_id', Integer, ForeignKey('course.id')),
    Column('student_id', Integer, ForeignKey('student.id'))
)


class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    students = relationship("Student", secondary=association_table)

    def __init__(self, title, description, students):
        self.title = title
        self.description = description
        self.students = students

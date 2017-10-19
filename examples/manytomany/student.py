# coding=utf-8

from sqlalchemy import Column, String, Integer

from ..common.base import Base


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

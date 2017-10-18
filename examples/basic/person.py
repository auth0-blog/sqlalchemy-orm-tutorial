# coding=utf-8

from .base import Base
from sqlalchemy import Column, String, Date, Integer, Numeric


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_of_birth = Column(Date)
    height = Column(Integer)
    weight = Column(Numeric)

    def __init__(self, name, date_of_birth, height, weight):
        self.name = name
        self.date_of_birth = date_of_birth
        self.height = height
        self.weight = weight

    def __repr__(self):
        return f'"name":"{self.name}",' \
               f'"dob":"{self.date_of_birth}"' \
               f'"height":"{self.height}"' \
               f'"weight":"{self.weight}"' \
            .format(self=self)

# coding=utf-8

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from ..common.base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    mobile = relationship("Mobile", uselist=False, back_populates="owner")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '{{"name": "{self.name}"' \
               '"mobile": "{self.mobile.number}"}}'.format(self=self)

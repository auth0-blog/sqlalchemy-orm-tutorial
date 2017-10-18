# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ..common.base import Base


class Mobile(Base):
    __tablename__ = 'mobile'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    number = Column(String)
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship("User", back_populates="mobile")

    def __init__(self, model, number, owner):
        self.model = model
        self.number = number
        self.owner = owner

    def __repr__(self):
        return '{{ "model": "{self.model}",' \
               '"number": "{self.number}",' \
               '"owner_name": "{self.owner.name}" }}' \
            .format(self=self)

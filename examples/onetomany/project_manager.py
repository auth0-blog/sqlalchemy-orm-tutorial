# coding=utf-8

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from ..common.base import Base


class ProjectManager(Base):
    __tablename__ = 'project_manager'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    projects = relationship("Project", back_populates="project_manager")

    def __init__(self, name):
        self.name = name

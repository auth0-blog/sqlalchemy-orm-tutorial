# coding=utf-8

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ..common.base import Base


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    project_manager_id = Column(Integer, ForeignKey('project_manager.id'))
    project_manager = relationship("ProjectManager", back_populates="projects")

    def __init__(self, title, description, project_manager):
        self.title = title
        self.description = description
        self.project_manager = project_manager

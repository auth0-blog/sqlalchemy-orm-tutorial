# coding=utf-8

from .project import Project
from .project_manager import ProjectManager
from ..common.base import session_factory


def populate_database():
    session = session_factory()

    bruno = ProjectManager("Bruno Krebs")
    john = ProjectManager("John Doe")

    todo = Project("To-Do List", "Let's help people accomplish their tasks", bruno)
    moneyfy = Project("Moneyfy", "Best app to manage personal finances", john)
    questionmark = Project("QuestionMark", "App that simulates technical exams", bruno)
    blog = Project("NewBlog", "New blog engine that solves all issues", john)

    session.add(todo)
    session.add(moneyfy)
    session.add(questionmark)
    session.add(blog)

    session.commit()
    session.close()


def query_projects():
    session = session_factory()
    projects_query = session.query(Project)
    session.close()
    return projects_query.all()


if __name__ == "__main__":
    projects = query_projects()
    if len(projects) == 0:
        populate_database()

    projects = query_projects()
    for project in projects:
        print(f'"{project.title}" is managed by {project.project_manager.name}')

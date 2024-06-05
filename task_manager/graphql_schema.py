import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from database import Task as TaskModel
from database import SessionLocal

class Task(SQLAlchemyObjectType):
    class Meta:
        model = TaskModel

class Query(graphene.ObjectType):
    tasks = graphene.List(Task)

    def resolve_tasks(self, info):
        db = SessionLocal()
        return db.query(TaskModel).all()

schema = graphene.Schema(query=Query)

from sqlalchemy.orm import Session
import database

def get_task(db: Session, task_id: int):
    return db.query(database.Task).filter(database.Task.id == task_id).first()

def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(database.Task).offset(skip).limit(limit).all()

def create_task(db: Session, task: database.TaskCreate):
    db_task = database.Task(title=task.title, description=task.description, status=task.status)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task: database.TaskUpdate):
    db_task = db.query(database.Task).filter(database.Task.id == task_id).first()
    if db_task:
        for key, value in task.dict(exclude_unset=True).items():
            setattr(db_task, key, value)
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    db_task = db.query(database.Task).filter(database.Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task

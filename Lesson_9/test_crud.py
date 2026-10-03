import pytest
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Student

@pytest.fixture
def db_session():
    
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    session.rollback()
    session.close()
    
    Base.metadata.drop_all(bind=engine)

def test_add_student(db_session: Session):
    student = Student(name="Тестовый студент", email="test@example.com")
    db_session.add(student)
    db_session.commit()
    
    found = db_session.query(Student).filter_by(email="test@example.com").first()
    assert found is not None
    assert found.name == "Тестовый студент"

def test_update_student(db_session: Session):
    student = Student(name="Старое имя", email="update@example.com")
    db_session.add(student)
    db_session.commit()
    
    student.name = "Новое имя"
    db_session.commit()
    
    updated = db_session.query(Student).filter_by(email="update@example.com").first()
    assert updated.name == "Новое имя"

def test_delete_student(db_session: Session):
    student = Student(name="Для удаления", email="delete@example.com")
    db_session.add(student)
    db_session.commit()
    student_id = student.id
    
    db_session.delete(student)
    db_session.commit()
    
    deleted = db_session.query(Student).filter_by(id=student_id).first()
    assert deleted is None
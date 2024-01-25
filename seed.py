from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from faker import Faker
from models import Base, Student, Group, Subject, Teacher, Grade
import random


engine = create_engine(
    "postgresql://postgres:mysecretpassword@localhost:5432/postgres", echo=True
)
Base = declarative_base()

# Створення таблиць у базі даних
Base.metadata.create_all(bind=engine)

# Створення сесії SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Генерація випадкових даних
fake = Faker()

# Створення груп
groups = [Group(name=fake.word()) for _ in range(3)]
session.add_all(groups)
session.commit()

# Створення викладачів
teachers = [Teacher(name=fake.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()

# Створення предметів та прив'язка їх до викладачів
subjects = [
    Subject(name=fake.word(), teacher=random.choice(teachers)) for _ in range(8)
]
session.add_all(subjects)
session.commit()

# Створення студентів та прив'язка їх до груп
students = [Student(name=fake.name(), group=random.choice(groups)) for _ in range(50)]
session.add_all(students)
session.commit()

# Створення оцінок для студентів з усіх предметів
for student in students:
    for subject in subjects:
        grade_value = random.randint(60, 100)
        grade = Grade(value=grade_value, student=student, subject=subject)
        session.add(grade)

# Збереження змін у базі даних
session.commit()

# Закриття сесії
session.close()

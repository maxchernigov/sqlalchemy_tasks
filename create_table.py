from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, MetaData

engine = create_engine(
    "postgresql://postgres:mysecretpassword@localhost:5432/postgres", echo=True
)
metadata = MetaData()

groups = Table(
    "groups",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True),
)

students = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True),
    Column("group_id", Integer, ForeignKey("groups.id")),
)

subjects = Table(
    "subjects",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True),
    Column("teacher_id", Integer, ForeignKey("teachers.id")),
)

teachers = Table(
    "teachers",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String, index=True),
)

grades = Table(
    "grades",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("value", Integer),
    Column("student_id", Integer, ForeignKey("students.id")),
    Column("subject_id", Integer, ForeignKey("subjects.id")),
)

metadata.create_all(engine)

from sqlalchemy import func
from sqlalchemy.orm import joinedload
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from models import Student, Grade, Subject, Group, Teacher

engine = create_engine(
    "postgresql://postgres:mysecretpassword@localhost:5432/postgres", echo=True
)
Session = sessionmaker(bind=engine)
session = Session()


def select_1():
    result = (
        session.query(
            Student.id, Student.name, func.avg(Grade.value).label("average_grade")
        )
        .join(Grade, Student.id == Grade.student_id)
        .group_by(Student.id, Student.name)
        .order_by(func.avg(Grade.value).desc())
        .limit(5)
        .all()
    )

    return result


def select_2(subject_name):
    result = (
        session.query(
            Student.id,
            Student.name.label("studentss_name"),
            func.avg(Grade.value).label("average_grade"),
        )
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.name == subject_name)
        .group_by(Student.id, Student.name)
        .order_by(func.avg(Grade.value).desc())
        .limit(1)
        .all()
    )

    return result


def select_3(subject_name):
    result = (
        session.query(Group.name, func.avg(Grade.value).label("average_grade"))
        .join(Student, Group.id == Student.group_id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.name == subject_name)
        .group_by(Group.name)
        .all()
    )

    return result


def select_4():
    result = session.query(func.avg(Grade.value).label("average_grade")).scalar()
    return result


def select_5(teacher_name):
    result = (
        session.query(Subject.name)
        .join(Teacher)
        .filter(Teacher.name == teacher_name)
        .distinct()
        .all()
    )

    return result


def select_6(group_name):
    result = (
        session.query(Student.name).join(Group).filter(Group.name == group_name).all()
    )
    return result


def select_7(group_name, subject_name):
    result = (
        session.query(Student.name.label("Carrie Vasquez"), Grade.value)
        .join(Group)
        .join(Grade, Student.id == Grade.student_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Group.name == group_name, Subject.name == subject_name)
        .all()
    )

    return result


def select_8(teacher_name):
    result = (
        session.query(func.avg(Grade.value).label("average_grade"))
        .join(Subject)
        .join(Teacher)
        .filter(Teacher.name == teacher_name)
        .scalar()
    )

    return result


def select_9(student_name):
    result = (
        session.query(Subject.name)
        .join(Grade)
        .join(Student)
        .filter(Student.name == student_name)
        .all()
    )

    return result


def select_10(student_name, teacher_name):
    result = (
        session.query(Subject.name)
        .join(Grade)
        .join(Student)
        .join(Teacher)
        .filter(Student.name == student_name, Teacher.name == teacher_name)
        .all()
    )

    return result


if __name__ == "__main__":
    result = select_1()
    print(result)

    result = select_2("tree")
    print(result)

    result = select_3("national")
    print(result)

    result = select_4()
    print(result)

    result = select_5("Benjamin Phillips")
    print(result)

    result = select_6("certain")
    print(result)

    result = select_7("hospital", "deep")
    print(result)

    result = select_8("Jason Neal")
    print(result)

    result = select_9("Courtney Gonzales")
    print(result)

    result = select_10("Joyce Evans", "Alexis James")
    print(result)

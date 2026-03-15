from models import Student


class TestStudents:
    """Тесты для работы со студентами"""

    def test_add_student(self, db_session):
        """Тест добавления студента"""
        student = Student(
            first_name="Анна",
            last_name="Смирнова",
            email="anna@test.com"
        )
        db_session.add(student)
        db_session.commit()
        assert student.id is not None

    def test_update_student(self, db_session, sample_student):
        """Тест изменения студента"""
        sample_student.first_name = "Петр"
        db_session.commit()
        assert sample_student.first_name == "Петр"

    def test_delete_student(self, db_session, sample_student):
        """Тест удаления студента"""
        student_id = sample_student.id
        db_session.delete(sample_student)
        db_session.commit()
        assert db_session.get(Student, student_id) is None

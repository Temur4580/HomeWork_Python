from models import Student


class TestStudents:
    """Простые тесты для студентов"""

    def test_add_student(self, db_session):
        """Тест 1: Добавление студента"""
        # Создаем
        student = Student(
            first_name="Анна",
            last_name="Смирнова",
            email="anna@test.com"
        )

        # Сохраняем
        db_session.add(student)
        db_session.commit()

        # Проверяем
        assert student.id is not None
        saved = db_session.get(Student, student.id)
        assert saved.email == "anna@test.com"

    def test_update_student(self, db_session, sample_student):
        """Тест 2: Изменение студента"""
        # Меняем имя
        sample_student.first_name = "Петр"
        db_session.commit()

        # Проверяем
        assert sample_student.first_name == "Петр"

    def test_delete_student(self, db_session, sample_student):
        """Тест 3: Удаление студента"""
        student_id = sample_student.id

        # Удаляем
        db_session.delete(sample_student)
        db_session.commit()

        # Проверяем
        assert db_session.get(Student, student_id) is None
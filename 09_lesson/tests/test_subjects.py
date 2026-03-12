from models import Subject


class TestSubjects:
    """Простые тесты для предметов"""

    def test_add_subject(self, db_session):
        """Тест 1: Добавление предмета"""
        # Создаем
        subject = Subject(
            name="Python",
            credits=4
        )

        # Сохраняем
        db_session.add(subject)
        db_session.commit()

        # Проверяем
        assert subject.id is not None
        saved = db_session.get(Subject, subject.id)
        assert saved.name == "Python"

    def test_update_subject(self, db_session, sample_subject):
        """Тест 2: Изменение предмета"""
        # Меняем название
        sample_subject.name = "Java"
        db_session.commit()

        # Проверяем
        assert sample_subject.name == "Java"

    def test_delete_subject(self, db_session, sample_subject):
        """Тест 3: Удаление предмета"""
        subject_id = sample_subject.id

        # Удаляем
        db_session.delete(sample_subject)
        db_session.commit()

        # Проверяем
        assert db_session.get(Subject, subject_id) is None
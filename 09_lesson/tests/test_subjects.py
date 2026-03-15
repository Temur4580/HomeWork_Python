from models import Subject


class TestSubjects:
    """Тесты для работы с предметами"""

    def test_add_subject(self, db_session):
        """Тест добавления предмета"""
        subject = Subject(
            name="Python",
            credits=4
        )
        db_session.add(subject)
        db_session.commit()
        assert subject.id is not None

    def test_update_subject(self, db_session, sample_subject):
        """Тест изменения предмета"""
        sample_subject.name = "Java"
        db_session.commit()
        assert sample_subject.name == "Java"

    def test_delete_subject(self, db_session, sample_subject):
        """Тест удаления предмета"""
        subject_id = sample_subject.id
        db_session.delete(sample_subject)
        db_session.commit()
        assert db_session.get(Subject, subject_id) is None

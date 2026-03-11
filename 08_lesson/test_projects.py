import requests
import uuid
import pytest

BASE_URL = "https://ru.yougile.com"  # Добавляем обратно в тесты


class TestProjects:
    """Тесты для проектов YouGile API"""

    # ========== ПОЗИТИВНЫЕ ТЕСТЫ ==========

    def test_create_project_success(self, auth_headers, project_data):
        """[POST] Успешное создание проекта"""
        resp = requests.post(
            f"{BASE_URL}/api-v2/projects",
            json=project_data,
            headers=auth_headers
        )
        assert resp.status_code == 201
        assert "id" in resp.json()

        project_id = resp.json()['id']
        print(f"\n✅ Создан проект с ID: {project_id}")

        # Очистка - удаляем созданный проект
        requests.delete(f"{BASE_URL}/api-v2/projects/{project_id}", headers=auth_headers)

    def test_get_project_success(self, auth_headers, created_project):
        """[GET] Успешное получение проекта по ID"""
        resp = requests.get(
            f"{BASE_URL}/api-v2/projects/{created_project}",
            headers=auth_headers
        )
        assert resp.status_code == 200
        assert resp.json()["id"] == created_project
        print(f"\n✅ Получен проект: {resp.json().get('title', 'Без названия')}")

    def test_update_project_success(self, auth_headers, created_project):
        """[PUT] Успешное обновление проекта"""
        new_title = f"Updated {uuid.uuid4().hex[:8]}"

        # Обновление
        resp = requests.put(
            f"{BASE_URL}/api-v2/projects/{created_project}",
            json={"title": new_title},
            headers=auth_headers
        )
        assert resp.status_code == 200

        # Проверка обновления
        get_resp = requests.get(
            f"{BASE_URL}/api-v2/projects/{created_project}",
            headers=auth_headers
        )
        assert get_resp.json()["title"] == new_title
        print(f"\n✅ Проект обновлен: {new_title}")

    # ========== НЕГАТИВНЫЕ ТЕСТЫ ==========

    def test_create_project_no_title(self, auth_headers):
        """[POST] Негативный: создание проекта без названия"""
        resp = requests.post(
            f"{BASE_URL}/api-v2/projects",
            json={"title": ""},
            headers=auth_headers
        )
        assert resp.status_code in [400, 422]
        print(f"\n⚠️ Ожидаемая ошибка: {resp.status_code}")

    def test_create_project_invalid_json(self, auth_headers):
        """[POST] Негативный: некорректный JSON"""
        headers = auth_headers.copy()
        headers["Content-Type"] = "text/plain"

        resp = requests.post(
            f"{BASE_URL}/api-v2/projects",
            data="not json",
            headers=headers
        )
        assert resp.status_code in [400, 415]
        print(f"\n⚠️ Ожидаемая ошибка: {resp.status_code}")

    def test_get_project_invalid_id(self, auth_headers):
        """[GET] Негативный: некорректный ID"""
        resp = requests.get(
            f"{BASE_URL}/api-v2/projects/123",
            headers=auth_headers
        )
        assert resp.status_code == 404
        print(f"\n⚠️ Ожидаемая ошибка: {resp.status_code}")

    def test_get_project_nonexistent(self, auth_headers):
        """[GET] Негативный: несуществующий проект"""
        fake_id = str(uuid.uuid4())
        resp = requests.get(
            f"{BASE_URL}/api-v2/projects/{fake_id}",
            headers=auth_headers
        )
        assert resp.status_code == 404
        print(f"\n⚠️ Ожидаемая ошибка: {resp.status_code}")

    def test_update_project_nonexistent(self, auth_headers):
        """[PUT] Негативный: обновление несуществующего проекта"""
        fake_id = str(uuid.uuid4())
        resp = requests.put(
            f"{BASE_URL}/api-v2/projects/{fake_id}",
            json={"title": "New Title"},
            headers=auth_headers
        )
        assert resp.status_code == 404
        print(f"\n⚠️ Ожидаемая ошибка: {resp.status_code}")

    def test_update_project_invalid_role(self, auth_headers, created_project):
        """[PUT] Негативный: некорректная роль пользователя"""
        invalid_users = {
            "invalid-uuid": "super_admin"
        }
        resp = requests.put(
            f"{BASE_URL}/api-v2/projects/{created_project}",
            json={"users": invalid_users},
            headers=auth_headers
        )
        assert resp.status_code in [400, 422]
        print(f"\n⚠️ Ожидаемая ошибка: {resp.status_code}")

    @pytest.mark.xfail(reason="Может вернуть 200 если пустое тело допустимо")
    def test_update_project_empty_body(self, auth_headers, created_project):
        """[PUT] Негативный: пустое тело запроса"""
        resp = requests.put(
            f"{BASE_URL}/api-v2/projects/{created_project}",
            json={},
            headers=auth_headers
        )
        assert resp.status_code in [400, 422]  # Ожидаем ошибку валидации
        print(f"\n⚠️ Результат: {resp.status_code}")

    def test_without_auth(self, project_data):
        """Негативный: запрос без авторизации"""
        resp = requests.post(
            f"{BASE_URL}/api-v2/projects",
            json=project_data
        )
        assert resp.status_code == 401
        print(f"\n⚠️ Ожидаемая ошибка авторизации: {resp.status_code}")
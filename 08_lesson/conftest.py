import pytest
import requests
import uuid

BASE_URL = "https://ru.yougile.com"
TOKEN = "jNDA-EM8FOPoQDLgUrQqelliTLnIZKJndjBdfXFEcTtOm+YkV8CZxDps1RkXJ0jg"


@pytest.fixture
def auth_headers():
    """Фикстура с заголовками для авторизации"""
    return {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }


@pytest.fixture
def project_data():
    """Фикстура с данными для нового проекта"""
    return {
        "title": f"Test Project {uuid.uuid4().hex[:8]}"
    }


@pytest.fixture
def created_project(auth_headers, project_data):
    """Фикстура создания проекта и его очистки после теста"""
    project_id = None
    try:
        resp = requests.post(
            url=f"{BASE_URL}/api-v2/projects",
            json=project_data,
            headers=auth_headers
        )
        assert resp.status_code == 201, f"Ошибка создания: {resp.text}"
        project_id = resp.json()["id"]
        print(f"\n🔨 Создан проект с ID: {project_id} для теста")

        yield project_id

    finally:
        if project_id:
            try:
                delete_resp = requests.delete(
                    url=f"{BASE_URL}/api-v2/projects/{project_id}",
                    headers=auth_headers
                )
                if delete_resp.status_code in [200, 204]:
                    print(f"🧹 Проект {project_id} удалён после теста")
                else:
                    print(f"⚠️ Не удалось удалить проект {project_id}: {delete_resp.status_code}")
            except Exception as e:
                print(f"❌ Ошибка при удалении: {e}")
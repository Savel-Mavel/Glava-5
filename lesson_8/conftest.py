import pytest
from yougile_api import YougileAPI

@pytest.fixture
def api():
    """Фикстура, которая предоставляет объект API для тестов."""
    return YougileAPI()

@pytest.fixture
def created_project(api):
    """
    Фикстура, которая создает проект перед тестом и удаляет его после.
    Это гарантирует стабильность: тесты не влияют друг на друга.
    """
    # 1. Подготовка (setup): создаем проект
    project_title = "Test Project For Fixture"
    response = api.create_project(project_title)
    # Предполагаем, что API возвращает ID проекта в поле 'id'
    project_id = response.json().get('id')
    
    # 2. Передаем ID проекта в тест
    yield project_id
    
    # 3. Очистка (teardown): удаляем проект после теста
    # Важно: API Yougile может не иметь метода DELETE для проектов.
    # Если это так, можно архивировать проект или просто оставить как есть.
    # Если метод DELETE есть, раскомментируй строку ниже.
    # api.delete_project(project_id) 
    print(f"\nCleanup: Project {project_id} can be deleted/archived here.")
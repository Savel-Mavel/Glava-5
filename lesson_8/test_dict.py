import pytest
import re

# --- Тесты для POST /api-v2/projects (создание проекта) ---

class TestCreateProject:
    """Позитивные и негативные тесты на создание проекта."""
    
    def test_create_project_positive(self, api):
        """Позитивный тест: создание проекта с валидным названием."""
        # Arrange
        project_name = "My Awesome Project"
        
        # Act
        response = api.create_project(project_name)
        
        # Assert
        assert response.status_code == 201, "Статус код при создании должен быть 201"
        response_data = response.json()
        assert 'id' in response_data, "Ответ должен содержать ID нового проекта"
        # Проверяем, что ID выглядит как UUID (простая проверка)
        assert re.match(r'^[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$', response_data['id'])

    def test_create_project_negative_empty_title(self, api):
        """Негативный тест: попытка создать проект с пустым названием."""
        # Arrange
        empty_title = ""
        
        # Act
        response = api.create_project(empty_title)
        
        # Assert
        # Ожидаем ошибку от сервера (400 Bad Request)
        assert response.status_code == 400, "Сервер должен вернуть ошибку 400 на пустое название"

# --- Тесты для PUT /api-v2/projects/{id} (обновление проекта) ---

class TestUpdateProject:
    """Позитивные и негативные тесты на обновление проекта."""
    
    def test_update_project_positive(self, api, created_project):
        """Позитивный тест: обновление названия существующего проекта."""
        # Arrange
        project_id = created_project
        new_title = "Updated Project Name3"
        
        # Act
        response = api.update_project(project_id, new_title)
        
        # Assert
        assert response.status_code == 200, "Статус код при обновлении должен быть 200"
        
        # Дополнительная проверка: получаем проект и убеждаемся, что название изменилось
        get_response = api.get_project(project_id)
        assert get_response.json()['title'] == new_title

    def test_update_project_negative_invalid_id(self, api):
        """Негативный тест: обновление проекта с несуществующим ID."""
        # Arrange
        fake_project_id = "00000000-0000-0000-0000-000000000000"
        new_title = "This Should Not Work"
        
        # Act
        response = api.update_project(fake_project_id, new_title)
        
        # Assert
        # Ожидаем, что API вернет 404 Not Found или 403/400 в зависимости от логики
        assert response.status_code == 404, "Сервер должен вернуть 404 для несуществующего проекта"

# --- Тесты для GET /api-v2/projects/{id} (получение проекта) ---

class TestGetProject:
    """Позитивные и негативные тесты на получение проекта."""
    
    def test_get_project_positive(self, api, created_project):
        """Позитивный тест: получение существующего проекта по ID."""
        # Arrange
        project_id = created_project
        
        # Act
        response = api.get_project(project_id)
        
        # Assert
        assert response.status_code == 200, "Статус код для существующего проекта должен быть 200"
        project_data = response.json()
        assert 'id' in project_data
        assert project_data['id'] == project_id

    def test_get_project_negative_not_found(self, api):
        """Негативный тест: запрос несуществующего проекта."""
        # Arrange
        non_existent_id = "99999999-9999-9999-9999-999999999999"
        
        # Act
        response = api.get_project(non_existent_id)
        
        # Assert
        # API должен вернуть 404 Not Found
        assert response.status_code == 404, "Сервер должен вернуть 404 для несуществующего проекта"
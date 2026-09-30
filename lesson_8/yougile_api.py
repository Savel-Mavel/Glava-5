import os
import requests

class YougileAPI:
    """Класс-клиент для взаимодействия с API Yougile."""

    def __init__(self):
        # Базовый URL для всех запросов
        self.base_url = "https://yougile.com/api-v2"
        # Токен берется из переменной окружения. Это безопасно!
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('YOUGILE_API_KEY')}"
        }

    def _request(self, method, endpoint, data=None):
        """Универсальный метод для отправки запросов."""
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, json=data, headers=self.headers)
        return response

    # --- Методы для работы с проектами ---

    def create_project(self, title):
        """Создание нового проекта."""
        return self._request("POST", "/projects", {"title": title})

    def update_project(self, project_id, title):
        """Обновление названия проекта."""
        return self._request("PUT", f"/projects/{project_id}", {"title": title})

    def get_project(self, project_id):
        """Получение информации о проекте по ID."""
        return self._request("GET", f"/projects/{project_id}")
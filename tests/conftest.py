import pytest
import random
import string
from api_client.api_client import APIClient
from settings import Settings



@pytest.fixture
def api_client():
    return APIClient(Settings.BASE_URL)


@pytest.fixture
def delete_courier(api_client):
    # Вспомогательная функция для генерации случайной строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # Тело запроса для регистрации курьера
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # Возвращаем данные курьера тесту
    yield payload

    # Удаляем курьера после завершения теста
    login_payload = {
        "login": login,
        "password": password
    }
    # После завершения фикстур удаляем курьера
    response_login = api_client.post('api/v1/courier/login', login_payload )
    if response_login.status_code == 200:
        id_courier = response_login.json()['id']
        api_client.delete(f'api/v1/courier/{id_courier}')


@pytest.fixture
def create_courier(api_client):
    # Вспомогательная функция для генерации случайной строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # Создание курьера
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    api_client.post('api/v1/courier', payload)

    login_payload = {
        "login": login,
        "password": password
    }
    # Возвращаем данные для авторизации
    yield login_payload

    # Удаляем курьера после завершения теста
    response_login = api_client.post('api/v1/courier/login', login_payload )
    if response_login.status_code == 200:
        id_courier = response_login.json()['id']
        api_client.delete(f'api/v1/courier/{id_courier}')
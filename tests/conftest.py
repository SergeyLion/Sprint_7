import pytest
import random
import string
from api_client.api_client import APIClient
from settings import Settings as St



@pytest.fixture
def api_client():
    return APIClient(St.BASE_URL)


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
    response_login = api_client.post(St.ENDPOINT_AUTH_COURIER, login_payload )
    if response_login.status_code == 200:
        id_courier = response_login.json()['id']
        api_client.delete(f'{St.ENDPOINT_COURIER}/{id_courier}')


@pytest.fixture
def create_courier(api_client, delete_courier):

    payload = delete_courier

    api_client.post(St.ENDPOINT_COURIER, payload)

    del payload["firstName"]
    # Возвращаем данные для авторизации
    yield payload

    # Удаляем курьера после завершения теста
    response_login = api_client.post(St.ENDPOINT_AUTH_COURIER, payload )
    if response_login.status_code == 200:
        id_courier = response_login.json()['id']
        api_client.delete(f'{St.ENDPOINT_COURIER}/{id_courier}')
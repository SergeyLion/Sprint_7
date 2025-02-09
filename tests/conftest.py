import pytest
import random
import string
import logging
from api_client.api_client import APIClient
from settings import Settings as St

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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
    logger.info(f"Выданные данные для регистрации: {payload}") #Логирование выдаваемых данных
    # Возвращаем данные курьера тесту
    yield payload
    logger.info(f"Измененные данные в тесте: {payload}") #Логирование какие данные возвращаются после теста
    # Удаляем курьера после завершения теста
    login_payload = {
        "login": login,
        "password": password
    }
    # После завершения фикстур удаляем курьера
    logger.info(f"Авторизация курьера для удаления: {login_payload}") #Логирование данных которые используются для удаления
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
    return payload

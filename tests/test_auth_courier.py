import allure
import pytest
from settings import Settings as St

@allure.feature("Работа с курьером")
@allure.story("Логин курьера в системе")
class TestAuthCourier:
    # Успешная авторизация

    @allure.title("Успешный логин курьера в систему")
    @allure.description(
        "Проверка, что успешной авторизации курьера, возвращения кода 200 и id в теле ответа")
    def test_courier_login_success(self, api_client, create_courier):
        # Данные для авторизации
        payload = create_courier

        with allure.step("Отправка POST-запроса для авторизации курьера"):
            response = api_client.post(St.ENDPOINT_AUTH_COURIER, payload)

        with allure.step("Проверка, что код ответа на создание заказа 200"):
            assert response.status_code == 200, "Ожидался успешный запрос"

        with allure.step("Проверка, что в теле ответа содержится id курьера"):
            assert "id" in response.json(), "Ожидалось поле 'id' в ответе"

    @allure.title("Возврат ошибки при отсутствие обязательного поля")
    @allure.description(
        "Проверка, что при отсутствие обязательного поля, возвращается кода 400 и текст ошибки в теле ответа")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_courier_login_missing_field_returns_error(self, api_client, missing_field, create_courier):
        payload = create_courier
        # Удаляем одно поле
        del payload[missing_field]
        with allure.step("Отправка POST-запроса для авторизации курьера"):
            response = api_client.post(St.ENDPOINT_AUTH_COURIER, payload)

        with (allure.step("Проверка, что код ответа на создание заказа 400")):
            assert response.status_code == St.RESPONSE_AUTH_BAD_REQUEST["code"],\
                f"Ожидалась ошибка 400 при отсутствии поля {missing_field}"

        with allure.step("Проверка, что в теле ответа содержится сообщение об ошибки"):
            assert St.RESPONSE_AUTH_BAD_REQUEST["message"] in response.json()["message"],\
                f"Ожидалось сообщение об ошибке при отсутствии поля {missing_field}"

    @allure.title("Возврат ошибки при неправильном значение поля")
    @allure.description(
        "Проверка, что при неправильном значение поля, возвращается кода 404 и текст ошибки в теле ответа")
    @pytest.mark.parametrize("incorrect_field", ["login", "password"])
    def test_courier_login_incorrect_field_returns_error(self, api_client, incorrect_field, create_courier):
        payload = create_courier
        # Заменяем поле
        payload[incorrect_field] = "tulskiy"
        with allure.step("Отправка POST-запроса для авторизации курьера"):
            response = api_client.post(St.ENDPOINT_AUTH_COURIER, payload)

        with allure.step("Проверка, что код ответа на создание заказа 404"):
            assert response.status_code == St.RESPONSE_AUTH_NOT_FOUND["code"],\
                f"Ожидалась ошибка 404 при неправильном поля {incorrect_field}"

        with allure.step("Проверка, что в теле ответа содержится сообщение об ошибки"):
            assert St.RESPONSE_AUTH_NOT_FOUND["message"] in response.json()["message"],\
                f"Ожидалось сообщение об ошибке при неправильном поля {incorrect_field}"

    @allure.title("Возврат ошибки авторизации несуществующего пользователя")
    @allure.description(
        "Проверка, что при попытки авторизоваться несуществующему пользователю, возвращается кода 404 и текст ошибки в теле ответа")
    def test_courier_login_nonexistent_user_returns_error(self, api_client):

        with allure.step("Отправка POST-запроса для авторизации курьера"):
            response = api_client.post(St.ENDPOINT_AUTH_COURIER, St.PAYLOAD_NONE_USER)

        with allure.step("Проверка, что код ответа на создание заказа 404"):
            assert response.status_code == St.RESPONSE_AUTH_NOT_FOUND["code"],\
                "Ожидалась ошибка 404 для несуществующего пользователя"

        with allure.step("Проверка, что в теле ответа содержится сообщение об ошибки"):
            assert St.RESPONSE_AUTH_NOT_FOUND["message"] in response.json()["message"],\
                "Ожидалось сообщение об ошибке"
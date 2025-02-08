import allure
import pytest

@allure.feature("Работа с курьером")
@allure.story("Создание курьера")
class TestCreatingCourier:

    @allure.title("Успешный создание курьера")
    @allure.description(
        "Проверка, что успешного создания курьера, возвращения кода 201 и статуса создания ok в теле ответа")
    def test_creating_courier_success(self, api_client, delete_courier):
        payload = delete_courier

        with allure.step("Отправка POST-запроса для создания курьера"):
            response = api_client.post("api/v1/courier", data=payload)

        with allure.step("Проверка, что код ответа на создание заказа 201"):
            assert response.status_code == 201, "Ожидался успешный запрос"

        with allure.step("Проверка, что в теле ответа содержится статус создания ok и его значение True"):
            assert response.json()["ok"] == True, "Ожидалось поле 'ok' в ответе со значением True"

    @allure.title("Создание двух одинаковых курьеров")
    @allure.description(
        "Проверка, что создать двух одинаковых курьеров невозможно, возвращение кода 409 и сообщения об ошибки в теле ответа")
    def test_double_creating_courier_conflict(self, api_client, delete_courier):
        payload = delete_courier
        with allure.step("Отправка POST-запроса для создания курьера"):
            response = api_client.post("api/v1/courier", data=payload)

        with allure.step("Проверка, что код ответа на создание заказа 201"):
            assert response.status_code == 201

        with allure.step("Отправка POST-запроса для создания курьера с теме же данными"):
            double_response = api_client.post("api/v1/courier", data=payload)

        with allure.step("Проверка, что код ответа на создание заказа 409"):
            assert double_response.status_code == 409

        with allure.step("Проверка, что в теле ответа сообщение об ошибки"):
            assert double_response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Создание курьера с существующим логином")
    @allure.description(
        "Проверка, что создать двух курьеров с одной почтой нельзя, возвращение кода 409 и сообщения об ошибки в теле ответа")
    def test_creating_courier_existing_login(self, api_client, delete_courier):
        payload = delete_courier
        with allure.step("Отправка POST-запроса для создания курьера"):
            response = api_client.post("api/v1/courier", data=payload)

        with allure.step("Проверка, что код ответа на создание заказа 201"):
            assert response.status_code == 201

        with allure.step("Отправка POST-запроса для создания курьера с таким же логином"):
            payload_exist_login = payload.copy()
            payload_exist_login["password"] = "123654789"
            response_exist_login = api_client.post("api/v1/courier", data=payload_exist_login)

        with allure.step("Проверка, что код ответа на создание заказа 409"):
            assert response_exist_login.status_code == 409

        with allure.step("Проверка, что в теле ответа сообщение об ошибки"):
            assert response_exist_login.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Создание курьера без обязательного поля {missing_field}")
    @allure.description(
        "Проверка, что создать курьера без обязательного поля нельзя, возвращение кода 400 и сообщения об ошибки в теле ответа")
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_field_returns_error(self, api_client, missing_field, delete_courier):
        payload = delete_courier
        # Удаляем одно поле
        del payload[missing_field]
        with allure.step("Отправка POST-запроса для создания курьера"):
            response = api_client.post("api/v1/courier", data=payload)

        with allure.step("Проверка, что код ответа на создание заказа 400"):
            assert response.status_code == 400, f"Ожидалась ошибка 400 при отсутствии поля {missing_field}"

        with allure.step("Проверка, что в теле ответа сообщение об ошибки"):
            assert "Недостаточно данных для создания учетной записи" in response.json()["message"],\
                f"Ожидалось сообщение об ошибке при отсутствии поля {missing_field}"


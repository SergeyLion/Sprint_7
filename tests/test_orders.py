import allure
import pytest
from settings import Settings as St


@allure.feature("Управление заказами")
@allure.story("Создание заказа")
class TestCreateOrder:

    @allure.title("Успешное создание заказа")
    @allure.description(
        "Проверка, что запрос на создание заказов возвращает статус 201 и track заказа")
    @pytest.mark.parametrize("color_select", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_with_black_color_returns_track(self, color_select, api_client):
        payload = St.BASE_ORDER_PAYLOAD.copy()
        payload["color"] = color_select

        with allure.step("Отправка POST-запроса для создание заказа"):
            response = api_client.post(St.ENDPOINT_ORDER, payload)

        with allure.step("Проверка, что код ответа на создание заказа 201"):
            assert response.status_code == 201, "Ожидался успешный запрос"

        with allure.step("Проверка, что в теле ответа содержится track заказа"):
            assert "track" in response.json(), "Ожидалось поле 'track' в ответе"

@allure.feature("Управление заказами")
@allure.story("Получение списка заказов")
class TestListOrder:

    @allure.title("Успешное получение списка заказов")
    @allure.description(
        "Проверка, что запрос на получение списка заказов возвращает статус 200 и непустой список заказов.")
    def test_get_list_order_success(self, api_client):

        payload = {'limit':'10', 'page':'0'}
        with allure.step("Отправка GET-запроса для получения списка заказов"):
            response = api_client.get(St.ENDPOINT_ORDER, params=payload)

        with allure.step("Проверка, что статус-код ответа равен 200"):
            assert response.status_code == 200, f"Ожидался статус-код 200, но получен {response.status_code}"

        with allure.step("Проверка, что список заказов содержит более одного элемента"):
            orders = response.json().get("orders", [])
            assert len(orders) > 1, f"Ожидалось более одного заказа, но получено {len(orders)}"

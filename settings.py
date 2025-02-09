

class Settings:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    # Авторизация
    ENDPOINT_AUTH_COURIER = "api/v1/courier/login" # Courier - Логин курьера в системе
    RESPONSE_AUTH_BAD_REQUEST = {"code": 400, "message": "Недостаточно данных для входа"}
    RESPONSE_AUTH_NOT_FOUND = {"code": 404, "message": "Учетная запись не найдена"}
    # Работа с сущностью курьер
    ENDPOINT_COURIER = "api/v1/courier" # Courier - Создание курьера
    RESPONSE_COURIER_BAD_REQUEST = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
    RESPONSE_COURIER_CONFLICT = {"code": 409, "message": "Этот логин уже используется"}
    #Работа с заказом
    ENDPOINT_ORDER = "api/v1/orders" # Orders - Создание заказа и получение заказа
    BASE_ORDER_PAYLOAD = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": []
    }


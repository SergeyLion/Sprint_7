

class Settings:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    ENDPOINT_AUTH_COURIER = "api/v1/courier/login" # Courier - Логин курьера в системе
    ENDPOINT_COURIER = "api/v1/courier" # Courier - Создание курьера
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


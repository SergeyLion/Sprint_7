# Sprint_7

## Описание
Этот проект представляет собой набор тестов API для сервиса Яндекс Самокат. Он проверяет:
- Создание курьера.
- Авторизацию курьера.
- Работу с заказами.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/SergeyLion/Sprint_7.git
   
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt

3. Запустить тесты
   ```bash
   pytest tests/
   
4. Собрать отчет в allure:
   ```bash
   pytest .\tests --alluredir=allure_results
   
5. Открыть отчет allure:
   ```bash
   allure serve allure_results
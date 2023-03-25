import requests

# URL для запросов
URL = 'https://bab66b22-42a3-47c4-b86b-7ab536ef5477.serverhub.praktikum-services.ru'

# Ключ для создания заказа
create_order_url = '/api/v1/orders'


def test_create_and_get_order():
    # создание заказа
    create_order = URL + create_order_url
    headers = {'Content-Type': 'application/json'}
    order_data = {
        "firstName": "Olga",
        "lastName": "Uchiha",
        "address": "Moscow",
        "metroStation": 4,
        "phone": "+78003333333",
        "rentTime": 5,
        "deliveryDate": "2023-03-26",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }
    response = requests.post(create_order, headers=headers, json=order_data)

    track_number = response.json().get('track')

    # запрос на получения заказа по треку заказа
    retrieve_order_url = URL + f'/v1/orders/track?t={track_number}'
    response = requests.get(retrieve_order_url)
    # Проверка кода ответа
    assert response.status_code == 200

    print(response.status_code)

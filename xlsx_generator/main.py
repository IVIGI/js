import pandas as pd
from faker import Faker
import random
from datetime import datetime

# Настройки генерации
fake = Faker('ru_RU')  # Русская локализация для фейкера
NUM_ROWS = 100  # Количество строк. Можешь сделать меньше или больше
START_DATE = '2024-01-01' # Дата начала продаж. Формат год-месяц-день
END_DATE = '2025-01-31' # Дата конца продаж

# Списки для генерации. Тут можешь написать свои товары и города
PRODUCTS = ['Ноутбук', 'Смартфон', 'Наушники', 'Планшет', 'Флешка', 'Монитор']
REGIONS = ['Москва', 'Воронеж', 'Санкт-Петербург', 'Казань', 'Новосибирск', 'Екатеринбург', 'Брянск', 'Орёл']


def generate_data(num_rows):
    data = []
    for _ in range(num_rows):
        # Генерация даты
        date = fake.date_between_dates(
            date_start=datetime.strptime(START_DATE, '%Y-%m-%d'),
            date_end=datetime.strptime(END_DATE, '%Y-%m-%d')
        ).strftime('%Y-%m-%d')

        # Генерация товара и цены
        product = random.choice(PRODUCTS)
        price = random.randint(1000, 50000) # Цена товара. Можешь поменять диапазон
        quantity = random.randint(1, 5) # Кол-во товара, также можно поменять диапазон

        # Расчет суммы
        total = price * quantity

        data.append({
            'Дата': date,
            'Товар': product,
            'Количество': quantity,
            'Цена': price,
            'Сумма': total,
            'Регион': random.choice(REGIONS)
        })

    return data


# Создание pandas DataFrame
df = pd.DataFrame(generate_data(NUM_ROWS))

# Сохранение в Excel
filename = input("Введите имя файла без .xlsx: ")
df.to_excel(f'{filename}.xlsx', index=False, engine='openpyxl')
print(f'Файл "{filename}.xlsx" с {NUM_ROWS} записями создан!')
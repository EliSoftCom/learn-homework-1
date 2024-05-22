"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""


def forms_in_par(text_title: str):
    print('*' * len(text_title))
    print(text_title)
    print('*' * len(text_title))


def main(products: list):
    forms_in_par("Количество продаж для каждого товара")
    for dict_temp in products:
        product = dict_temp['product']
        sales = dict_temp['items_sold']
        print(f"Текущий продук - {product}:\nБыл продан общим числом - {sum(sales)}")
        print()

    forms_in_par("Среднее количество продаж для каждого товара")

    for dict_temp in products:
        product = dict_temp['product']
        sales = dict_temp['items_sold']
        print(f"Средние продажи товара {product} за месяц: {int(sum(sales)/len(sales))}")
        print()

    forms_in_par("Суммарное количество продаж всех товаров")

    sum_product = 0
    for dict_temp in products:
        sales = dict_temp['items_sold']
        sum_product += sum(sales)
    print(f"Суммарные продажи - {sum_product} шт.")
    print()

    forms_in_par("Cреднее количество продаж всех товаров за месяц")

    for i in range(12):
        sales_month_total = 0
        for dict_temp in products:
            sales_month = dict_temp['items_sold'][i]
            sales_month_total += sales_month
        print(f"Средние продажи всех товаров за {i+1} месяц: {int(sales_month_total / len(products))}")


if __name__ == "__main__":
    products = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    main(products)

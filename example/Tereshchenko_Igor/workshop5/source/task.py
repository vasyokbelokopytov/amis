# Створити dataset та працювати з ним
from example.Tereshchenko_Igor.workshop5.source.dataset_handle.handler import create_dataset
import plotly
import plotly.graph_objs as go

dataset = create_dataset('data/orders.csv')


# Які продукти купляли усі покупці?

user_product = dict()

for client in dataset:
    user_product[client] = set()

    for date in dataset[client]:
        user_product[client].update( set(dataset[client][date].keys()) )

orders = list( user_product.values() )
common_products_set = orders[0]

for order in orders:
    common_products_set = common_products_set.intersection(order)

print("Task 1: ",common_products_set)



# Як змінювалась ціна на яблука? (графік)
from datetime import datetime

apple_date_price = dict()

for client in dataset:
    for date in dataset[client]:
        if 'apple' in dataset[client][date]:

            datetime_object = datetime.strptime(date, '%d.%m.%Y')

            apple_date_price[datetime_object] = dataset[client][date]['apple']['price']

print("Task 2: ",apple_date_price)

data = go.Scatter(x=list(apple_date_price.keys() ), y=list(apple_date_price.values()))
plotly.offline.plot([data], filename='apple.html')


# Скільки грошей витрачає кожний покупець на покупки? (графік)

user_expenses = dict()
for client in dataset:
    user_expenses[client] = 0
    for date in dataset[client]:
        for product in dataset[client][date]:
            user_expenses[client] += float(dataset[client][date][product]['price'])*float(dataset[client][date][product]['quantity'])

print("Task 3: ", user_expenses)

data = go.Bar(x=list(user_expenses.keys() ), y=list(user_expenses.values()))
plotly.offline.plot([data], filename='user_expenses.html')


# Який найпопулярніший товар?
# Якого товару було куплено найменше?

product_popularity = dict()
for client in dataset:
    for date in dataset[client]:
        for product in dataset[client][date]:
            if product not in product_popularity:
                product_popularity[product] = 0

            product_popularity[product] += float(dataset[client][date][product]['quantity'])

products = list(product_popularity.keys())
quantities = list(product_popularity.values())
max_quantities = max(quantities)
min_quantities = min(quantities)

index_max = quantities.index(max_quantities)
index_min = quantities.index(min_quantities)


print("Task 4: ",product_popularity,products[index_max],products[index_min])


# Який найдорожчий товар?
product_price = dict()
for client in dataset:
    for date in dataset[client]:
        for product in dataset[client][date]:
            product_price[product] = float(dataset[client][date][product]['price'])

products = list(product_price.keys())
prices = list(product_price.values())
max_price = max(prices)

index_max = prices.index(max_price)

print("Task 5: ", products[index_max], max_price)


# Якого товару, скільки покупців купляє? (графік)
product_user = dict()
for client in dataset:
    for date in dataset[client]:
        for product in dataset[client][date]:
            if product not in product_user:
                product_user[product] = 0

            product_user[product]+=1

data = go.Bar(x=list(product_user.keys() ), y=list(product_user.values()))
plotly.offline.plot([data], filename='product_user.html')


# Написати функціонал для додавання нових даних
#TODO
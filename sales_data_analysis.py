from asyncio import queues
from functools import reduce


sales_data = [
    ("Q1", [("Jan", 1000), ("Feb", 1200), ("Mar", 1100)]),
    ("Q2", [("Apr", 1300), ("May", 1250), ("Jun", 1400)]),
    ("Q3", [("Jul", 1350), ("Aug", 1450), ("Sep", 1300)])
]
for i in sales_data:
    quarter,sales = i
    total = reduce(lambda x,y: x+y, [sales for _,sales in sales])
    print(f"{quarter} total sales: {total}")

print("-"*20)
all_months = [months for _,months in sales_data for months in months]
print(all_months)
print("-"*20)
print(max([sale for _,sale in all_months]))
print("-"*20)





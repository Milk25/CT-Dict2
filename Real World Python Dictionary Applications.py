restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}





restaurant_menu['Beverages'] = {'Pepsi': 2.99, 'Coke': 2.99}
print(restaurant_menu)
restaurant_menu['Main Course'].update({'Steak': 17.99})
print(restaurant_menu)


for value in restaurant_menu.values():
    print(value)




del restaurant_menu['Starters']['Bruschetta']
print(restaurant_menu)
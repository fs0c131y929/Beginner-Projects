delicious_menu = {

    'Hot Dog': 11.50, 
    'Slice of Pizza' : 1.99,
    'Whole Pizza' : 9.95,
    'Soft Drink' : 0.59

}



hot_dog = int(input('Please enter the number of Hot Dogs: '))
pizza_slice = int(input('Please enter the number of Pizza Slices: '))
whole_pizza = int(input('Please enter the number of Whole Pizzas: '))
soft_drinks = int(input('Please enter the number of Soft Drinks: '))

total = delicious_menu['Hot Dog'] + delicious_menu['Slice of Pizza'] + delicious_menu ['Soft Drink'] + delicious_menu ['Whole Pizza']
print('The total cost of the order is: ', '$',total)
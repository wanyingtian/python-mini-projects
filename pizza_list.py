'''
this script helps practice the basic list manipulations
the scenario is a pizza place trying to origanize their list of pizzas
'''
#1D lists
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives","anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

#Count the number of occurrences of 2 in the prices list
num_two_dollar_slices = prices.count(2)

#Find the length of the toppings list
num_pizzas = len(toppings)
print("We sell %d different kind of pizza!" % num_pizzas)

#2-d list
pizza_and_prices = [[2,	"pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7 , "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)

#sorting and slicing pizzas
pizza_and_prices.sort()
print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

#someone bought last slice of anchovies, remove most expensive pizza
pizza_and_prices.pop()

#add peppers
pizza_and_prices.insert(4,[2.5, "peppers"])
print(pizza_and_prices)

#find 3 cheapest pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
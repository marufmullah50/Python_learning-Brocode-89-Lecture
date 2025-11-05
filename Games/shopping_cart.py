foods =[]
prices =[]
total=0
while True:
    food= input("Enter a food item :")
    if food.lower() == 'q': # q to quit
        break
    else:
        price = float(input(f"Enter the price of {food}:$ "))
        foods.append(food)
        prices.append(price)
        

print ("-------- Shopping Cart --------")
for food in foods:
    print(food)
for price in prices:
    total += price
print(f"Total Price: ${total:.2f}")

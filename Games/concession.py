#Concession Stand Program

menu ={
    "Hot Dog": 2.50,
    "Burger": 3.00,
    "Fries": 1.50,
    "Soda": 1.00,
    "Candy": 0.75,
    "Nachos": 2.00,
    "chicken_nuggets": 3.50,
    "Ice Cream": 2.25,
    "Popcorn": 1.75
}
# to keep track
cart = []
total = 0
# key , value instead of one variable like i
#Thats why it will loop for two variables key and value instead of one like i usually

print("-------- Menu -----------")
for key, value in menu.items():
    print(f"{key}: ${value:.2f}")

print("------------------------")
while True:
    food = input("Enter the food item you want to order (or type 'q' to finish): ").lower()# to  ensure quit
    if food == 'q':
        break
    elif food.title() in menu:
        cart.append(food.title())
    else:
        print("Item not found in the menu. Please try again.")

print("\n-------- Your Order -----------")
for item in cart:
    print(f"- {item}: ${menu[item]:.2f}")
    total += menu[item]

print(f"Total: ${total:.2f}")
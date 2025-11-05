principal = 0
rate = 0
time = 0
while principal <= 0:
    principal = float(input("Enter the principal amount : "))
    if principal <= 0:
        print("Principal amount can't be less than zero.")

while rate <= 0:
    rate = float(input("Enter the rate of interest : "))
    if rate <= 0:
        print("Rate of interest can't be less than zero.")

while time <= 0:
    time = float(input("Enter the time period (in years) : "))
    if time <= 0:
        print("Time period can't be less than zero.")
total_amount = principal * (1 + (rate / 100) * time)
print(f"The total amount after {time} years is: {total_amount:.2f}")
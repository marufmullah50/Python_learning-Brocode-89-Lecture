conversion= int(input("Conversion Category : \n 1.Weight conversioncle\n2.Temperature conversion:"))
if conversion ==1 :
    type_of_conversion = int(input("Convert from: \n1.kg to lb \n 2. lb to kg"))
    if type_of_conversion == 1:
        kg =float(input("Enter weight in kg: "))
        lb = kg * 2.20462
        print(f"{kg} kg is equal to {lb} lb")
    elif type_of_conversion == 2: 
        lb =float(input("Enter weight in lb: "))
        kg = lb / 2.20462
        print(f"{lb} lb is equal to {kg} kg")
elif conversion == 2:
    type_of_conversion = int(input("Convert from:\n 1. Celsius to Fahrenheit \n 2. Fahrenheit to Celsius " 
                            "\n 3. Celsius to Kelvin \n 4. Kelvin to Celsius \n 5. Fahrenheit to Kelvin \n 6. Kelvin to Fahrenheit"))
    if type_of_conversion == 1:
       celsius = float(input("Enter temperature in Celsius: "))
       fahrenheit = (celsius * 9/5) + 32
       print(f"{celsius} °C is equal to {fahrenheit} °F")
    elif type_of_conversion == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} °F is equal to {celsius} °C")
    elif type_of_conversion == 3:
         celsius = float(input("Enter temperature in Celsius: "))
         kelvin = celsius + 273.15
         print(f"{celsius} °C is equal to {kelvin} K")
    elif type_of_conversion == 4:
         kelvin = float(input("Enter temperature in Kelvin: "))
         celsius = kelvin - 273.15
         print(f"{kelvin} K is equal to {celsius} °C")
    elif type_of_conversion == 5:
         fahrenheit = float(input("Enter temperature in Fahrenheit: "))
         kelvin = (fahrenheit - 32) * 5/9 + 273.15
         print(f"{fahrenheit} °F is equal to {kelvin} K")
    elif type_of_conversion == 6:
         kelvin = float(input("Enter temperature in Kelvin: "))
         fahrenheit = (kelvin - 273.15) * 9/5 + 32
         print(f"{kelvin} K is equal to {fahrenheit} °F")
else:
    print("Invalid conversion category selected.")
print("Conversion completed.")
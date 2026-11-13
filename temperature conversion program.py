unit = input("enter the unit (c for celsius or f for fahrenheit): ")
if unit == "c":
    temperature = flaot(input("enter the temperature in celsius: "))
    converted_temperature = (temperature * 9 / 5) + 32
    print(f"the temperature in fahrenheit is {converted_temperature} f")

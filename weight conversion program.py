# python weight converter
weight=float(input("enter the weight"))
unit=input("enter the unit (K for kilograms or L for pounds)")
if unit=="K":
    weight=weight*2.205
    unit="lbs."
    print(f"the weight in pounds is {weight} {unit}")
elif unit=="L":
        weight=weight/2.205
        unit="kgs."
        print(f"the weight in kilograms is {weight} {unit}")
else:
    print(f"the unit {unit} is not valid. Please enter K for kilograms or L for pounds.")
print(f"your new converted weight is {weight} {unit}")

weight = input("Enter your weight in kg: ")
height = input("Enter your height in m: ")


weight_as_integer = int(weight)
height_as_float = float(height)

bmi = weight_as_integer / height_as_float**2
print(int(bmi))

if bmi < 18.5:
    print(f"your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"your bmi is {bmi}, your have normal weight")
elif bmi < 30:
    print("your bodyweigt is sligtly")
elif bmi < 35:
    print("you are obese")
else:
    print("you are clinical obese")

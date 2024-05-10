height = int(input("Please enter your height in cm.\n"))
weight = int(input("Please enter your weight in kg\n"))

height_in_meter = height/100

bmi = weight / height_in_meter ** 2

bmi_rounded = round(bmi,2)

print("Your bmi is", bmi_rounded)
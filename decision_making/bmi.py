weight_in_kg=int(input("Enter weight in kg"))
height_in_cm=int(input("Enter height in cm"))
height_in_meter=(height_in_cm/100)
bmi=(weight_in_kg)/height_in_meter**2
print(f"bmi={bmi}")
if bmi<19:
    print("Under Weight")
elif bmi<25:
    print("Healthy")
elif bmi<30:
    print("Over Weight")
elif bmi<40:
    print("Obesity")
elif bmi>40:
    print("Severe Obese")
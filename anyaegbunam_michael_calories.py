age = float(input("Please enter your age: "))
weight = int(input("Please enter your weight in pounds: "))
heart_rate = int(input("Please enter your heart rate in beats per miniute: "))
time = int(input("Please enter the length of your workout in minutes: "))

caloriesburned = (age * 0.2757 + weight * 0.03295 + heart_rate * 1.0781 - 75.4991) * time // 8.368
print ("Calories burned: ")
print ("caloriesburned", caloriesburned)
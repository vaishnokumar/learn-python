# height = input("Enter Your Height: ")
# weight = input("Enter Your Weight: ")
# height = int(height)
# weight = float(weight)
# BMI = weight/(height/100)**2
# if BMI >= 30:
#     print("You are Obese")
# elif 25 < BMI < 29:
#     print("You are Overweight")
# elif 18.5 < BMI < 25:
#     print("You are perfectly Normal!")
# elif BMI <= 18.5:
#     print("You are Underweight")
# else:
#     print()

India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York","Chicago","Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]

city = input("Enter City Name: ")
if city in India:
    print(f' {city} is present in India')
elif city in USA:
    print(f' {city} is present in USA')
elif city in UK:
    print(f' {city} is present in UK')
else:
    print("Unknown City")
  


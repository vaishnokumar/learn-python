India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York", "Chicago", "Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]

city1 = input("Enter First City: ")
city2 = input("Enter Second City: ")
if city1 in India and city2 in India:
    print("Both Cities Belong To IN ")
elif city1 in USA and city2 in USA:
    print("Both Cities Belong To USA ")
elif city1 in UK and city2 in UK:
    print("Both Cities Belong To UK")
else:
    print("Unknown City")

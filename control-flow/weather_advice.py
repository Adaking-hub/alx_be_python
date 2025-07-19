# weather_advice.py
# Weather recommendation app

# Prompt User for Weather Input
weatherToday = input("What's the weather like today? (sunny/rainy/cold): ")

# Provide Clothing Recommendations
if weatherToday == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weatherToday == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weatherToday == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
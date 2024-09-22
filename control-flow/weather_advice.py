# weather_advice.py

# Prompt the user for the current weather condition
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Check for the "sunny" condition
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
# Check for the "rainy" condition
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
# Check for the "cold" condition
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
# Handle unexpected input with an else statement
else:
    print("Sorry, I don't have recommendations for this weather.")

def temp():
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
    
celsius = int(input("Enter the temperature :"))
print(temp())
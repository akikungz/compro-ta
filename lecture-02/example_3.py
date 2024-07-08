# input temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# convert temperature to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# display the temperature in Fahrenheit
print("Temperature in Fahrenheit: {:.2f}".format(fahrenheit))
print("Temperature in Kelvin: {:.2f}".format(celsius + 273.15))
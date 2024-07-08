# Get the user's name, age, and income
name = input("Enter your name: ")
age = int(input("Enter your age: "))
income = float(input("Enter your income: "))

# Display the user's name, age, and income
print("Here is the data you entered:")
print(f"Name: {name}")
print(f"Age: {age}")
print("Income: {:12,.2f}".format(income))
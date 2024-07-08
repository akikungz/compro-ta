# Input weights and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate the BMI
bmi = weight / height ** 2

# Display the BMI
print(f"Your BMI is {bmi:.2f}")
string1, string2 = "Mary", "Mark"

if string1 == string2:
    print(f"{string1} is equal to {string2}.")
else:
    print(f"{string1} is not equal to {string2}.")
    
if string1 < string2:
    print(f"{string1} is less than {string2}.")
elif string1 > string2:
    print(f"{string1} is greater than {string2}.")
    
if string1.lower() == string2.lower():
    print(f"{string1} is equal to {string2} when case is ignored.")
else:
    print(f"{string1} is not equal to {string2} when case is ignored.")
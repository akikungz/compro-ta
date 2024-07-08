male_std = int(input("Enter count of male student: "))
female_std = int(input("Enter count of female student: "))

total_std = male_std + female_std

print(f"Male students in percentage: {male_std/total_std*100:.2f}%")
print(f"Female students in percentage: {female_std/total_std*100:.2f}%")
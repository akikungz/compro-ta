worked_hours = int(input("Enter worked hours: "))
hourly_rate = int(input("Enter hourly rate: "))

gross_pay = worked_hours * hourly_rate

if worked_hours > 40:
    over_time = worked_hours - 40
    gross_pay += over_time * 0.5 * hourly_rate
    
print(f"Gross pay: ${gross_pay:,.2f}")

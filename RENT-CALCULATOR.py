# This is the rent calculator program in Python

"""
Electricity bill
Water bill
Gas bill
WiFi bill
Flat maintenance bill
Grocery bill
"""

print("ENTER THE AMOUNT OF ALL THE HOUSEHOLD BILLS")
print("")

try:
    electricity_bill = int(input("ENTER THE ELECTRICITY BILL = "))
    water_bill = int(input("ENTER THE WATER BILL = "))
    wifi_bill = int(input("ENTER THE WIFI BILL = "))
    flat_maintenance_bill = int(input("ENTER THE FLAT MAINTENANCE BILL = "))
    grocery_bill = int(input("ENTER THE GROCERY BILL = "))

    total_sum = electricity_bill + water_bill + wifi_bill + flat_maintenance_bill + grocery_bill
    print(f"Total sum of bills: {total_sum}")

    members = int(input("ENTER THE NUMBER OF MEMBERS TO DIVIDE THE TOTAL: "))
    if members > 0:
        print(f"The total division for {members} members is: {total_sum / members}")
    else:
        print("Number of members must be greater than 0.")
except ValueError:
    print("Please enter valid numeric values.")

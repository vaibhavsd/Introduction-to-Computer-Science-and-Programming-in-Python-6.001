annual_salary= float(input("Enter your annual salary: "))

portion_saved= float(input("Enter the percent of your salary to save, as a decimal: "))

total_cost= float(input("Enter the cost of your dream home: "))

increment = float(input("Enter the semiannual raise, as a decimal: "))

r = 0.04
ms = annual_salary/12
current_saving = 0
months = 0
portion_down_payment = 0.25

down_payment= total_cost*portion_down_payment
counter = 0

while current_saving < down_payment:
    if counter is 6:
        counter = 0
        ms += ms*increment
    current_saving = current_saving + (portion_saved*ms) + (current_saving*r/12)
    months += 1
    counter += 1

print("Number of Months required for down payment:", months)
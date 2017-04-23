annual_salary= float(input("Enter your annual salary: "))

portion_saved= float(input("Enter the percent of your salary to save, as a decimal: "))

total_cost= float(input("Enter the cost of your dream home: "))

r = 0.04
ms = annual_salary/12
current_saving = 0
months = 0
portion_down_payment = 0.25

down_payment= total_cost*portion_down_payment

while current_saving < down_payment:
    current_saving = current_saving + (portion_saved*ms) + (current_saving*r/12)
    months += 1

print("Number of Months required for down payment:", months)
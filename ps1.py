annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25*total_cost
monthly_salary = annual_salary/12
current_savings = 0.0
annual_return = 0.04

month_count = 0
while portion_down_payment > current_savings :
    month_count = month_count + 1
    current_savings = current_savings + portion_saved*monthly_salary + current_savings*annual_return/12

print("Number of months:", month_count)
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04

target_down_payment = total_cost * portion_down_payment
saved_from_salary_per_month = (annual_salary / 12) * portion_saved

month_counter = 0

while current_savings < target_down_payment:
    investment_earnings_this_month = (current_savings * r) / 12
    total_contribution_this_month = (
        saved_from_salary_per_month + investment_earnings_this_month
    )
    current_savings += total_contribution_this_month
    month_counter += 1

print(f"Number of months: {month_counter}")

# to be able to afford a down payment in three years, how much should you save each month?

annual_salary = float(input("Enter your annual salary: "))

MONTHS_IN_YEAR: int = 12

# starting assumptions
semi_annual_raise: float = 0.07
investment_return: float = 0.04
down_payment_target: float = 0.25
cost_of_house: int = 1_000_000
savings_goal: float = cost_of_house * down_payment_target

# target information
target_months: int = MONTHS_IN_YEAR * 3
target_accuracy_tolerance: int = 100


# get number of months for target
def savings_after_n_months(number_of_months: int, savings_rate: float):
    total_saved: int = 0
    current_salary: float = annual_salary
    for month_counter in range(number_of_months):
        investment_earnings_this_month = (total_saved * investment_return) / 12
        if month_counter % 6 == 0 and month_counter != 0:
            current_salary += current_salary * semi_annual_raise
        saved_from_salary_per_month = int((current_salary / 12) * savings_rate)
        total_saved += int(saved_from_salary_per_month + investment_earnings_this_month)
        month_counter += 1
    return total_saved


# bisection search
def get_guess(bound1: float, bound2: float):
    return (bound1 + bound2) / 2


low: float = 0
high: float = 1
guessed_savings_rate: float = get_guess(low, high)
resulting_savings = savings_after_n_months(target_months, guessed_savings_rate)
num_of_guesses: int = 1

if resulting_savings < savings_goal:
    print("It is not possible to pay the down payment in three years.")
else:
    while abs(resulting_savings - savings_goal) >= target_accuracy_tolerance:
        num_of_guesses += 1
        if resulting_savings > savings_goal:
            high = guessed_savings_rate
        else:
            low = guessed_savings_rate
        guessed_savings_rate = get_guess(low, high)
        resulting_savings = savings_after_n_months(target_months, guessed_savings_rate)

    print(f"Best savings rate {round(guessed_savings_rate, 4)}")
    print(f"Steps in bisection search: {num_of_guesses}")

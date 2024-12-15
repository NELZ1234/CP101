
def calculate_bonus(years, department, bonus_high, bonus_low):
    if years >= 10:
        return bonus_high
    elif years > 0:
        return bonus_low
    else:
        print(f"Sorry, no bonus in {department}!")
        return 0

years_in_IT = float(input("Years of service in IT Department: "))
years_in_ACCT = float(input("Years of service in ACCT Department: "))
years_in_HR = float(input("Years of service in HR Department: "))

#to calculatw
bonus_IT = calculate_bonus(years_in_IT, "IT", 10000, 5000)
bonus_ACCT = calculate_bonus(years_in_ACCT, "ACCT", 12000, 6000)
bonus_HR = calculate_bonus(years_in_HR, "HR", 15000, 7500)

#total
total_bonuses = bonus_IT + bonus_ACCT + bonus_HR
print(f"Total bonuses from all departments: {total_bonuses}")

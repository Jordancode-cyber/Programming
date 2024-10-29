def main():
    principal = float(input("Enter the initial principal: "))
rate = float(input("Enter the annual interest rate (as a decimal): "))
years = int(input("Enter the number of years: "))
annual_investment = float(input("Enter the yearly investment amount: "))
for i in range(years):
    principal = (principal + annual_investment) * (1 + rate)
print(f"The total amount after {years} years is:", principal)
main()
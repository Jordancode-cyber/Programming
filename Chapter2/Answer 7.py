def main():
    principal = float(input("Enter the initial principal: "))
rate = float(input("Enter the annual nominal rate (as a decimal): "))
periods = int(input("Enter the number of compounding periods per year: "))
years = int(input("Enter the number of years: "))
for i in range(years * periods):
    principal = principal * (1 + rate / periods)
print(f"The amount after {years} years is:", principal)
main()
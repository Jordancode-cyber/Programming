def main():
    principal=float(input("enter principal initial value:" ))
    rate= float(input("enter annual interest rate (as a decimal):"))
    years= int(input("enter number of years:"))
    for i in range(years):
        principal=principal * (1 + rate)
        print(f"amount after{years} years is:",principal)
main()
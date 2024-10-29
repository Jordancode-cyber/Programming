def main():
    print("Celsius to Fahrenheit Conversion Table")
for celsius in range(0, 101, 10):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")
main()
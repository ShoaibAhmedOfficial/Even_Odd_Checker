user_input = input("Enter a number: ")

try:
    num = int(user_input)   # Try converting to integer
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

except ValueError:
    print("Invalid input! Please enter an integer (no letters or Decimal value or symbols).")

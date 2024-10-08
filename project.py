# This function adds two numbers
def tambahan(x, y):
    return x + y

# This function subtracts two numbers
def pengurangan(x, y):
    return x - y

# This function multiplies two numbers
def perkalian(x, y):
    return x * y

# This function divides two numbers
def pembagian(x, y):
    return x / y


print("pilih pengoprasian")
print("1.tambahan")
print("2.perngurangan")
print("3.perkalian")
print("4.pembagian")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", tambahan(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", pengurangan(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", perkalian(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", pengurangan(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
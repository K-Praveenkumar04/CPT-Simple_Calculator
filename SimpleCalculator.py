#SimpleCalculator
#fix output
def addition(x, y):
   return x + y
def multiplication(x, y):
   return x * y
def division(x, y):
   return x / y
def raisePower(x, y):
   return x ** y
#print("Operation to perform:")
#print("For addition, enter 1")
#print("For subtraction, enter 2")
#print("For multiplication, enter 3")
#print("For division, enter 4")
#print("For raising to a power, enter 5")

choice = input("Enter choice: ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == '1':
   print(num1, "+" ,num2, "=", addition(num1, num2))

elif choice == '2':
   print(num1, "-", num2, "=", subtraction(num1, num2))

elif choice == '3':
   print(num1, "*", num2, "=", multiplication(num1, num2))

elif choice == '4':
   print(num1, "/", num2, "=", division(num1, num2))

elif choice == '5':
   print(num1, "**", num2, "=", raisePower(num1, num2))

else:
   print("Please select a valid input.");

   print (answer)()

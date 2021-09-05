# main.py

print("Welcome to the calculator!\n")
operation = input("Choose an operation to get started (+, -, *, /, ^, !): ")

while True:
  if operation == "+":
    #num1 = int(input("Enter the first number: "))
    #num2 = int(input("Enter the second number: "))
    #num3 = int(input("Enter the third number: "))
    #num4 = int(input("Enter the fourth number: "))
    #num5 = int(input("Enter the fifth number: "))
    
    amount = input("How many numbers are being inputted? The max is 5: ")
    if amount == '2':
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      print("Your solution is " + str(num1 + num2))
    elif amount == '3':
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      num3 = int(input("Enter the third number: "))
      print("Your solution is " + str(num1 + num2 + num3))
    elif amount == '4':
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      num3 = int(input("Enter the third number: "))
      num4 = int(input("Enter the fourth number: "))
      print("Your solution is " + str(num1 + num2 + num3 + num4))
    elif amount == '5':
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      num3 = int(input("Enter the third number: "))
      num4 = int(input("Enter the fourth number: "))
      num5 = int(input("Enter the fifth number: "))
      print("Your solution is " + str(num1 + num2 + num3 + num4 + num5))
    else:
      print("Sorry, not supported! Try a number between 2-5 instead.")


  elif operation == '-':
    amount = input("How many numbers are being inputted? The max is 5: ")
    if amount == '2':
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      print("Your solution is " + str(num1 - num2))
    elif amount == '3':
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      num3 = int(input("Enter the third number: "))
      print("Your solution is " + str(num1 - num2 - num3))
    elif amount == '4':
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      num3 = int(input("Enter the third number: "))
      num4 = int(input("Enter the fourth number: "))
      print("Your solution is " + str(num1 - num2 - num3 - num4))
    elif amount == '5':
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      num3 = int(input("Enter the third number: "))
      num4 = int(input("Enter the fourth number: "))
      num5 = int(input("Enter the fifth number: "))
      print("Your solution is " + str(num1 - num2 - num3 - num4 - num5))
    else:
      print("Sorry, not supported! Try a number between 2-5 instead.")
    

  elif operation == '*':
    amount = input("How many numbers are being inputted? The max is 5: ")
    if amount == '2':
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      print("Your solution is " + str(num1 * num2))
    elif amount == '3':
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      num3 = int(input("Enter the third number: "))
      print("Your solution is " + str(num1 * num2 * num3))
    elif amount == '4':
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      num3 = int(input("Enter the third number: "))
      num4 = int(input("Enter the fourth number: "))
      print("Your solution is " + str(num1 * num2 * num3 * num4))
    elif amount == '5':
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      num3 = int(input("Enter the third number: "))
      num4 = int(input("Enter the fourth number: "))
      num5 = int(input("Enter the fifth number: "))
      print("Your solution is " + str(num1 * num2 * num3 * num4 * num5))
    
  elif operation == '/':
    amount = input("How many numbers are being inputted? The max is 5: ")
    if amount == '2':
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      print("Your solution is " + str(num1/num2))
    elif amount == '3':
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      num3 = int(input("Enter the third number: "))
      print("Your solution is " + str(num1/num2/num3))
    elif amount == '4':
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      num3 = int(input("Enter the third number: "))
      num4 = int(input("Enter the fourth number: "))
      print("Your solution is " + str(num1/num2/num3/num4))
    elif amount == '5':
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      num3 = int(input("Enter the third number: "))
      num4 = int(input("Enter the fourth number: "))
      num5 = int(input("Enter the fifth number: "))
      print("Your solution is " + str(num1/num2/num3/num4/num5))
    
  elif operation == '^':
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(num1 ** num2)
  
  elif operation == '!':
    w = int(input("Enter the number: "))
    def Factorial(w):
      factorials = 1
      for i in range(1, w + 1):
        factorials *= i
        return factorials
        print(Factorial(w))
  
  answer = input("\nWould you like to perform another operation? Enter 'y' for yes or 'n' for no: ")

  if answer == 'n':
    break    

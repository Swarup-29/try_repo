import math

def option():
    print("\n******************************************")
    print('           welcome to our program.          ')
    print("******************************************\n")
    print('1.Addition : ')
    print('2.Subtraction : ')
    print('3.Multiplication : ')
    print('4.Division : ')
    print('5.Sin(x) : ')
    print('6.Cos(x) : ')
    print('7.Tan(x) : ')
    print('8.Factorial : ')
    print('9.Exit : \n')


def main():
    while True :
        option()
        choice = input("Enter your choice(If you want to exit than just enter 'exit') : ")

        if choice.lower() == 'exit' or choice == '9':
            print("\n******************** Thank you for using our program. ********************\n")
            break

        try:
            choice = int(choice)

            if choice == 1:
                num1 = float(input('Enter your 1st number: '))
                num2 = float(input('Enter your 2nd number: '))
                print(f"Result : {num1 + num2}")

            elif choice == 2:
                num1 = float(input('Enter your 1st number: '))
                num2 = float(input('Enter your 2nd number: '))
                print(f"Result : {num1 + num2}")

            elif choice == 3:
                num1 = float(input('Enter your 1st number: '))
                num2 = float(input('Enter your 2nd number: '))
                print(f"Result : {num1 * num2}")

            elif choice == 4:
                num1 = float(input('Enter your 1st number: '))
                num2 = float(input('Enter your 2nd number: '))
                if num2 != 0:
                    print(f"Result : {num1 / num2}")

                else:
                    print('Invalid input')

            elif choice == 5:
                num1 = float(input("Enter the value of Sin(x) : "))
                print(f"The value of Sin({num1}) : {math.sin(num1)}")

            elif choice == 6:
                num1 = float(input("Enter the value of Cos(x) : "))
                print(f"The value of Cos({num1}) : {math.cos(num1)}")

            elif choice == 7:
                num1 = float(input("Enter the value of Tan(x) : "))
                print(f"The value of Tan({num1}) : {math.tan(num1)}")


            elif choice == 8:
                num1 = int(input("Enter the number For factorial : "))
                fact = 1
                if num1 == 0 or num1 == 1:
                    print(f"The Factorial of {num1} : 1")

                elif num1 < 0:
                    print("invalid input")

                else:
                    for i in range(1,num1+1):
                        fact *= i

                    print(f"The Factorial of {num1} : {fact}")

            else:
                print("Please enter the number in between 1 to 9.")

        except ValueError as e:
            print("invalid input",e)

if __name__ == '__main__':
    main()








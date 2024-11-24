# calculator.py
# Vivian Li
# COP 3504C

#need to make spacings exact
import math

class calculator:
    '''We will make functions that will be called in the main function. Each one will return a float'''
    numlist = []  # class variable, will add the individual results for average

    def add():
        first = float(input("Enter first operand: "))
        second = float(input("Enter second operand: "))
        result = first + second
        calculator.numlist.append(result)
        return result

    def subtract():
        first = float(input("Enter first operand: "))
        second = float(input("Enter second operand: "))
        result = first - second
        calculator.numlist.append(result)
        return result

    def multiply():
        first = float(input("Enter first operand: "))
        second = float(input("Enter second operand: "))
        result = first * second
        calculator.numlist.append(result)
        return result

    def divide():
        first = float(input("Enter first operand: "))
        second = float(input("Enter second operand: "))
        if second == 0: #error trap divide by zero
            print("Cannot divide by zero.")
            return
        result = first / second
        calculator.numlist.append(result)
        return result

    def exponent():
        first = float(input("Enter first operand: "))
        second = float(input("Enter second operand: "))
        result = first ** second
        calculator.numlist.append(result)
        return result

    def log():
        first = float(input("Enter first operand: "))
        second = float(input("Enter second operand: "))
        #Error trapping
        if first == 0:
            print("\nError: Cannot find log base zero.")
            return
        elif second == 0:
            print("\nError: Undefined.")
            return
        elif second < 0:
            print("\nError: Can't find log of negative number.")
            return
        elif first < 0:
            print("\nError: Can't find log of negative base")
            return

        result = math.log(second, first) #math.log(x, base)
        calculator.numlist.append(result)
        return result


    def avg():
        numItems = len(calculator.numlist)
        if numItems == 0:  # if empty
            print("\nError: No calculations yet to average!")
        else:
            sum = 0
            for i in range(numItems):  # loop through the list to find sum of all calculations
                sum += calculator.numlist[i] #finding the sum
            print("\nSum of calculations:", sum)
            print("Number of calculations:", numItems)
            avg = sum / numItems
            return avg

def main():
    result = 0.0
    print("Current Result:", result)
    selection = 99
    print("""\nCalculator Menu \n---------------\n0. Exit Program\n1. Addition
2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm
7. Display Average""")

    while selection != 0:
        selection = int(input("\nEnter Menu Selection: "))  # enter invalid, doesn't repeat menu
        if selection == 0:
            print("\nThanks for using this calculator. Goodbye!")
            exit()
        elif selection == 1:
            result = calculator.add()
        elif selection == 2:
            result = calculator.subtract()
        elif selection == 3:
            result = calculator.multiply()
        elif selection == 4:
            result = calculator.divide()
        elif selection == 5:
            result = calculator.exponent()
        elif selection == 6:
            result = calculator.log()
        elif selection == 7:
            result = calculator.avg()
        else:
            print("\nError: Invalid selection!")
            continue  # breaks out of current iteration, should go back to beginning
        if selection != 7:
            print("\nCurrent Result:", result)
            print("""\nCalculator Menu \n---------------\n0. Exit Program\n1. Addition
2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm
7. Display Average""")
        elif selection == 7 and result != None:
            print("Average of calculations:", round(result, 2))

if __name__ == "__main__":
    main()
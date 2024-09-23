import math

"""def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test" """

"""3. Simple Calculator
Build a simple calculator that can perform basic arithmetic operations: addition, subtraction, multiplication, and division. The program should ask the user for two numbers and the operation they want to perform."""

# num1 = input("Enter an initial number: ")
# num2 = input("Enter an another number: ")
# operation = input("Enter an operation (+ - / %): ")

# def calc(num1, num2, operation):
#     if(operation == "+"):
#         return num1 + num2
#     elif(operation == "-"):
#         return num1 - num2
#     elif(operation == "/"):
#         return num1 / num2
#     elif(operation == "*"):
#         return num1 * num2
#     elif(operation == "%"):
#         return num1 % num2
#     else:
#         return "Operation is not recognized"

# assert calc(1,1,"+") == 2, "addition"
# assert calc(3,1,"-") == 2, "subtraction"
# assert calc(8,7,"*") == 56, "multiplication"
# assert calc(21,7,"/") == 3, "division"
# assert calc(22,7,"%") == 1, "modulus"
# print("Tests Passed")

# def sinApprox(argument):
#     sum = 0
#     for i in range (100):
#         numerator = pow(-1,i)*pow(argument,((2*i)+1))
#         denominator = math.factorial((2*i)+1)
#         sum += numerator / denominator 
#     print(sum)
#     return sum

# assert sinApprox(0) == 0, "Zero Case"
# assert sinApprox(1.047198) == 0.5, "60 Degree Case"
# assert sinApprox() == 0, "Zero Case"
# print("Tests passed")

def countA(str):
    numberOfA = 0
    for el in str:
        if (el == "A" or el == "a"):
            numberOfA += 1
    return numberOfA

assert countA("abacus") == 2, "ABACUS failed"
assert countA("aaaoooAAAOOO") == 6, "oaOA failed"
assert countA("this has no A's") == 2, "ironic sentence failed"
print("All Tests Passed")

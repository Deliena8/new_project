"""#class User:
New class"

def initialize(self, num_1, num_2, sign, result):
        self.num_1 = num_1
        self.num_2 = num_2
        self.result = result
        self.sign = sign

    #def get_number(self):
"The program gets the first numbers"
print("You need to type the first number to make calculation.")
num_1 = int(input())


        #def get_second_number(self):
"The program gets the second numbers"
print("You need to type the second number to make calculation.")
num_2 = int(input())

        #def get_sign(self):
"The program gets sign for calculation"
print("Inter please what you want to do with these numbers")
sign = (input)


#def calculation():
    #while True:
if sign == '+':
    result = int(num_1) + int(num_2)
    print(result.format(num_1, num_2)
elif sign =="-":
    result = int(num_2) - int(num_2)
    print(result)
elif sign =="*":
    result = int(num_2) * int(num_2)
    print(result)
elif sign =="/":
    result = int(num_2) / int(num_2)
    print(result)
else:
    print("Try again")"""

#calculation()

num_1 = int(input('Enter the first number'))
num_2 = int(input('Enter the second one'))

operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
if operation == '+':
    print('{} + {} = '.format(num_1, num_2))
    print(num_1 + num_2)
elif operation == '-':
    print('{} - {} = '.format(num_1, num_2))
    print(num_1 - num_2)
elif operation == '*':
    print('{} * {} = '.format(num_1, num_2))
    print(num_1 * num_2)
elif operation == '/':
    print('{} / {} = '.format(num_1, num_2))
    print(num_1 / num_2)
else:
    print('You have not typed a valid operator, please run the program again.')
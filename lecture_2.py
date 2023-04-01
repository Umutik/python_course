import sys

x = 3
# print(x > 3 or x < 8)
# print(x > 3 or x > 8)
# print(x > 3 and not x < 8)
# print(x > 3 and not x > 8)

#
# if x == 5:
#     print('Five')
# elif x >= 5:
#     print("more than five")
# else:
#     print("less than five")

# age = int(input('Please, enter your age '))
# if age >= 18:
#     print('Welcome')
# else:
#     print('Go home, baby!!')


# num1 = int(input('Number 1: '))
# num2 = int(input('Number 2 : '))
# operator = input('Operator: ')
# if num2 == 0 and operator == '/':
#     try:
#         result = num1 / num2
#         print(f'Result = {result}')
#     except ZeroDivisionError:
#         print('You cant divide to 0')
# else:
#     result = num1 + num2
#     print(f'result = {result}')

# num = 1
# while num < 5:
#     print(num)
#     num += 1


# message = "Hello"
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i, message)


# for i in range(6):
#     print(i)

# for i in range(1, 6, 4):
#     print(i)

# for i in "Hello":
#     print(i)

# def num():
#     return 2 * 2
#
# start = num()
# stop = 15
# step = 3
# for i in range(start, stop, step):
#     print(i)

# i = 0
# x = 0
#
# while i < 5:
#     print(i)
#     x += i
#     i += 1
#     print(f'x = {x}, i = {i}')



# message = ''
# if message:
#     print(message)
# else:
#     print('the string is empty')

# num = 10
# if num%2:
#     print("this number is odd")
# else:
#     print

def num(num1, num2):
    return num1 - num2

# print(num(9, 3))
start = num(10, 5)
stop = 15
step = 3
for i in range(start, stop, step):
    print(i)



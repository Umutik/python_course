#Lists

# my_list = [1, 'hello', 2.0, True, None]
# print(my_list)
# print(id(my_list))
# print(my_list[0])
# print(my_list[-1])
# my_list[0] = 2
# print(my_list)
# print(id(my_list))
# sentence = 'Python is awesome'
# print(sentence.split(' ', maxsplit=0))
# print(sentence[5])
# my_list.append(sentence)
# my_list.insert(1, 'inserted')
# print(my_list.count(1))
# print(my_list.index(1))
# print(len(my_list))
# my_list1 = [1, 2, 3, 4, 5, [1, 2, 3, 4,5, [1, 2]]]
# print(sum(my_list1))
# print(min(my_list1))
# print(max(my_list1))
# print(my_list1.count(5))
# print(my_list1[-1][-1][-1])
# print(my_list1.reverse())
# print(my_list1)

#For loop with list

# numbers = [1, 2, 3, 4, 5]
# # for num in numbers:
# #     print(num ** 2)
# new_i = [i * i for i in numbers if i % 2]
# print(new_i)
#secondoption
# new_l = [i for i in numbers if i % 2 == 0]
# print(new_l)

#.sort() and sorted()

# nums = [2, 3, 1, 5, 6, 4, 0]
# print(id(nums))
# print('sorted()')
# print(f'New sorted list: {sorted(nums)}')
# print(f'Initial Lists after sorting: {nums}')
# print(id(nums))
# print('SORT()')
# print(f'New sorted List: {nums.sort()}') #None
# print(f'Initial list after sorting: {nums}')
# print(id(nums))
# print(nums.reverse())
# print(nums)
# print(id(nums))


#Tuples
#Create a tuple: option 1
# my_tuple = 1, 2, 3
# print(my_tuple)
# print(type(my_tuple))

# #Create a tuple: option 2
# my_tuple = (1, True, 'name', None, 'name', 'name', 24)
# print(my_tuple)

#Create a tuple: option 3
# name = ('Mark'),
# print(name)
# print(type(name))

# my_tuple = ('apple', 'banana', 'cat')
# a, b, c = my_tuple
# print(a)
# print(b)
# print(c)
#
# letters = list(my_tuple)
# letters[0] = 'ananas'
# print(letters)

#Getting index of items
# my_tuple = (1, True, 'name', None, 'name', 'name', 25)
# print(my_tuple.index('name'))
# print(my_tuple.count('name'))

#Filtering
# my_tuple = (1, 'name', None, 'name', 'name', 25, True)
# result = tuple([item for item in my_tuple if isinstance(item, int)])
# print(result)

#Tuple methods
# print(f'Sum is: {sum(result)}')
# print(f'Max is: {max(result)}')
# print(f'Min is: {min(result)}')
# print(f'Lenght of my tuple is: {len(my_tuple)}')
# print(f'Lenght of result is: {(len(result))}')

#Iterate tuple with for loop
# for (index, item) in enumerate(my_tuple):
#     print(index, item)

#iterate tuple with while loop
# i = 3
# while i < len(my_tuple):
#     print(my_tuple[i])
#     i += 1

#Nested list in tuple
# fruits = ('apple', ['ananas', 'mango'], 'melon')
# fruits[1][0] = 'cherry'
# print(fruits)

#swaping variables
# a = 5
# b = 10
# a, b = b, a
# print(f'a = {a}')
# print(f'b = {b}')
# # print(a, b)

# Passing tuple as an argument in function
# def sum_it(*args):
#     total = 0
#     print(args)
#     for num in args:
#         total = total + num
#     return total
# print(sum_it(4, 5, 10, 6, 20))

# def sum_it(num1, num2, num3):
#     sum = num1 + num2 + num3
#     return sum
#
# print(sum_it(5, 10, 8))

# def func(*args):
#     l = []
#     print(len(args))
#     for item in args:
#         l.append(item * item)
#     return l
# print(func(2, 5, 6, 8, 10))



#Dictionaries
# my_dict = {
#     'name': 'Anna',
#     'last_name': 'Pavlova',
#     'age': 35,
#     'department': 'IT'
# }
# print(type(my_dict))
# print(my_dict)
# print(id(my_dict))
# print(my_dict['name'])
# my_dict['last_name'] = 'Smirnova'
# print(my_dict)
# print(len((my_dict)))
# my_dict['salary'] = 100000
# print(my_dict)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print(my_dict.pop('department'))
# print(my_dict)
# print(my_dict.get('department', 'Not found'))
# print(my_dict.get('age'))

# keys = ['name', 'salary', 'department']
# values = ['Alex', '100000', 'Finance']
# employee = dict(zip(keys, values))
# print(employee)

# employee1 = dict(name ='John', position = 'developer', salary = 220000, department = 'IT', state = 'Florida')
# print(employee1)

#Sets

# my_list = [1, 8, 2, 1, 1, 5, 5, 8, 9, 9]
# print(set(my_list))

# set1 = {1, 2, 3, 'one', 'ten', 6}
# set2 = {1, 2, 3, 'one', 'ten', 100, 525}
# set3 = {1, 2, 3}

# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# print(set2.intersection(set1))
# print(set2.difference(set1))
# print(set1.symmetric_difference(set2))

# print(set1)
# print(id(set1))
# print(set1.remove(1))
# #removed 1, but brings None. if you print it again you will see that there is no more 1.
# print(set1)
# print(id(set1))
# print(set1.add(8))
# print(set1)
# print(id(set1))

# fs = frozenset({1, 2, 3})
# print(fs)
# fs.remove(1)
# print(fs)










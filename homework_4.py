# 4.1
from math import sqrt
def square(side):
  return (side**2, side*4, round(sqrt(side**2*2), 2))

# 4.2
# def employee(*args):


#4.3
my_list = [20, -3, 15, 2, -1, -21]
filtered = list(filter(lambda x: x >= 0, my_list))
print(filtered)

# 4.4
# from functools import reduce
# result = reduce(lambda x, y: x * y, my_list)
# print(result)

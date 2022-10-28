import array as arr
import math
import random

numbers = arr.array('i',[])
numbers_rt = arr.array ('i', [])

for i in range (50):
    numbers.append(random.randint(0,100))

for number in numbers:					# нужно прбежаться по массиву
  if (math.sqrt(number)%1) == 0:
    numbers_rt.append (int(math.sqrt(number)))

print(numbers)						# нужно прбежаться по массиву
print(numbers_rt)					# нужно прбежаться по массиву
print(max(numbers_rt))

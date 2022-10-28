import array as arr
import random

numbers = arr.array('i',[])
n_size  = 3

for i in range (n_size):				# нужно пробежаться по массиву: O (n)
  numbers.append(random.randint(0,9)) # генерируем массив из из целых чисел от 0 до 9.

result = 0;

for ii in range (n_size):				# нужно пробежаться по массиву: O (n)
  result ^= numbers [ii]

print(numbers)						# нужно пробежаться по массиву: O (n)
#print(result)

if (result & 1) == 0:					# O(1)
  print ("число", result, "чётное")
else:
  print ("число", result, "нечётное")

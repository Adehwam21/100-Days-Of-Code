import math

list1 = [1, 2, 4, 6, 8, 4]

sum_list = 0
counter = 0
summation = 0

for i in list1:
    sum_list += i
    counter += 1
avg = sum_list / counter

for num in list1:
    summation += (num - avg) * (num - avg)

pop_std = math.sqrt(summation / counter)
print(round(pop_std, 4))

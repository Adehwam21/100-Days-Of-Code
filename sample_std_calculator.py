import math

list1 = [3, 7, 4, 8, 6]

sum_list = 0
counter = 0
summation = 0

for i in list1:
    sum_list += i
    counter += 1
avg = sum_list / counter

for num in list1:
    summation += (num - avg) * (num - avg)

pop_std = math.sqrt(summation / counter - 1)
print(round(pop_std, 4))

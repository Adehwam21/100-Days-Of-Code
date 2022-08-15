num = int(input("Enter number of events to compute: "))

event_data = []
sum_list = 0
counter = 0
summation = 0

for i in range(1, num+1):
    event = float(input(f"Enter value x{i}: "))
    event_data.append(event)

for i in event_data:
    sum_list += i
    counter += 1
avg = sum_list / counter

for event in event_data:
    summation += (event - avg)**2

pop_std = (summation / (counter - 1))**0.5
print(f"Sample Standard deviation = {round(pop_std, 4)}")

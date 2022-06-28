# Change the Measurements numbers to your numbers that you get from the Website
Measurements = '''\
143
147
150
'''
#Part 1
numbers = [int(line) for line in Measurements.splitlines()]

count = 0

prev = numbers[0]
for n in numbers[1:]:
    if n > prev:
        count += 1
    prev = n
    
#The count is the Answer
print(f"Part 1: {count}")



#Part 2
numbers = [int(line) for line in Measurements.splitlines()]

count = sum(
    numbers[i] > numbers[i - 3]
    for i in range(3, len(numbers))
)


#The count is the Answer
print(f"Part 2: {count}")

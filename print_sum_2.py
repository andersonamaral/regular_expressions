import re


x = open('/home/anderson/Desktop/python_web/first_assignment/regex_sum_236412.txt')
numlist = list()

for line in x:
	numbers = re.findall('[0-9]+', line)
	if len(numbers) == 1:
		num1 = int(numbers[0])
		numlist.append(num1)
	if len(numbers) == 2:
		num2 = int(numbers[0])
		num3 = int(numbers[1])
		numlist.append(num2)
		numlist.append(num3)
	if len(numbers) == 3:
		num4 = int(numbers[0])
		num5 = int(numbers[1])
		num6 = int(numbers[2])
		numlist.append(num4)
		numlist.append(num5)
		numlist.append(num6)

sum = 0
for number in numlist:
	sum += number
print (sum)
import random

print("Enter the number of list numbers:")
nlist = int(input())
numbers = []
sum_odd = 0
for num in range(nlist):
    numbers.append(random.randint(0,nlist))
    
print("This List:")
print(numbers)

print("Odd numbers in list:")
for li in range(nlist):
    if numbers[li]%2 != 0:
        sum_odd += numbers[li]
        print(numbers[li])
        
print("Sum numbres of odd: "+ str(sum_odd))

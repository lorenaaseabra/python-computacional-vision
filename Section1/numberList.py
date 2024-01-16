import random

numberList = [random.randint(1, 100) for _ in range(20)]

biggestNumber = max(numberList)

print("List of numbers:", numberList)
print("The biggest number in the list:", biggestNumber)

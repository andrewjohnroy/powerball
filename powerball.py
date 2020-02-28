import random
numbers = []

while len(numbers) < 7:
    number = random.randint(1,35)
    if number not in numbers:
        numbers.append(number)

print("Pick these numbers:")
for i in numbers:
    print(i, end=" ")

print("\nAnd this Powerball number:")
print(random.randint(1,20))

print("Good luck, you have a one in 134,490,400 chance of winning the jackpot")

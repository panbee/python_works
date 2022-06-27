squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)


squares = [value**2 for value in range(1, 11)]
print(squares)

# for number in range(1, 21):
#     print(number)

numbers = list(range(1, 1000001))
# for number in numbers:
#     print(number)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# numbers = list(range(1, 20, 2))
# for number in numbers:
#     print(number)

# for number in range(3, 31):
#     if(number%3 == 0):
#         print(number)

numbers = [value**3 for value in range(1, 11)]
print(numbers)


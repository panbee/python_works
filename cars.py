cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)

# cars.sort(reverse=True)
# print(cars)

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars, reverse=True))

print("\nHere is this original list again:")
print(cars)

for car in cars:
    if car == 'bmw':
        print(car.title())
    else:
        print(car.upper())

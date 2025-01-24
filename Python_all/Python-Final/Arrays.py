cars = ['Ford', 'Volvo', 'BMW']
cars[0]="Toyota"
print(cars[0])
print(len(cars))
for x in cars:
    print(x)
cars.append('Mazeda')
print(cars)
# cars.pop(1)
cars.pop()
print(cars)
# cars.remove('Toyota')
a=cars.remove()
print(a)
print(cars)


from collections import namedtuple

Color = namedtuple('Color', ('red', 'green', 'blue'))
color = Color(55, 155, 255)
white = Color(255,251,250)


print(white.blue)

print(color[0])
print(color.red)
print(color.blue)
print(color.green)

# Car = namedtuple('Car', ('BMW', 'Mazeda', 'Toyata'))
# power = Car(24.8, 22.6, 20.9)

# print(power.BMW)
# print(power.Mazeda)
# print(power.Toyata)

# print(power[0])


# from collections import namedtuple

# Color = namedtuple('Color', ['red', 'green', 'blue'])
# color = Color(55, 155, 255)

# color = (55, 155, 255)
# color = {'red': 55, 'green': 155, 'blue': 255}

# print(color.blue)
from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])
color2 = Color(55,155,255)
white = Color(245,245,245)
print(white.blue)
print(color2.red)

color = (55,155,255)
print(color[0])

color1 = {'red': 56, 'green': 67, 'blue': 244}
print(color1['red'])
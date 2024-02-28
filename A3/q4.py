import random
import matplotlib.pyplot as plt


def y1(x, y):
    if -y + 0.5 * x + 2 >= 0:
        return 1
    return 0


def y2(x, y):
    if -y - 3 * x + 9 >= 0:
        return 1
    return 0


def y3(x, y):
    if y - 3 * x + 9 >= 0:
        return 1
    return 0


def y4(x, y):
    if y + 0.5 * x + 2 >= 0:
        return 1
    return 0


def y5(x):
    if x >= 0:
        return 1
    return 0


def y6(x, y):
    if -y - 0.5 * x + 2 >= 0:
        return 1
    return 0


def y7(x, y):
    if -y + 3 * x + 9 >= 0:
        return 1
    return 0


def y8(x, y):
    if y + 3 * x + 9 >= 0:
        return 1
    return 0


def y9(x, y):
    if y - 0.5 * x + 2 >= 0:
        return 1
    return 0


def y10(x):
    return 1 if x <= 0 else 0


def g1(x, y):
    s = y1(x, y) + y2(x, y) + y3(x, y) + y4(x, y) + y5(x)
    if s >= 5:
        return 1
    return 0


def g2(x, y):
    s = y6(x, y) + y7(x, y) + y8(x, y) + y9(x, y) + y10(x)
    if s >= 5:
        return 1
    return 0


def ytotal(x, y):
    s = g1(x, y) + g2(x, y)
    if s >= 1:
        return 1
    return 0


NUMBER_OF_SAMPLES = 10 ** 4 * 5

x_valid_points = []
y_valid_points = []

for i in range(NUMBER_OF_SAMPLES):
    x_sample, y_sample = random.random() * 8 - 4, random.random() * 8 - 4
    res = ytotal(x_sample, y_sample)
    if res >= 1:
        x_valid_points.append(x_sample)
        y_valid_points.append(y_sample)

plt.scatter(x_valid_points, y_valid_points)
plt.xlabel('x_valid_points')
plt.ylabel('y_valid_points')
plt.title('Plot of x_valid_points vs y_valid_points')
plt.grid(True)

plt.savefig('plot.png')

plt.show()

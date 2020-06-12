from math import sqrt
import matplotlib.pyplot as plt
class SquareFunction:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        if self.b > 0:
            sign_b = '+'
        else:
            sign_b = ''

        if self.c > 0:
            sign_c = '+'
        else:
            sign_c = ''
        return f'{self.a}x^2 {sign_b} {self.b}x {sign_c} {self.c}'

    def delta(self):
        return self.b * self.b - 4 * self.a * self.c

    def solve(self):
        fun_delta = self.delta()
        if fun_delta >= 0:
            x1 = (-1 * self.b - sqrt(fun_delta)) / 2
            x2 = (-1 * self.b + sqrt(fun_delta)) / 2
            return x1, x2
        else:
            return None

    def count_y(self, x):
        return x * x * self.a + x * self.b + self.c
        
    def generate_y(self):
        tab_y = []
        tab_x = []
        tab_0 = []
        for x in range(-10, 11):
            tab_y.append(self.count_y(x))
            tab_x.append(x)
            tab_0.append(0)
        return tab_x, tab_y, tab_0

    def draw_fun(self):
        plt.plot(self.generate_y()[0], self.generate_y()[1])
        plt.plot([-10, 10], [0, 0])
        plt.show()


my_func = SquareFunction(1, 0, 0)
print(my_func)
print(my_func.draw_fun())
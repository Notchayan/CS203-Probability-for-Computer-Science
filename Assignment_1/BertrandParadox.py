from random import random
from matplotlib import pyplot as plt
import numpy as np
import math

class BertrandParadoxSimulation:
    def __init__(self):
        self.figure, self.axes = plt.subplots()
        self.triangle_side_length = 0

    def calculate_distance(self, point_a, point_b):
        return math.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)

    def draw_circle(self, radius):
        self.axes.set_xlim((-radius - 1, radius + 1))
        self.axes.set_ylim((-radius - 1, radius + 1))
        self.axes.set_xlabel('x')
        self.axes.set_ylabel('y')

        circle = plt.Circle((0, 0), radius, color='black', fill=False)
        self.axes.add_artist(circle)

    def draw_equilateral_triangle(self, point_p):
        x, y = point_p

        points = np.hstack([x, y])
        self.axes.plot(x, y, color='cyan', marker='o', label='Point P')

        angle = np.deg2rad(120)
        x = point_p[0] * np.cos(angle) - (point_p[1] * np.sin(angle))
        y = point_p[0] * np.sin(angle) + (point_p[1] * np.cos(angle))
        point_a = (x, y)
        points = np.vstack([points, [x, y]])
        self.axes.plot(x, y, color='magenta', marker='*')  

        angle = np.deg2rad(240)
        x = point_p[0] * np.cos(angle) - (point_p[1] * np.sin(angle))
        y = point_p[0] * np.sin(angle) + (point_p[1] * np.cos(angle))
        point_b = (x, y)

        self.triangle_side_length = self.calculate_distance(point_a, point_b)
        points = np.vstack([points, [x, y]])
        self.axes.plot(x, y, color='orange', marker='*')

        points = np.vstack([points, [point_p[0], point_p[1]]])
        self.axes.plot(points[:, 0], points[:, 1], linewidth=3, color='#3e0b78', label='Equilateral triangle')

    def simulate_random_endpoints_method(self):
        radius = float(input('Enter the radius of the circle (r): '))
        num_trials = int(input('Enter the number of trials (n): '))

        self.figure.suptitle('Bertrand Paradox - Random Endpoints Method')
        self.draw_circle(radius)

        alpha = random() * (2 * np.pi)
        x, y = radius * np.cos(alpha), radius * np.sin(alpha)
        point_p = (x, y)
        self.draw_equilateral_triangle(point_p)

        favorable_count = 0
        for _ in range(num_trials):
            alpha = random() * (2 * np.pi)
            x, y = radius * np.cos(alpha), radius * np.sin(alpha)
            point_m = (x, y)
            self.axes.plot(x, y, color='black', marker='.', markersize=5)
            if self.calculate_distance(point_p, point_m) > self.triangle_side_length:
                self.axes.plot([point_p[0], x], [point_p[1], y], color='green', alpha=0.5, linewidth=1)
                favorable_count += 1
            else:
                self.axes.plot([point_p[0], x], [point_p[1], y], color='#b85ea7', alpha=0.5, linewidth=1)

        print('Out of {} trials, {} cases favored the condition, yielding a probability of {:.2f}'.format(
            num_trials, favorable_count, favorable_count / num_trials))

        plt.legend()
        plt.grid()
        plt.show()

    def simulate_random_radial_point_method(self):
        radius = float(input('Enter the radius of the circle (r): '))
        num_trials = int(input('Enter the number of trials (n): '))

        self.figure.suptitle('Bertrand Paradox - Random Radial Point Method')
        self.draw_circle(radius)

        alpha = random() * (2 * np.pi)
        x, y = radius * np.cos(alpha), radius * np.sin(alpha)
        plt.plot([0, x], [0, y], color='black', linewidth=3, label='Radius')

        beta = abs(alpha - np.pi/2)
        x, y = radius * np.cos(alpha), radius * np.sin(alpha)
        point_p = (x, y)
        self.draw_equilateral_triangle(point_p)

        point_a = (radius / 2 * np.cos(alpha), radius / 2 * np.sin(alpha))
        plt.plot(point_a[0], point_a[1], color='#3e0b78', marker='o', label='Middle of the radius')

        favorable_count = 0
        for _ in range(num_trials):
            m = random() * radius
            x, y = m * np.cos(alpha), m * np.sin(alpha)
            point_m = (x, y)
            plt.plot(x, y, color='orange', marker='.', markersize=5)

            length = math.sqrt(pow(radius, 2) - pow(self.calculate_distance(point_m, (0, 0)), 2))
            x1, y1 = x + length * np.cos(beta), y + length * np.sin(beta)
            x2, y2 = x - length * np.cos(beta), y - length * np.sin(beta)
            if self.calculate_distance(point_a, (0, 0)) < self.calculate_distance(point_m, (0, 0)):
                plt.plot([x1, x2], [y1, y2], color='#b85ea7', alpha=0.5, linewidth=1)
            else:
                plt.plot([x1, x2], [y1, y2], color='green', alpha=0.5, linewidth=1)
                favorable_count += 1

        print('Out of {} trials, {} cases favored the condition, yielding a probability of {:.2f}'.format(
            num_trials, favorable_count, favorable_count / num_trials))

        plt.legend()
        plt.grid()
        plt.show()

    def simulate_random_midpoint_method(self):
        radius = float(input('Enter the radius of the circle (r): '))
        num_trials = int(input('Enter the number of trials (n): '))

        self.figure.suptitle('Bertrand Paradox - Random Midpoint Method')
        self.draw_circle(radius)

        alpha = random() * (2 * np.pi)
        point_p = x, y = radius * np.cos(alpha), radius * np.sin(alpha)
        self.draw_equilateral_triangle(point_p)

        circle = plt.Circle((0, 0), radius / 2, color='grey', fill=False)
        self.axes.add_artist(circle)

        favorable_count = 0
        for _ in range(num_trials):
            alpha = random() * (2 * np.pi)
            rand_radius = math.sqrt(random())
            x, y = rand_radius * radius * np.cos(alpha), rand_radius * radius * np.sin(alpha)
            point_m = (x, y)
            if self.calculate_distance(point_m, (0, 0)) <= radius / 2:
                plt.plot(x, y, color='green', marker='.', markersize=5)
                favorable_count += 1
            else:
                plt.plot(x, y, color='#b85ea7', marker='.', markersize=5)

        print('Out of {} trials, {} cases favored the condition, yielding a probability of {:.2f}'.format(
            num_trials, favorable_count, favorable_count / num_trials))

        plt.legend()
        plt.grid()
        plt.show()

def main():
    print('Please select one of the following methods to explore the Bertrand Paradox:')
    print('1. Method 1: The "random endpoints" method')
    print('2. Method 2: The "random radial point" method')
    print('3. Method 3: The "random midpoint" method')
    
    choice = int(input('Enter your choice out of 1 or 2 or 3: '))
    bertrand_simulation = BertrandParadoxSimulation()

    if choice == 1:
        bertrand_simulation.simulate_random_endpoints_method()
    elif choice == 2:
        bertrand_simulation.simulate_random_radial_point_method()
    elif choice == 3:
        bertrand_simulation.simulate_random_midpoint_method()
    else:
        print("Invalid choice. Please select a number from 1 to 3.")

if __name__ == '__main__':
    main()

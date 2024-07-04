import numpy as np
import plotly.graph_objects as go

# Function to calculate the probability ratio of winning by switching vs. staying
def calculate_probability_ratio(num_doors, num_cars):
    switch_wins = 0
    stay_wins = 0

    for _ in range(12000):  # 12,000 trials
        doors = ['goat'] * num_doors
        car_indices = np.random.choice(range(num_doors), num_cars, replace=False)
        for idx in car_indices:
            doors[idx] = 'car'

        contestant_choice = np.random.randint(num_doors)
        revealed_goat_indices = [idx for idx, prize in enumerate(doors) if prize == 'goat' and idx != contestant_choice]
        door_revealed = np.random.choice(revealed_goat_indices)

        # Calculate win for switch
        switch_win = doors[(set(range(num_doors)) - {contestant_choice, door_revealed}).pop()] == 'car'
        if switch_win:
            switch_wins += 1

        # Calculate win for stay
        stay_win = doors[contestant_choice] == 'car'
        if stay_win:
            stay_wins += 1

    switch_probability = switch_wins / 12000
    stay_probability = stay_wins / 12000

    return switch_probability / stay_probability

# Generate data for the surface plot
num_doors_values = np.arange(3, 22)
num_cars_values = np.arange(1, 20)
X, Y = np.meshgrid(num_doors_values, num_cars_values)
Z = np.zeros_like(X, dtype=float)

for i in range(len(num_doors_values)):
    for j in range(len(num_cars_values)):
        num_doors = num_doors_values[i]
        num_cars = num_cars_values[j]
        if num_doors >= num_cars + 2:
            Z[j, i] = calculate_probability_ratio(num_doors, num_cars)

# Plotting using Plotly
fig = go.Figure(data=[go.Surface(z=Z, x=num_doors_values, y=num_cars_values)])
fig.update_layout(title='Probability Ratio of Winning by Switching vs. Staying',
                  scene=dict(xaxis_title='Number of Doors (n)',
                             yaxis_title='Number of Cars (k)',
                             zaxis_title='P(win/switch) / P(win/stay)'))
fig.show()
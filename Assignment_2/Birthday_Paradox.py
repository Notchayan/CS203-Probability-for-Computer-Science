import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D
from matplotlib.patches import Arc

#Actual Factorial Calculation
def factorial_calculation(m):
	answer = 0
	for i in range(365,365-(m),-1):
		answer += (np.log(i) - np.log(365))
	return answer

def birthday_paradox(probability):
	for i in range(1,365):
		if np.log(1-probability) > factorial_calculation(i):
			return i
		
# Stirling's Approximation
def stirling_approximation(k):
	return (365-k+0.5)*(np.log(365.0/(365-k))) - k 

def birthday_paradox_stirling(probability):
	for i in range(1,365):
		if stirling_approximation(i) < np.log(1-probability):
			return i

p = input("Enter the required probaiblitity: ")
num_people = birthday_paradox_stirling(float(p))
print("Required no. of people to have a probability of ", p, "is: ", num_people)
print("The probability of two people having the same birthday with ", num_people, "people is: ", 1 - (math.factorial(365)/(math.factorial(365-num_people)*365**num_people)))

def animate_plot():
	my_array=np.linspace(0, 1, num=1000, endpoint=False)
	probability=[]
	no_of_people=[]
	for i in my_array:
		num_people = birthday_paradox_stirling(i)
		probability.append(i)
		no_of_people.append(num_people)
	probability=np.array(probability)
	no_of_people=np.array(no_of_people)
	plt.plot(probability, no_of_people, color='blue')
	plt.ylabel('Number of People')
	plt.xlabel('Probability')
	plt.legend(['Number of People'])
	plt.title('Number of People vs Probability Required')
	plt.show()

animate_plot()
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from itertools import zip_longest
from math import pi, sqrt, factorial
from typing import List, Union

print("Welcome to the conversion of a uniform distribution between [a, b] to a Gaussian distribution with parameters mu (mean) and sigma (standard deviation).")

while True:
    lower_bound = float(input("Enter the lower bound (a): "))
    upper_bound = float(input("Enter the upper bound (b): "))
    if upper_bound > lower_bound:
        break
    else:
        print("Error: The upper bound must be greater than the lower bound.")

num_samples = int(input("Enter the number of samples: "))
mean = float(input("Provide the mean: "))
std_deviation = float(input("Provide standard deviation : "))

while True:
    num_terms_taylor_series = input("Enter the number of terms in the Taylor series (between 1 and 100): ")
    try:
        num_terms_taylor_series = int(num_terms_taylor_series)
        if 1 <= num_terms_taylor_series <= 100:
            break
        else:
            print("Error: Number of terms must be between 1 and 100.")
    except ValueError:
        print("Error: Please enter a valid integer.")

class InverseGaussianCDF:
    def __init__(self, degree: int) -> None:
        """
        Initialize with Taylor series coefficients of the inverse error function.
        :param degree: Highest degree of the Taylor series.
        """
        self.taylor_coeffs = self._get_taylor_coeffs(degree + 1)

    def _update_polynomial(self, polynomial: List[int], power: int) -> List[int]:
        """
        Update polynomial for each term of Taylor series approximation of erfinv.
        :param polynomial: Polynomial of the previous power.
        :param power: Power of the current term.
        :return: Polynomial of the current power term.
        """
        extended_polynomial = [0] + polynomial
        two_n_EP = [2 * power * coeff for coeff in extended_polynomial]
        dP = [power * coeff for power, coeff in enumerate(polynomial)][1:]
        updated_polynomial = [two_nEP_coeff + dP_coeff for two_nEP_coeff, dP_coeff in zip_longest(two_n_EP, dP, fillvalue=0)]
        return updated_polynomial

    def _get_taylor_coeffs(self, num_terms: int) -> List[float]:
        """
        Get coefficients of Taylor series approximation for the inverse error function (up to specified number of terms).
        :param num_terms: Number of terms of the Taylor series.
        :return: List of Taylor series coefficients matching the number of terms.
        """
        taylor_coeffs = [0, sqrt(pi) / 2]  # First two coefficients

        if num_terms <= 2:
            return taylor_coeffs[:num_terms]
        else:
            polynomial = [0, 2]  # Polynomial of the second derivative
            first_derivative_at_0 = sqrt(pi) / 2  # First derivative at x = 0

            for n in range(2, num_terms):
                polynomial_const = polynomial[0]
                taylor_coefficient = (first_derivative_at_0 ** n * polynomial_const) / factorial(n)
                polynomial = self._update_polynomial(polynomial, n)
                taylor_coeffs.append(taylor_coefficient)
            return taylor_coeffs

    def calculate_sample(self, sampled_areas: Union[float, np.ndarray]) -> Union[float, np.ndarray]:
        """
        Return Gaussian sample(s) from sampled left-side area(s).
        :param sampled_areas: Sampled left-side area(s), can be a single float or a numpy float array.
        :return: Gaussian sample(s) from applying inverse CDF to sampled area(s), can be a single float or numpy float array.
        """
        sample = sqrt(2) * sum(coeff * (2 * sampled_areas - 1) ** power for power, coeff in enumerate(self.taylor_coeffs))
        return sample


# Create an instance of the InverseGaussianCDF class
inverse_gaussian_cdf = InverseGaussianCDF(num_terms_taylor_series)

# Generate uniformly sampled areas
sampled_areas = np.array([random.uniform(lower_bound, upper_bound) for _ in range(num_samples)])

# Normalize sampled areas
sampled_areas = (sampled_areas - lower_bound) / (upper_bound - lower_bound)

# Calculate Gaussian samples
gaussian_samples = inverse_gaussian_cdf.calculate_sample(sampled_areas)

# Plot histogram
plt.figure(figsize=(10, 6))
sns.histplot(gaussian_samples, bins=30, kde=True, color='skyblue', edgecolor='black')
plt.title('Histogram of Gaussian Samples')
plt.xlabel('Gaussian Samples')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Calculate probabilities
num_sigma = np.sum(np.logical_or(gaussian_samples > mean + std_deviation, gaussian_samples < mean - std_deviation))
probability = 1 - (num_sigma / num_samples)

num_2sigma = np.sum(np.logical_or(gaussian_samples > mean + 2 * std_deviation, gaussian_samples < mean - 2 * std_deviation))
probability2 = 1 - (num_2sigma / num_samples)

print("Probability of numbers within one standard deviation from the mean :", probability)
print("Probability of numbers within two standard deviations from the mean:", probability2)


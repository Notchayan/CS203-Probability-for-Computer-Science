# Gaussian Distribution Sampler using Inverse CDF Method

## Introduction
This Python script demonstrates the conversion of a uniform distribution between [a, b] to a Gaussian distribution using the Inverse Cumulative Distribution Function (CDF) method. The script utilizes Taylor series approximation of the inverse error function (erfinv) to generate Gaussian samples.

## Requirements
- Python 3.x
- NumPy
- Matplotlib
- Seaborn

## Usage
1. Run the script in a Python environment.
2. You will be prompted to input the lower and upper bounds of the interval [a, b], the number of samples, the mean, the standard deviation, and the number of terms in the Taylor series.
3. The script will generate Gaussian samples using the Inverse CDF method and plot a histogram to visualize the distribution.
4. The probability of numbers within one and two standard deviations from the mean will be printed.

## Files
- `gaussian_sampler.py`: Python script containing the implementation of the Gaussian distribution sampler using the Inverse CDF method.
- `README.md`: This file, providing instructions and information about the script.

## Example
Suppose you want to generate 1000 Gaussian samples with a mean of 0 and a standard deviation of 1, within the interval [-1, 1], and use a Taylor series approximation with 10 terms. You can run the script, and input the following values when prompted:
- Lower bound (a): -1
- Upper bound (b): 1
- Number of samples: 1000
- Mean: 0
- Standard deviation: 1
- Number of terms in the Taylor series: 10

## References
- Inverse Cumulative Distribution Function (Inverse CDF) method: [Wikipedia](https://en.wikipedia.org/wiki/Inverse_transform_sampling)
- Error function and Inverse error function: [Wikipedia](https://en.wikipedia.org/wiki/Error_function)
- [blog](https://medium.com/mti-technology/how-to-generate-gaussian-samples-347c391b7959)


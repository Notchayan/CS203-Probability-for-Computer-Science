## Bayesian Analysis

### Dependencies

- Python 3.x
- Required Python libraries: `numpy`, `matplotlib`

### Usage

1. **Install Dependencies:**

   ```bash
   pip install numpy matplotlib
   ```
1. **Run Code**

   ```bash
   bayesian_analysis.py
   ```

The code demonstrates Bayesian analysis of beta distribution priors using observed outcomes. It includes:

- Plotting prior distributions.
- Calculating likelihood based on observed outcomes.
- Plotting likelihood distribution.
- Updating priors to posterior distributions.
- Plotting posterior distributions with Maximum Likelihood Estimate (MLE) and Maximum A Posteriori (MAP) estimates.

### Inputs

- `priors`: List of tuples containing prior beta distribution parameters `(a, b)`.
- `outcomes`: List of observed outcomes (`'H'` for heads, `'T'` for tails).

### Outputs

- Visualizations of prior, likelihood, and posterior distributions.
- MLE and MAP estimates for each posterior distribution
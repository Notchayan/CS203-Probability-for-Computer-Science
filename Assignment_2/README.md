# BIRTHDAY PARADOX

This is the second assignment submission for CS203: Mathematics for Computer Science III submitted by Aditi Khandelia and Kushagra Srivastava.

### Contents

- `Birthday_Paradox.py`
  - This is the main python file for the assignment.
  - It takes as input the probability for which we need to find the no. of people with probability of atleast two people sharing the same birthday > the given probability.
  - Produces the required no. of people, the exact probability of atleast two people sharing the same birthday with the said no. of people, and the plot of probability vs no. of people

### Build instructions

```
python3 Birthday_Paradox.py
```

### Formulae

$$p = \frac{365!}{{365}^{n}(365-n)!}$$
where $p$ = probability, $n$ = no. of people

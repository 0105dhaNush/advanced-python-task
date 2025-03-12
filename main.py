from functools import reduce

# Lambda function to generate Fibonacci series up to n terms
fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])[:n]

# Test the function
n_terms = 10
print(fibonacci(n_terms))

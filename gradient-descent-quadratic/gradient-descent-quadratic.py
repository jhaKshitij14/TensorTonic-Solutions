def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here
    x = x0

    for step in range(steps):
        x = x - lr * ((2*a*x) + b)
    return x
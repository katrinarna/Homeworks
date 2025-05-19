import numpy as np
import matplotlib.pyplot as plt

class MonteCarlo:
    """
    Monte Carlo integrator for 1D and 2D functions.

    Attributes:
        f: Function to integrate.
        a: Lower bound for 1D integration or tuple (x_min, y_min) for 2D.
        b: Upper bound for 1D integration or tuple (x_max, y_max) for 2D.
    """

    def __init__(self, f, a, b):
        self.f = f
        self.a = a
        self.b = b

    def integrate(self, N):
        """Approximate the integral using Monte Carlo integration."""
        if isinstance(self.a, (int, float)):
            x = np.random.uniform(self.a, self.b, N)
            return (self.b - self.a) * np.mean(self.f(x))
        else:
            x = np.random.uniform(self.a[0], self.b[0], N)
            y = np.random.uniform(self.a[1], self.b[1], N)
            values = self.f(x, y)
            area = (self.b[0] - self.a[0]) * (self.b[1] - self.a[1])
            return area * np.mean(values)

    def plot(self, N, exact_value=None):
        """Plot how the Monte Carlo approximation converges."""
        estimates = []
        trials = np.arange(1, N + 1)
        for n in trials:
            estimates.append(self.integrate(n))

        plt.plot(trials, estimates, label='Monte Carlo Estimate')
        if exact_value is not None:
            plt.axhline(y=exact_value, color='red', linestyle='--', label='Exact Value')
        plt.xlabel("Number of Samples")
        plt.ylabel("Integral Estimate")
        plt.title("Convergence of Monte Carlo Integration")
        plt.legend()
        plt.grid()
        plt.show()



# f(x) = sin(x) on [0, pi] has exact integral = 2
mc = MonteCarlo(lambda x: np.sin(x), 0, np.pi)
print("Approximate:", mc.integrate(10000))
mc.plot(5000, exact_value=2)

# H(x, y) = 1 if inside unit circle, else 0
def H(x, y):
    return (x**2 + y**2 <= 1).astype(float)

mc_pi = MonteCarlo(H, (-1, -1), (1, 1))
print("Approximation of π:", mc_pi.integrate(100000))


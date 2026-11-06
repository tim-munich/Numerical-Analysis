import numpy as np
import matplotlib.pyplot as plt

# 1. Model parameters
lambda_b = 1.0
lambda_r = 4.0
b_e = 0.5
r_e = 0.25

# 2. Initial conditions
b0 = 1.0
r0 = 0.1

# 3. Time discretization
T = 20
N = 5000
h = T / N

t = np.linspace(0, T, N + 1)

# 4. Initialize population arrays
b = np.zeros(N + 1)
r = np.zeros(N + 1)

b[0] = b0
r[0] = r0

# 5. Explicit Euler method
for n in range(N):
    b[n + 1] = b[n] + h * lambda_b * b[n] * (1 - r[n] / r_e)
    r[n + 1] = r[n] + h * lambda_r * r[n] * (b[n] / b_e - 1)

# 6. Population over time
plt.figure()
plt.plot(t, b, label="Prey")
plt.plot(t, r, label="Predator")
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Population over time")
plt.legend()
plt.grid(True)

# 7. Phase-space trajectory
plt.figure()
plt.plot(b, r)
plt.xlabel("Prey")
plt.ylabel("Predator")
plt.title("Phase space")
plt.grid(True)

plt.show()
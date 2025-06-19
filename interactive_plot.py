import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from matplotlib.widgets import Slider

# Define the antiderivatives F1 and F2
def F1(x, a, b):
    return (2 / (45 * a ** 2)) * (a * x + b) ** (5 / 2) - (2 * b / (27 * a ** 2)) * (a * x + b) ** (3 / 2)

def F2(x, a, b):
    return (2 / (3 * a)) * x * (a * x + b) ** (3 / 2) - (4 / (15 * a ** 2)) * (a * x + b) ** (5 / 2)

# Reference numerical integration
def I_ref(x, a, b):
    integral, _ = quad(lambda t: t * np.sqrt(a * t + b), 0, x)
    return integral

# Compute error arrays
def compute_errors(x_vals, a, b):
    f1_vals = np.array([F1(x, a, b) for x in x_vals])
    f2_vals = np.array([F2(x, a, b) for x in x_vals])
    ref_vals = np.array([I_ref(x, a, b) for x in x_vals])
    e1 = np.abs(f1_vals - ref_vals)
    e2 = np.abs(f2_vals - ref_vals)
    delta = np.abs(e2 - e1)
    return e1, e2, delta

# Create plot
x_vals = np.logspace(-2, 2, 300)
a_init, b_init = 3, 1
e1, e2, delta = compute_errors(x_vals, a_init, b_init)

fig, ax = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
plt.subplots_adjust(left=0.25, bottom=0.25)

l1, = ax[0].plot(x_vals, e1, label='Error of F1', color='green')
l2, = ax[0].plot(x_vals, e2, label='Error of F2', color='red', linestyle='--')
ax[0].set_ylabel('Absolute Error')
ax[0].set_xscale('log')
ax[0].set_yscale('log')
ax[0].legend()
ax[0].grid(True)

l3, = ax[1].plot(x_vals, delta, label='|Error F2 - Error F1|', color='blue')
ax[1].set_xlabel('x')
ax[1].set_ylabel('Error Difference')
ax[1].set_xscale('log')
ax[1].set_yscale('log')
ax[1].legend()
ax[1].grid(True)

# Add sliders
ax_a = plt.axes([0.25, 0.12, 0.65, 0.03])
ax_b = plt.axes([0.25, 0.07, 0.65, 0.03])
slider_a = Slider(ax_a, 'a', 0.001, 5.0, valinit=a_init)
slider_b = Slider(ax_b, 'b', 0.001, 5.0, valinit=b_init)

# Update function
def update(val):
    a = slider_a.val
    b = slider_b.val
    e1, e2, delta = compute_errors(x_vals, a, b)
    l1.set_ydata(e1)
    l2.set_ydata(e2)
    l3.set_ydata(delta)
    fig.canvas.draw_idle()

slider_a.on_changed(update)
slider_b.on_changed(update)

plt.show()

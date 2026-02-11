import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8-muted')

x = np.linspace(0, 10, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)
categories = ['A', 'B', 'C', 'D']
values = [15, 30, 45, 10]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(x, y_sin, label='Sine', color='royalblue', linewidth=2)
ax1.plot(x, y_cos, label='Cosine', color='indianred', linestyle='--')
ax1.set_title('Trigonometric Functions')
ax1.legend()
ax1.grid(True, alpha=0.3)

ax2.bar(categories, values, color='teal', alpha=0.7)
ax2.set_title('Category Distribution')
ax2.set_ylabel('Impact Score')

plt.tight_layout()
plt.show()
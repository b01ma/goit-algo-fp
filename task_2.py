import matplotlib.pyplot as plt
import numpy as np

def draw_branch(x, y, length, angle, level, ax):
    if level == 0:
        return

    # Кінцева точку відрізка
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    ax.plot([x, x_end], [y, y_end], color='brown', lw=1)

    new_length = length * 0.7
    draw_branch(x_end, y_end, new_length, angle + np.pi/4, level - 1, ax)  # ліва гілка
    draw_branch(x_end, y_end, new_length, angle - np.pi/4, level - 1, ax)  # права гілка

# Налаштування графіка
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_aspect('equal')
ax.axis('off')

# Початкова точка і параметри
x0, y0 = 0, 0
initial_length = 100
initial_angle = np.pi / 2  # вертикально вгору
recursion_depth = int(input('Depth level, from 1 to 10: ')) 

while recursion_depth <= 0 or recursion_depth > 10:
    recursion_depth = int(input('Please provide a level from 1 to 10: '))

draw_branch(x0, y0, initial_length, initial_angle, recursion_depth, ax)
plt.show()

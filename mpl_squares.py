import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
ax.scatter(2,4)
ax.plot(input_values, squares, linewidth = 3)

"""Назначение размера шрифта деления на осях"""
ax.tick_params(axis='both', labelsize = 14)


plt.show()
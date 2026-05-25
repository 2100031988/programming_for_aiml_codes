import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
from matplotlib.patches import Circle
from matplotlib.patheffects import withStroke


# < ----- in class activity 1 ------ >

# <----- Build a complete Matplotlib figure (element by element) ----->

fig = plt.figure(figsize=(7.5, 7.5))

ax = fig.add_axes([0.5, 0.5, 0.3, 0.3])

plt.show()

np.random.seed(45)

x = np.linspace(0.5, 3.5, 100)
y1 = 3 + np.cos(x)
y2 = 1 + np.cos(1 + x / 0.75) / 2
y3 = np.random.uniform(y1, y2, len(x))

print(x)


# function
def annotate(ax, x, y, text, code):
    royal_blue = [0, 20/256, 82/256]
    c = Circle((x, y), radius=0.15, clip_on=False, zorder=10, linewidth=2.5,  # FIX: 'randius' -> 'radius'
               edgecolor=royal_blue + [0.6], facecolor='none',
               path_effects=[withStroke(linewidth=7, foreground='white')])

    ax.add_artist(c)
    for path_effects in [[withStroke(linewidth=0, foreground='white')], []]:  # FIX: extra ']' removed

        color = 'white' if path_effects else royal_blue

        ax.text(x, y + 0.2, text, zorder=100,          # FIX: 'y=0.2' -> 'y + 0.2'
                ha='center', va='top', weight='bold', color=color,
                style='italic', fontfamily='monospace',
                path_effects=path_effects)

        color = 'white' if path_effects else 'black'

        ax.text(x, y - 0.3, code, zorder=100,          # FIX: 'y=-0.3' -> 'y - 0.3'
                ha='center', va='top', weight='normal', color=color,
                fontfamily='monospace',                 # FIX: 'medium' is not valid; use 'monospace'
                path_effects=path_effects)


fig, ax = plt.subplots(figsize=(5.5, 5.5))

print(ax.plot(x, y1, c='C1', label='Line A'))
print(ax.plot(x, y2, c='C2', label='Line B'))          # FIX: was plotting y1 twice, changed to y2

print(ax.plot(x, y3, linewidth=0, marker='s'))
print(ax.plot(x[::3], y3[::3], linewidth=0, marker='s', markerfacecolor='none', markeredgecolor='C4',  # FIX: 'maker...' -> 'marker...'; 'c4' -> 'C4'
              markersize=9, markeredgewidth=2.5))       # FIX: 'makersize', 'makeredgewidth' -> 'markersize', 'markeredgewidth'

ax.set_xlabel('X data')
ax.set_ylabel('Y data')
ax.set_title('Figure XY')

ax.set_xlim(0, 4)
ax.set_ylim(0, 4)

ax.xaxis.set_major_locator(MultipleLocator(1.0))
ax.xaxis.set_minor_locator(AutoMinorLocator(4))

ax.yaxis.set_major_locator(MultipleLocator(1.0))
ax.yaxis.set_minor_locator(AutoMinorLocator(4))

ax.tick_params(which='major', width=1.0, length=10, labelsize=14)
ax.tick_params(which='minor', width=1.0, length=5, labelsize=10, labelcolor='0.25')

ax.xaxis.set_minor_formatter("{x:.2f}")                # FIX: invalid string format -> proper format string

ax.grid(linestyle='--', linewidth=0.5, color='0.25', zorder=-10)
ax.legend(loc='upper right', fontsize=14)

annotate(ax, 1.75, 2.0, "Line A", 'Line A trend')
fig.patch.set(linewidth=4, edgecolor='0.5')

plt.show()


# <----------------------------------------------->


# <------- Activity 2: Examples of commonly used plots ------->

# Scatter plot
plt.figure()
x = np.random.rand(50)
y = np.random.rand(50)
y2 = np.random.rand(50)

plt.scatter(x, y, c='purple', marker='s')
plt.scatter(x, y2, c='skyblue', marker='o')            # FIX: 'skyclue' -> 'skyblue'

plt.title('Scatter plot')
plt.xlabel('X value')
plt.ylabel('Y value')

plt.show()


# Bar chart
plt.figure()
labels = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]

plt.bar(labels, values, color='darkviolet')

plt.title('Bar Chart')                                  # FIX: 'plt.titel' -> 'plt.title'
plt.xlabel('Category')
plt.ylabel('Count')

plt.show()


# Histogram
plt.figure()                                            # FIX: 'plt.firgure' -> 'plt.figure'
data = np.random.randn(1000)                            # FIX: 'randin' -> 'randn'
data2 = np.random.randn(500)

plt.hist(data, bins=30, color='green', alpha=0.7)
plt.hist(data2, bins=30, color='blue', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.show()


# Pie chart
plt.figure()
sizes = [15, 30, 45, 10]
labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)   # FIX: '%11.1f%%' -> '%1.1f%%'
plt.title('Pie Chart')

plt.show()


# Box plot
plt.figure()                                            # FIX: 'boc plot' comment only, code was 'plt.figure()' - fine
data = [np.random.normal(0, std, 100) for std in range(1, 3)]
plt.boxplot(data)
plt.title('Box Plot')
plt.xlabel('Group')
plt.ylabel('Value')

plt.show()


# Heatmap
plt.figure()
data = np.random.rand(10, 10)
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.title('Heatmap')
plt.xlabel('Column')
plt.ylabel('Row')
plt.colorbar()

plt.show()


# 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

ax.plot_surface(x, y, z, cmap='plasma')
ax.set_title('3D Surface Plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')                                      # FIX: 'set_ylabel' used twice -> second one changed to 'set_zlabel'

plt.show()
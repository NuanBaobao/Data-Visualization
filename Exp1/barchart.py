# library
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
from pylab import mpl

# 设置默认字体，解决中文显示乱码问题
mpl.rcParams["font.sans-serif"] = ["SimHei"]

# Add table data
table_data = [
    ["Class", "female", "male", "Sum"],
    ["first", 145, 180, 325],
    ["second", 106, 179, 285],
    ["third", 196, 510, 706],
    ["crew", 23, 862, 885],
    [" ", 470, 1731, 2201],
]

# Initialize a figure with ff.create_table(table_data)
fig = ff.create_table(table_data, height_constant=60)

# Create bars
barWidth = 0.9
bars1 = [180, 179, 510, 862]
bars2 = [145, 106, 196, 23]
bars3 = bars1 + bars2

# The X position of bars
r1 = [1, 3, 5, 7]
r2 = [2, 4, 6, 8]
r3 = r1 + r2

# Create barplot
plt.bar(r1, bars1, width=barWidth, color=(0.3, 0.1, 0.4, 0.6), label="male")
plt.bar(r2, bars2, width=barWidth, color=(0.3, 0.5, 0.4, 0.6), label="female")
# Note: the barplot could be created easily. See the barplot section for other examples.

# Create legend
plt.legend()

# Text below each barplot with a rotation at 90°
plt.xticks(
    [r + 0.5 for r in range(1, len(2 * r1), 2)],
    ["first", "second", "third", "crew"],
    rotation=90,
)

# Create labels
label = [
    "n = 180",
    "n = 145",
    "n = 179",
    "n = 106",
    "n = 510",
    "n = 196",
    "n = 862",
    "n = 23",
]

# Text on the top of each bar
for i in range(len(r3)):
    plt.text(x=r3[i] - 0.35, y=bars3[i] + 1, s=label[i], size=8)

# Adjust the margins
plt.subplots_adjust(bottom=0.2, top=0.98)

# Show graphic
plt.savefig("barchart.png")
plt.show()

# library
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]  # 显示中文标签,处理中文乱码问题
plt.rcParams["axes.unicode_minus"] = False  # 坐标轴负号的处理
plt.axes(aspect="equal")  # 将横、纵坐标轴标准化处理，确保饼图是一个正圆，否则为椭圆

# create data: an array of values
size_of_groups = [145, 106, 196, 23, 180, 179, 510, 862]
labels = [
    "female-first",
    "female-second",
    "female-third",
    "female-crew",
    "male-first",
    "male-second",
    "male-third",
    "male-crew",
]

# Create a pieplot
plt.pie(
    x=size_of_groups,  # 绘图数据
    labels=labels,  # 添加教育水平标签
    # colors=colors,
    autopct="%.2f%%",  # 设置百分比的格式，这里保留两位小数
    pctdistance=0.8,  # 设置百分比标签与圆心的距离
    labeldistance=1.1,  # 设置标签与圆心的距离
    startangle=180,  # 设置饼图的初始角度
    radius=1.2,  # 设置饼图的半径
    counterclock=False,  # 是否逆时针，这里设置为顺时针方向
    wedgeprops={"linewidth": 1.5, "edgecolor": "green"},  # 设置饼图内外边界的属性值
    textprops={"fontsize": 10, "color": "black"},  # 设置文本标签的属性值
)

# add a circle at the center to transform it in a donut chart
my_circle = plt.Circle((0, 0), 0.7, color="white")
p = plt.gcf()
p.gca().add_artist(my_circle)

plt.savefig('pie.png')
plt.show()

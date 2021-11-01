import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Build a dataset
data = pd.read_csv('F:\可视化\Exp2-zjh\sunshine.csv')
df = pd.DataFrame(data)

df["city"] = df["city"] + " " + df["lon"].round(2).map(
    str) + " " + df["lat"].round(2).map(str)
df.drop(['monthnum'], axis=1, inplace=True)


def get_label_rotation(angle, offset):
    # 旋转必须以度数指定
    rotation = np.rad2deg(angle + offset)
    if angle <= np.pi:
        alignment = "right"
        rotation = rotation + 180
    else:
        alignment = "left"
    return rotation, alignment


def add_labels(angles, values, labels, offset, ax):

    # 这是条形末端和标签之间的空间
    padding = 2

    # 迭代角度、值和标签
    for angle, value, label, in zip(angles, values, labels):
        angle = angle
        value = int(value)

        # 获取文本旋转和对齐
        rotation, alignment = get_label_rotation(angle, offset)

        # 添加文本
        ax.text(x=angle,
                y=value + padding,
                s=label,
                ha=alignment,
                va="center",
                rotation=rotation,
                rotation_mode="anchor")


VALUES = df["sunshine"].values
df["month"] = df["month"] + "=" + df["sunshine"].map(str)
LABELS = df["month"].values 
GROUP = df["city"].values
print(set(GROUP))

# 确定每个条的宽度。
# 周长是“2 * pi”，将总宽度除以条形数量。
WIDTH = 2 * np.pi / len(VALUES)

# 确定放置第一条的位置。.
OFFSET = np.pi / 2

# 在每组末尾添加3个空条
PAD = 3
ANGLES_N = len(VALUES) + PAD * len(np.unique(GROUP))
ANGLES = np.linspace(0, 2 * np.pi, num=ANGLES_N, endpoint=False)
# 获取正确的索引
offset = 0
IDXS = []
GROUPS_SIZE = [12, 12, 12, 12, 12, 12]
for size in GROUPS_SIZE:
    IDXS += list(range(offset + PAD, offset + size + PAD))
    offset += size + PAD

# 初始化图形和轴
fig, ax = plt.subplots(figsize=(15, 15), subplot_kw={"projection": "polar"})

# 指定偏移量
ax.set_theta_offset(OFFSET)

# 设置径向 (y) 轴的限制
ax.set_ylim(-300, 300)

# 去除spines
ax.set_frame_on(False)

# 删除网格和刻度线
ax.xaxis.grid(False)
ax.yaxis.grid(False)
ax.set_xticks([])
ax.set_yticks([])

# 为每组使用不同的颜色
GROUPS_SIZE = [12, 12, 12, 12, 12, 12]
COLORS = [f"C{i}" for i, size in enumerate(GROUPS_SIZE) for _ in range(size)]

# 添加条形
ax.bar(ANGLES[IDXS],
       VALUES,
       width=WIDTH,
       color=COLORS,
       edgecolor="white",
       linewidth=1)

# 添加标签
add_labels(ANGLES[IDXS], VALUES, LABELS, OFFSET, ax)

# 线条和注释

offset = 0
for group, size in zip([
        "Seattle -122.34 47.61","San Francisco -80.19 25.76","Houston -122.45 37.73","Miami -95.36 29.75","New York -73.94 40.73", "Chicago -87.62 41.88"
         
        
], GROUPS_SIZE):
    # 在条形下方添加线
    x1 = np.linspace(ANGLES[offset + PAD],
                     ANGLES[offset + size + PAD - 1],
                     num=73)
    ax.plot(x1, [-10] * 73, color="#333333")

    # 添加文本以指示组
    ax.text(np.mean(x1),
            -50,
            group,
            color="#333333",
            fontsize=8,
            fontweight="bold",
            ha="center",
            va="center")

    # 添加参考线
    x2 = np.linspace(ANGLES[offset], ANGLES[offset + PAD - 1], num=73)
    ax.plot(x2, [40] * 73, color="#bebebe", lw=0.8)
    ax.plot(x2, [90] * 73, color="#bebebe", lw=0.8)
    ax.plot(x2, [140] * 73, color="#bebebe", lw=0.8)
    ax.plot(x2, [190] * 73, color="#bebebe", lw=0.8)
    ax.plot(x2, [240] * 73, color="#bebebe", lw=0.8)
    ax.plot(x2, [290] * 73, color="#bebebe", lw=0.8)

    offset += size + PAD
plt.rcParams['savefig.dpi'] = 300  #图片像素
plt.rcParams['figure.dpi'] = 100  #分辨率
plt.savefig('output.png', dpi=300)
plt.show()

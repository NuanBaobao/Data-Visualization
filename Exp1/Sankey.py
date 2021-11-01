from pyecharts.charts import Sankey
from pyecharts import options as opts
from pylab import mpl
# 设置默认字体，解决中文显示乱码问题
mpl.rcParams['font.sans-serif'] = ['SimHei']

# 节点名称
nodes = [
    {"name": "first"},
    {"name": "second"},
    {"name": "third"},
    {"name": "crew"},
    {"name": "female"},
    {"name": "male"},
]

# 节点之间的关系和数量，source起点，target终点，value数量
links = [
    {"source": "first", "target": "female", "value": "145"},
    {"source": "first", "target": "male", "value": "180"},
    {"source": "second", "target": "female", "value": "106"},
    {"source": "second", "target": "male", "value": "179"},
    {"source": "third", "target": "female", "value": "196"},
    {"source": "third", "target": "male", "value": "510"},
    {"source": "crew", "target": "female", "value": "23"},
    {"source": "crew", "target": "male", "value": "862"},
]

pic = (
    Sankey(init_opts=opts.InitOpts(width="1200px", height="600px"))#设置图表的宽度和高度
    .add(
        "sankey",
        nodes,#读取节点
        links,#读取路径
        linestyle_opt=opts.LineStyleOpts(opacity=0.3, curve=0.6, color="source"),#设置线条样式,curve:弯曲度
        label_opts=opts.LabelOpts(position="top"),#设置标签配置项
        node_gap=30,
        node_align=str( "justify"),#设置节点对齐方式：right，left,justify(节点双端对齐)
    )
    # set_global_opts(title_opts=opts.TitleOpts(title="Sankey"))
).render("Sankey.html")

import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly 

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

# Add graph data
teams = [
    "first",
    "second",
    "third",
    "crew"
]
GFPG = [145, 106, 196, 23]
GAPG = [180, 179, 510, 862]

# Make traces for graph
trace1 = go.Bar(
    x=teams,
    y=GFPG,
    xaxis="x2",
    yaxis="y2",
    marker=dict(color="#0099ff"),
    name="Female",
)
trace2 = go.Bar(
    x=teams,
    y=GAPG,
    xaxis="x2",
    yaxis="y2",
    marker=dict(color="#404040"),
    name="Male",
)

# Add trace data to figure
fig.add_traces([trace1, trace2])

# initialize xaxis2 and yaxis2
fig["layout"]["xaxis2"] = {}
fig["layout"]["yaxis2"] = {}

# Edit layout for subplots
fig.layout.yaxis.update({"domain": [0, 0.45]})
fig.layout.yaxis2.update({"domain": [0.6, 1]})

# The graph's yaxis2 MUST BE anchored to the graph's xaxis2 and vice versa
fig.layout.yaxis2.update({"anchor": "x2"})
fig.layout.xaxis2.update({"anchor": "y2"})
fig.layout.yaxis2.update({"title": "Num"})

# Update the margins to add a title and see graph x-labels.
fig.layout.margin.update({"t": 75, "l": 50})
fig.layout.update({"title": "Barplot"})

# Update the height because adding a graph vertically will interact with
# the plot height calculated for the table
fig.layout.update({"height": 800})

# Plot!
fig.write_image('Barplot.png')
fig.show()

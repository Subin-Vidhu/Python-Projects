import plotly.graph_objects as go

fig = go.Figure(go.Treemap(
    labels = ["A","B", "C", "D", "E", "F", "G", "H", "I"],
    parents = ["", "A", "A", "C", "C", "A", "A", "G", "A"]
))

fig.show()

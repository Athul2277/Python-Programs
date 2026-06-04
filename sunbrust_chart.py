import plotly.express as px

data = dict(
    character=[
        "Technology",
        "AI",
        "Web",
        "ML",
        "DL",
        "Frontend",
        "Backend"
    ],
    parent=[
        "",
        "Technology",
        "Technology",
        "AI",
        "AI",
        "Web",
        "Web"
    ]
)

fig = px.sunburst(
    data,
    names="character",
    parents="parent"
)

fig.show()

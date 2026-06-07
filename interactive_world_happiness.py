import plotly.express as px

df = px.data.gapminder().query("year==2007")

fig = px.choropleth(
    df,
    locations="iso_alpha",
    color="lifeExp",
    hover_name="country",
    title="World Life Expectancy"
)

fig.show()

import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load processed data
df = pd.read_csv("output.csv")

# Convert date column and sort
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "date": "Date",
        "sales": "Total Sales ($)"
    }
)

# Add vertical line for price increase date
fig.add_vline(
    x="2021-01-15",
    line_dash="dash",
    line_color="red"
)


# Build Dash app
app = Dash(__name__)

app.layout = html.Div(
    style={"width": "80%", "margin": "auto"},
    children=[
        html.H1("Pink Morsel Sales Analysis"),
        html.P(
            "This chart shows Pink Morsel sales over time. "
            "The red dashed line marks the price increase on 15 January 2021."
        ),
        dcc.Graph(figure=fig)
    ]
)

if __name__ == "__main__":
    app.run(debug=True)

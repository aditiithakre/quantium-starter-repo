import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load processed data
df = pd.read_csv("output.csv")

# Convert and sort dates
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create Dash app
app = Dash(__name__)

app.layout = html.Div(
    className="container",
    children=[
        html.H1("Pink Morsel Sales by Region"),

        html.Div(
            className="radio-group",
            children=[
                dcc.RadioItems(
                    id="region-selector",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                )
            ],
        ),

        html.Div(
            className="graph-box",
            children=[
                dcc.Graph(id="sales-graph")
            ]
        )
    ]
)

@app.callback(
    Output("sales-graph", "figure"),
    Input("region-selector", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"].str.lower() == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        labels={
            "date": "Date",
            "sales": "Total Sales ($)"
        }
    )

    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        line_color="red"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)

from dash_core_components import Interval, Graph
from dash_html_components import Div
from plotly.graph_objs import Scatter, Layout
from plotly.graph_objs import layout as go_layout 
from plotly.io import templates
from dash_bootstrap_components import Col
from dash.dependencies import Input, Output
# MY IMPORTS
from .helper_methods import *
from .style import app_colors, theme
# import correct app type based on if the app is being run
# directly or via the django framework
if __name__ == '__main__':
    from dash import Dash    
    app = Dash("flood_graph")
else:
    from django_plotly_dash import DjangoDash
    app = DjangoDash('flood_graph')


app.layout = Col(
    width=8,
    children=[
        Interval(
            id="graph_interval",
            interval = 6 * 1000,
        ),
        Div(Graph(id='flood-graph', animate=False)),
    ],
)


@app.callback(
    Output(component_id='flood-graph', component_property='figure'),
    [Input('graph_interval', 'interval')])
def update_flood_graph(interval):
    print('graph-update!')
    obs_data = get_observed_data()
    obs_plot = Scatter(
        name='Observed Level',
        x=obs_data['Time'],
        y=obs_data['Level'],
        line=dict(color=(app_colors['blue']),
                  width=6),
        fill='tozeroy',
        fillcolor=app_colors['blue'],
    )
    observed_data = get_observed_data()
    forecast_data = get_forecast_data()
    forecast_data = bridge_to_fore(observed_data, forecast_data)
    forecast_plot = Scatter(
        name='Level Forecast',
        x=forecast_data['Time'],
        y=forecast_data['Level'],
        line=dict(
            color=(app_colors['green']),
            width=6,
        ),
        fill='tozeroy',
        mode="lines",
        dx=5,
    )

    # get range of y axis
    y_lowest = min(min(list(obs_data['Level'])), min(
        list(forecast_data['Level']))) - 2
    y_highest = max(max(list(obs_data['Level'])), max(
        list(forecast_data['Level']))) + 5

    x_lowest = obs_data['Time'].iloc[0]
    x_highest = forecast_data['Time'].iloc[-1]
    print(x_lowest, x_highest)

    zone1 = Scatter(
        name='Action Stage',
        x=[x_lowest, x_highest],
        y=[9, 9],
        fill=None,
        mode='lines',
        line_color='#696300')
    zone2 = Scatter(
        name='Flood Stage',
        x=[x_lowest, x_highest],
        y=[12, 12],
        fill='tonexty',  # fill area between trace0 and trace1
        mode='lines', line_color='#696300')
    zone3 = Scatter(
        name='Moderate Flood Stage',
        x=[x_lowest, x_highest],
        y=[15, 15],
        fill='tonexty',  # fill area between trace0 and trace1
        mode='lines', line_color='#694200')
    zone4 = Scatter(
        name='Major Flood Stage',
        x=[x_lowest, x_highest],
        y=[22, 22],
        fill='tonexty',  # fill area between trace0 and trace1
        mode='lines', line_color='#691000')
    zone5 = Scatter(
        name='Record',
        x=[x_lowest, x_highest],
        y=[28.62, 28.62],
        fill='tonexty',  # fill area between trace0 and trace1
        mode='lines',
        line_color='#9c0000',
    )

    current_level = obs_data['Level'].iloc[-1]
    level_metric_str = "Level: " + str(current_level) + "ft"
    templates["draft"] = go_layout.Template(
        layout_annotations=[
            dict(
                name="draft watermark",
                text=level_metric_str,
                textangle=0,
                opacity=0.9,
                font=dict(color=app_colors['red'], size=get_screen_resolution()[
                          'width']*.07),
                xref="paper",
                yref="paper",
                x=0,
                y=0,
                showarrow=False,
            ),
        ]
    )

    return {
        'data': [obs_plot, forecast_plot, zone1, zone2, zone3, zone4, zone5],
        'layout': Layout(
            # height=int(get_screen_resolution()['height'] * .6),
            # width=int(get_screen_resolution()['width'] * .6),
            xaxis={
                'title': "Date",
                'color': 'white',
            },
            yaxis={
                'title': "Water Level ft.",
                'range': ([0, y_highest]),
                'color': 'white',
            },
            margin=dict(t=0, b=50, l=50, r=20),
            plot_bgcolor=app_colors['black'],
            paper_bgcolor=app_colors['black'],
            template="draft",
            legend=dict(
                bgcolor='rgba(0,0,0,0)',
                traceorder="reversed",
                title_font_family="Times New Roman",
                font=dict(
                    family="Courier",
                    size=12,
                    color="white",
                ),
                orientation='h',
                yanchor='bottom',
                xanchor='right',
                y=1.02,
                x=1,
            )
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True, port=3636)
    print("Local hosting your dashboard")

      
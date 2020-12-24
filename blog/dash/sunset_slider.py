from dash import Dash
from dash_core_components import Interval
from dash_html_components import Div
from dash_bootstrap_components import Row, Col
from dash.dependencies import Input, Output
# MY IMPORTS
from helper_methods import *

clima_data = get_climacell_data()

app_colors = {
    'black': '#232931',
    'grey': '#807875',
    'green': '#41aea9',
    'white': "#eeeeee",
    'blue': '#16697a',
    'purple': '#9d65c9',
    'red': "#ff5747",
}

theme = {
    'dark': True,
    'detail': '#007439',
    'primary': '#00EA64',
    'secondary': '#6E6E6E',
}

############################## STYLE ##############################################
def get_gradient1_style(clima_data):
    return {
        # creates a gradient background
        'background': app_colors['black'],
        'background': get_gradient(
            1, 
            clima_data['sunrise_value'], 
            clima_data['sunset_value'], 
            app_colors['red'], 
            'yellow', 
            'black'
        ),
        # no padding to keep proportions
        'padding': 0,
        # grid layout to allow for overlapping
        'display': 'grid',
        'grid-template-columns': '1fr',
    }

def get_gradient2_style(clima_data):
    return {
        'background': app_colors['red'],
        'background': get_gradient(
            2, 
            clima_data['sunrise_value'], 
            clima_data['sunset_value'],
            app_colors['red'], 
            'yellow', 
            'black'                            
        ),
        'padding': 0,
    }

def get_sun_row_style():
    return {
        # 'border': '.5em solid black',
        # 'border-radius': '.25em',
        'margin': 0,
    }


def get_time_slider_style(percent=0):
    return {
        'background': 'grey',
        'left': f'{int(get_mins_from_midnight() / (24 * 60))}%',
        'padding': 0,
        'grid-row-start': 1,
        'grid-column-start': 1,
        'position': 'relative',
        'background': 'yellow',
        'width': '2px',
        'height': '45px',
        'margin-left': f'{percent * 2}%',
        'padding': 0,
    }


def get_sunrise_style():
    return {
        'color': app_colors['red'],
        'font-size': '1em',
        'font-weight': 900,
        'text-align': 'center',
        'position': 'absolute',
        'float': 'left'
    }

def get_sunset_style():
    return {
        'color': app_colors['red'],
        'font-size': '1em',
        'font-weight': 900,
        'text-align': 'center',
        'float': 'right',
        'position': 'relative',
        'top': 0,
        'left': 0,
    }

# from django_plotly_dash import DjangoDash
# app = DjangoDash('SunsetGauge')
app = Dash("sun stuff")

################################ LAYOUT ############################################
app.layout = Row(
            style=get_sun_row_style(),
            children=[
                ################ first half of the gradient background ###################
                Col(
                    id='gradient1',
                    width=6,
                    style=get_gradient1_style(clima_data),
                    children=[
                        ################ time slider ###################
                        Div(
                            id='time-slider',
                            style=get_time_slider_style(),
                        ),

                        ################ sunrise time display text ###################
                        Div(
                            id='sunrise',
                            style=get_sunrise_style(),
                        ),
                    ],
                ),  # end first half of row

                Col(
                    id='gradient2',
                    width=6,
                    style=get_gradient2_style(clima_data),
                    children=[
                        Div(
                            id='sunset',
                            style=get_sunset_style(),
                        ),
                    ]
                ),  # end second half of row

                Interval(
                    id="minute-interval",
                    interval=1*1000,
                    n_intervals=0
                )
        ],  # end row children


    )

######################################## CALLBACK ##################################
# update time slider on the sunset gauge
@app.callback(
    [
    Output(component_id='gradient1', component_property='children'),
    Output(component_id='gradient2', component_property='children'),
    ],
    [Input(component_id='minute-interval', component_property='interval')]
)
def update_time_slider(n):
    percent = get_mins_from_midnight() / (24 * 60)
    percent *= 100
    print("slider update!")
    # two gradients, if the day is more than half over, the
    # slider needs to be on the seond gradient
    if percent < 50:
        return (
            [
                Div(
                    id='slider-marker',
                    style=get_time_slider_style(percent),
                ),
                Div(
                    id='sunrise',
                    style=get_sunrise_style(),
                ),
            ],
            Div(
                id='sunset',
                style=get_sunset_style(),
            ),
        )

    else:
        return (
            Div(
                id='sunrise',
                style=get_sunrise_style(),
            ),
            [
                Div(
                    id='slider-marker',
                    style=get_time_slider_style(),
                ),
                Div(
                    id='sunset',
                    style=get_sunset_style(),
                ),
            ]
        )






if __name__ == '__main__':
    app.run_server(debug=True, port=3636)
    print("Local hosting your dashboard")

               

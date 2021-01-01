from dash import Dash
from dash_core_components import Interval
from dash_html_components import Div
from dash_daq import LEDDisplay
from dash.dependencies import Input, Output
# MY IMPORTS
from helper_methods import get_time, get_time_postfix

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

def get_current_time_style():
    return {
        'background-color': 'black',
        'margin-left': 'auto',
    }

def get_time_postfix_style():
    return {
        'color': app_colors['red'],
        'font-size': '3em',
        'font-weight': 900,
        'margin-top': '3%',
        'margin-bottom': '3%',
        'margin-left': '1%',
        'margin-right': 'auto',
        'background-color': 'black',
        'z-index': 1,
        
    }

app = Dash("clock")

app.layout = Div([
    LEDDisplay(
        id='current_time',
        value=str(get_time()),
        backgroundColor = app_colors['black'],
        color=app_colors['red'],
        style=get_current_time_style(),
    ),

    ################_Time Postfix_#########################
    Div(
        id='time_postfix',
        style=get_time_postfix_style(),
    ),

    Interval(
        id='minute_interval',
        interval=60*1000,
    ),

])


@app.callback(
    [
        Output(component_id='current_time', component_property='children'),
        Output(component_id='time_postfix', component_property='children'),
        # Output(component_id='date-display', component_property='children'),
    ],
    [Input(component_id='minute_interval', component_property='interval')]
)
def update_output_div(interval):
    print('time update!')
    return get_time(), get_time_postfix(),  # get_date()


if __name__ == '__main__':
    print("Local hosting your dashboard")
    app.run_server(debug=True, port=3636)
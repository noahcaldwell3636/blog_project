from .helper_methods import *
import dash_html_components as html

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




def get_date_display_style():
    return {
        'color': app_colors['red'],
        'font-size': '3em',
        'font-weight': 900,
        'margin-top': 'auto',
        'margin-bottom': 'auto',
        'padding-left': '5%',
        'background-color': app_colors['black'],
        'z-index': 1,
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



















######################################################################
# DECORATORS

def give_hours_axis(*children):

    span = html.Span(style={
        'background-color': 'red',
        'width': '100%',
        'display': 'inline-block',
    })

    x_axis = html.P(
            ["12 3 6 9 12 3 6 9 12", span], 
            style={
                'position': 'absolute',
                'bottom': "7.5%",
                'color': 'white',
                'width': '100%',
                'text-align': 'justify',
                'padding-right': '2%',
                'height': 0,
            },   
        )

    return html.Div(
            id="border_container",
            children = list(children) + [ x_axis, span],
            style={
                'padding': '.3rem',
                'position': 'relative',
                'background': 'black',
                'border': '.4em ridge #423d3b',
                'text-align': 'justify',
            }
        )
    
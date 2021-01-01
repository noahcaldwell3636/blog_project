from dash import Dash
from dash_core_components import Interval
from dash_html_components import Div, P
from dash_bootstrap_components import Row, Col
from dash.dependencies import Input, Output
# MY IMPORTS
from helper_methods import get_climacell_data, format_datetime

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

app = Dash("weather metrics")

latitude_style = {
        'color': app_colors['grey'],
        'display': 'inline-block',
        'font-size': '130%',
        'background-color': app_colors['black'],
        'text-align': 'right',
    }

longitude_style = {
        'color': app_colors['grey'],
        'display': 'inline-block',
        'font-size': '130%',
        'background-color': app_colors['black'],
        'text-align': 'left',
    }

obs_time_style = {
        'color': app_colors['grey'],
        'font-size': '130%',
        'background-color': app_colors['black'],
        'padding-bottom': '3%',
    }

temp_style = {
        'color': app_colors['red'],
        'font-size': '8em',
        'font-weight': 900,
        'text-shadow': '0.02em 0.02em 0 ' + app_colors['blue'], 
        # 'background-color': app_colors['black'], # allows overlapping to deal with spacing 
        'margin-top': '-8%',
        'margin-bottom': '-7%',
        'z-index': 0,
        'margin-left': 'auto',
        'margin-right': 'auto',
    }

feels_like_style = {
        'color': app_colors['grey'],
        'font-size': '1.5em',
        'font-weight': 900,
        'text-shadow': '0.02em 0.02em 0 ' + app_colors['blue'], 
        'background-color': app_colors['black'],
        'margin-left': 'auto',
        'margin-right': 'auto',
    }


weather_code_style = {
        'color': app_colors['red'],
        'font-size': '2em',
        'font-weight': 900,
        'background-color': app_colors['black'],
    }


cloud_cover_style = {
        'color': app_colors['red'],
        'font-size': '2em',
        'font-weight': 900,
        'background-color': app_colors['black'],
    }


barometer_style = {
        'color': app_colors['red'],
        'font-size': '2em',
        'font-weight': 900,
        'background-color': app_colors['black'],
    }

humidity_style = {
        'color': app_colors['red'],
        'font-size': '2em',
        'font-weight': 900,
        'background-color': app_colors['black'],
    }

precipitation_type_style = {
        'color': app_colors['red'],
        'font-size': '2em',
        'font-weight': 900,
        'background-color': app_colors['black'],
    }

visability_style = {
        'color': app_colors['red'],
        'font-size': '2em',
        'font-weight': 900,
        'background-color': app_colors['black'],
    }

wind_gust_style = {
        'color': app_colors['red'],
        'font-size': '2em',
        'font-weight': 900,
        'background-color': app_colors['black'],
        'text-align': 'center',
        'margin': '0% 0% 0% 0%',
    }

wind_speed_style = {
        'color': app_colors['red'],
        'font-size': '2em',
        'font-weight': 900,
        'background-color': app_colors['black'],
        'text-align': 'center',
        'margin': '0% 0% 0% 0%',
    }




sunrise_style = {
        'color': app_colors['red'],
        'font-size': '1em',
        'font-weight': 900,
        'text-align': 'center',
        'position': 'absolute',
        'float': 'left'
    }

sunset_style = {
        'color': app_colors['red'],
        'font-size': '1em',
        'font-weight': 900,
        'text-align': 'center',
        'float': 'right',
        'position': 'relative',
        'top': 0,
        'left': 0,
    }

sunrise_text_style = {
        'float': 'left',
    }



app.layout = Col([  # ->>>>> metrics on the right column
    Row([  # ->>>>> coordinate row

        ##########Latitude##################
        Div(
            id='latitude',
            style=latitude_style,
        ),

        ##########Longitude##################
        Div(
            id='longitude',
            style=longitude_style,
        ),

    ],),


    ###############_last_update_###############
    Row(Div(
        id='obs_time',
        style=obs_time_style,
    ),),


    ####################_Temperature_######################################
    Row(P(
        id='temp',
        style=temp_style,
    ),),

    ####################_Feels like temperature_######################################
    Row(Div(
        id='feels_like',
        style=feels_like_style,
    ),),

    ####################_weather_description_######################################
    Row(Div(
        id='weather_code',
        style=weather_code_style,
    ),),

    ####################_cloud_cover_##############################################
    Row(Div(
        id='cloud-cover',
        style=cloud_cover_style,
    ),),

    ####################_barometer_##########################################
    Row(Div(
        id='barometer',
        style=barometer_style,
    ),),

    ####################_humidity_###########################################
    Row(Div(
        id='humidity',
        style=humidity_style,
    ),),


    ####################_percip_type_#########################################
    Row(Div(
        id='precipitation_type',
        style=precipitation_type_style,
    ),),

    ####################_visability_###########################################
    Row(Div(
        id='visability',
        style=visability_style,
    ),),

    ####################_wind_gust_######################################
    Row(Div(
        id='wind_gust',
        style=wind_gust_style,
    ),),

    ####################_wind_speed_######################################
    Row(Div(
        id='wind_speed',
        style=wind_speed_style,
    ),),

    Row([
        Div(
            id='sunrise',
            style=sunrise_style,
        ),
        Div(
            id='sunset',
            style=sunset_style,
        ),
    ]),

    Interval(
        id="metric_interval",
        interval = 6 * 1000,
    ),

],)





@app.callback(
    [
        Output(component_id='temp', component_property='children'),
        Output(component_id='barometer', component_property='children'),
        Output(component_id='cloud-cover', component_property='children'),
        Output(component_id='feels_like', component_property='children'),
        Output(component_id='humidity', component_property='children'),
        Output(component_id='latitude', component_property='children'),
        Output(component_id='longitude', component_property='children'),
        Output(component_id='obs_time', component_property='children'),
        Output(component_id='precipitation_type', component_property='children'),
        Output(component_id='sunrise', component_property='children'),
        Output(component_id='sunset', component_property='children'),
        Output(component_id='visability', component_property='children'),
        Output(component_id='weather_code', component_property='children'),
        Output(component_id='wind_gust', component_property='children'),
        Output(component_id='wind_speed', component_property='children'),
    ],
    [Input(component_id='metric_interval', component_property='interval')]
)
def update_output_div(interval):
    # Sometimes Clima cell gives data errors this try-except statement
    # will use the most recent data it did fetch. This remedy will work when the
    # dashboard has gotten at least one good dataset. To see the error handling
    # when an initial dataset was never retrived since the porgram was started,
    # see the 'get_climacell_data' method in helper_methodds for more.
    try:
        data = get_climacell_data()
        most_recent_clima_data = data
    except:
        data = most_recent_clima_data
        raise ValueError(
            'ClimaCell may be providing DataErrors, we fetched the most recent dataset.')

    print("climacell data update")
    return (
        str(round(data['temp_value'], 1)) + " " + str(data['temp_units']),
        str(data['baro_pressure_value']) + " " + data['baro_pressure_units'],
        "Cloud Cover: " + str(data['cloud_cover_value']) +
        str(data['cloud_cover_units']),
        "Feels Like: " +
        str(round(data['feels_like_value'], 1)) +
        str(data['feels_like_units']),
        "Humidity: " + str(data['humidity_value']) +
        str(data['humidity_units']),
        "(" + str(data['lat']) + "\N{DEGREE SIGN},",
        str(data['long']) + "\N{DEGREE SIGN}" + ")",
        "updated: " + str(data['obs_time']),
        "Precipitation: " + str(data['precipitation_type_value']),
        [
            P(
                "Sunrise",
                style=sunrise_text_style,
            ),
            P(
                format_datetime(data['sunrise_value'], date=False),
                style=sunrise_text_style,
            ),
        ],
        [
            Div("Sunset"),
            Div(format_datetime(data['sunset_value'], date=False))
        ],
        "Visibility: " + str(data['visibility_value']) +
        str(data['visibility_units']),
        "Weather: " + str(data['weather_code_value']),
        "Top Wind Gust: " + str(data['wind_gust_value']) +
        str(data['wind_gust_value']),
        "Wind Speed: " + str(data['wind_speed_value']) +
        str(data['wind_speed_value']),
    )



if __name__ == '__main__':
    print("Local hosting your dashboard")
    app.run_server(debug=True, port=3636)
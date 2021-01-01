import plotly
import plotly.graph_objs as go
import plotly.io as pio
import dash
import dash_html_components as html
import dash_daq as daq
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output
# MY IMPORTS
from helper_methods import *
from layout import *


################################################################################
##########################_CONSTANTS_###########################################
################################################################################
app_colors = {
    'black': '#232931',
    'grey': '#807875',
    'green': '#41aea9',
    'white': "#eeeeee",
    'blue': '#16697a',
    'purple': '#9d65c9',
    'red': "#ff5747",
}

theme =  {
    'dark': True,
    'detail': '#007439',
    'primary': '#00EA64',
    'secondary': '#6E6E6E',
}

external_stylesheets = [dbc.themes.BOOTSTRAP]

#################################################################################
################################_GET_DATA_#######################################
#################################################################################
observed_data = get_observed_data()
forecast_data = get_forecast_data()
forecast_data = bridge_to_fore(observed_data, forecast_data)
most_recent_clima_data = get_climacell_data()


##################################################################################
##################################_LAYOUT_########################################
##################################################################################

########### CREATE APP ######################
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
########### CREATE APP ######################


########### LAYOUT ######################
app.layout = html.Div(
style={
    'background-color': app_colors['black'],
    # 'background-image': 'static/bg.png',
    'margin': 0,
},
children=[

    dcc.Interval(
            id='flood-update-interval',
            interval= 60 * 1000,
            n_intervals= 0,
        ),

    dcc.Interval(
            id='time-update-interval',
            interval= 10 * 1000,
            n_intervals= 0,
        ),

    dbc.Row([ # ->>>>>>>>>>>> FIRST ROW WITH GRAPH AND METRICS

        #################_FLOOD_GRAPH_###########################
        dbc.Col(
            width=8,
            children=[
                html.Div(dcc.Graph(id='flood-graph', animate=False)),
            ],
        ),
        #################_FLOOD_GRAPH_###########################

        
        dbc.Col([ # ->>>>> metrics on the right column

            dbc.Row([ # ->>>>> coordinate row

                ##########Latitude##################
                html.Div(
                    id='latitude',
                    style=get_latitude_style(),
                ),

                ##########Longitude##################
                html.Div(
                    id='longitude',
                    style=get_longitude_style(),
                ),
                
            ],),
            

            ###############_last_update_###############
            dbc.Row(html.Div(
                    id='obs_time',
                    style=get_obs_time_style(),
            ),),


            ####################_Temperature_######################################
            dbc.Row(html.P(
                id='temp',
                style=get_temp_style(),
            ),),

            ####################_Feels like temperature_######################################
            dbc.Row(html.Div(
                id='feels_like',
                style=get_feels_like_style(),
            ),),

            ####################_weather_description_######################################
            dbc.Row(html.Div(
                id='weather_code',
                style=get_weather_code_style(),
            ),),

            ####################_cloud_cover_##############################################
            dbc.Row(html.Div(
                id='cloud-cover',
                style=get_cloud_cover_style(),
            ),),

            ####################_barometer_##########################################
            dbc.Row(html.Div(
                id='barometer',
                style=get_barometer_style(),
            ),),

            ####################_humidity_###########################################
            dbc.Row(html.Div(
                id='humidity',
                style=get_barometer_style(),
            ),),


            ####################_percip_type_#########################################
            dbc.Row(html.Div(
                id='precipitation_type',
                style=get_precipitation_type_style(),
            ),),

            ####################_visability_###########################################
            dbc.Row(html.Div(
                id='visability',
                style=get_visability_style(),
            ),),

            ####################_wind_gust_######################################
            dbc.Row(html.Div(
                id='wind_gust',
                style=get_wind_gust_style(),
            ),),

            ####################_wind_speed_######################################
            dbc.Row(html.Div(
                id='wind_speed',
                style=get_wind_speed_style(),
            ),),


            give_hours_axis(
                dbc.Row(
                    id='datetime_row',
                    style=get_datetime_row_style(),
                    children = [ #---->> clock and date row
                    ################_Time LED_#########################
                    
                    ###############_Date Display_#########################
                    # html.Div(
                    #     id='date-display',
                    #     style=get_date_display_style(),
                    # ),

                ],), # end time/date row

                dbc.Row( # -->>> sunrise/set slider
                    style=get_sun_row_style(),
                    children=[
                        ################ first half of the gradient background###################
                        dbc.Col(
                            id='gradient1', 
                            width=6, 
                            style=get_gradient1_style(most_recent_clima_data),
                            children=[

                                ################ time slider ###################
                                html.Div(
                                    id='time-slider',   
                                    style=get_time_slider_style(),                  
                                ),

                                ################ sunrise time display text ###################
                                html.Div(
                                    id='sunrise',
                                    style=get_sunrise_style(),
                                ),
                            ],
                        ), # end first half of row

                        dbc.Col(
                            id='gradient2', 
                            width=6, 
                            style=get_gradient2_style(most_recent_clima_data),
                            children=[
                                html.Div(
                                    id='sunset',
                                    style=get_sunset_style(),
                                ),
                            ]
                        ), # end second half of row

                    ] # end row children
                ), 
            ) # end sun rise/set row

        ]), # end of the right metrics column

    ],), # end of graph and metrics row

    # dbc.Row(
    #     style={
    #         # nothing yet!
    #     },
    #     children=[
    #         html.Button(
    #             id="debug_kill_program",
    #             n_clicks=0,
    #             style={
    #                 'text': 'kill dashboard.',
    #                 'color': 'red',
    #             }
    #         )
    #     ]
    # )









],)   

##################################################################################################################################
##################################################################################################################################
##################################_CALLBACKS_#####################################################################################
##################################################################################################################################
##################################################################################################################################



@app.callback(
    Output(component_id='flood-graph', component_property='figure'),
    [Input('flood-update-interval', 'interval')])
def update_flood_graph(interval):
    print('graph-update!')
    obs_data = get_observed_data()
    obs_plot = go.Scatter(
        name='Observed Level',
        x=obs_data['Time'], 
        y=obs_data['Level'],
        line = dict(color = (app_colors['blue']),
                            width = 6),
        fill='tozeroy',
        fillcolor=app_colors['blue'],
    )

    forecast_data = get_forecast_data()
    forecast_data = bridge_to_fore(observed_data, forecast_data)
    forecast_plot = go.Scatter(
        name='Level Forecast',
        x=forecast_data['Time'],
        y=forecast_data['Level'],
        line = dict(
            color = (app_colors['green']),
            width = 6,
        ),
        fill='tozeroy',
        mode="lines",
        dx=5,
    )

    # get range of y axis
    y_lowest = min( min(list(obs_data['Level'])), min(list(forecast_data['Level'])) ) - 2
    y_highest = max( max(list(obs_data['Level'])), max(list(forecast_data['Level'])) ) + 5

    x_lowest = obs_data['Time'].iloc[0]
    x_highest = forecast_data['Time'].iloc[-1]
    print(x_lowest, x_highest)

    zone1 = go.Scatter(
        name='Action Stage',
        x=[x_lowest, x_highest], 
        y=[9, 9],
        fill=None,
        mode='lines',
        line_color='#696300')
    zone2 = go.Scatter(
        name='Flood Stage',
        x=[x_lowest, x_highest],
        y=[12, 12],
        fill='tonexty', # fill area between trace0 and trace1
        mode='lines', line_color='#696300')
    zone3 = go.Scatter(
        name='Moderate Flood Stage',
        x=[x_lowest, x_highest],
        y=[15, 15],
        fill='tonexty', # fill area between trace0 and trace1
        mode='lines', line_color='#694200')
    zone4 = go.Scatter(
        name='Major Flood Stage',
        x=[x_lowest, x_highest],
        y=[22, 22],
        fill='tonexty', # fill area between trace0 and trace1
        mode='lines', line_color='#691000')
    zone5 = go.Scatter(
        name='Record',
        x=[x_lowest, x_highest],
        y=[28.62, 28.62],
        fill='tonexty', # fill area between trace0 and trace1
        mode='lines',
        line_color='#9c0000',
        )

    current_level = obs_data['Level'].iloc[-1]
    level_metric_str = "Level: " + str(current_level) + "ft"
    pio.templates["draft"] = go.layout.Template(
        layout_annotations=[
            dict(
                name="draft watermark",
                text=level_metric_str,
                textangle=0,
                opacity=0.9,
                font=dict(color=app_colors['red'], size=get_screen_resolution()['width']*.07),
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
        'layout': go.Layout(
            height=int(get_screen_resolution()['height'] * .6),
            width=int(get_screen_resolution()['width'] * .6),
            xaxis={
                'title': "Date",
                'color': 'white',
            },
            yaxis={
                'title': "Water Level ft.",
                'range': ([0, y_highest]),
                'color': 'white',
            },
            margin=dict(t=0, b=50, l=50, r=0),
            plot_bgcolor = app_colors['black'],
            paper_bgcolor = app_colors['black'],
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
    [Input(component_id='flood-update-interval', component_property='interval')]
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
        raise ValueError('ClimaCell may be providing DataErrors, we fetched the most recent dataset.')

    print("climacell data update!")
    return (
        str(round(data['temp_value'], 1)) + " " + str(data['temp_units']),
        str(data['baro_pressure_value']) + " " + data['baro_pressure_units'],
        "Cloud Cover: " + str(data['cloud_cover_value']) + str(data['cloud_cover_units']),
        "Feels Like: " + str(round(data['feels_like_value'], 1)) + str(data['feels_like_units']),
        "Humidity: " + str(data['humidity_value']) + str(data['humidity_units']),
        "(" + str(data['lat']) + "\N{DEGREE SIGN},",
        str(data['long']) + "\N{DEGREE SIGN}" + ")",
        "updated: " + str(data['obs_time']),
        "Precipitation: " + str(data['precipitation_type_value']),
        [
            html.P(
                "Sunrise",
                style=get_sunrise_text_style(),    
            ),
            html.P(
                format_datetime(data['sunrise_value'], date=False),
                style=get_sunrise_text_style(),
            ),
        ],
        [
            html.Div("Sunset"), 
            html.Div(format_datetime(data['sunset_value'], date=False))
        ],
        "Visibility: " + str(data['visibility_value']) + str(data['visibility_units']),
        "Weather: " + str(data['weather_code_value']),
        "Top Wind Gust: " + str(data['wind_gust_value']) + str(data['wind_gust_value']),
        "Wind Speed: " + str(data['wind_speed_value']) + str(data['wind_speed_value']),
    )







@app.callback(
    [
    Output(component_id='current_time', component_property='children'),
    Output(component_id='time_postfix', component_property='children'),
    # Output(component_id='date-display', component_property='children'),
    ],
    [Input(component_id='time-update-interval', component_property='interval')]
)
def update_output_div(interval):
    print('time update!')
    return get_time(), get_time_postfix(), #get_date()






############################################################
# update time slider on the sunset gauge
@app.callback(
    Output(component_id='gradient1', component_property='children'),
    Output(component_id='gradient2', component_property='children'),
    [Input(component_id='flood-update-interval', component_property='interval')]
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
                html.Div(
                    id='slider-marker',
                    style = get_time_slider_style(percent),
                ),
                html.Div(
                    id='sunrise',
                    style=get_sunrise_style(),
                ),
            ],
            html.Div(
                    id='sunset',
                    style=get_sunset_style(),
                ),
        )

    else:
        return (
            html.Div(
                id='sunrise',
                style=get_sunrise_style(),
            ), 
            [
                html.Div(
                id='slider-marker',
                style = get_time_slider_style(),
                ),
                html.Div(
                    id='sunset',
                    style=get_sunset_style(),
                ),
            ]
        )
    


# # debug kill program method
# @app.callback([Input('debug_kill_program', 'n_clicks')])
# def on_click(n_clicks):
#     if n_clicks != None:
#         exit()

############################################################################################################################################
############################################################################################################################################
#########################################_MAIN_#############################################################################################
############################################################################################################################################
############################################################################################################################################

# if __name__ == '__main__':
#     app.run_server(debug=True,port=6969)
#     print("Local hosting your dashboard")

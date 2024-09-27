import os
import pandas as pd
import plotly.express as px
import dicts_2024
from get_lap_times import get_lap_times

"""
Retrieves lap times for two drivers of a specified team in a specific race and plots a comparison of their lap times.

This script performs the following steps:
1. Retrieves drivers for the specified team from the `dicts_2024` dictionary.
2. Calls the `get_lap_times` function to download lap data for both drivers for the specified race.
3. Loads the CSV files for the drivers, converts lap times to float, and trims the data to the shortest number of laps.
4. Combines the data for both drivers and creates a Plotly line chart to compare their lap times.
5. Displays the lap time comparison in a Plotly interactive chart.

Parameters:
    team (str): The name of the team (e.g., 'McLaren Formula 1 Team').
    race (str): The name of the race (e.g., 'Miami').
    year (str): The year of the race (e.g., '2024').

Team names supported (2024 Season):
    - Red Bull Racing
    - McLaren Formula 1 Team
    - Mercedes-AMG PETRONAS F1 Team
    - Scuderia Ferrari
    - Aston Martin Aramco F1 Team
    - Visa Cash App RB Formula One Team
    - BWT Alpine F1 Team
    - Williams Racing
    - Stake F1 Team Kick Sauber
    - MoneyGram Haas F1 Team

Race names supported (2024 Season):
    - Bahrain
    - Saudi Arabia
    - Australia
    - Japan
    - China
    - Miami
    - Emilia-Romagna
    - Monaco
    - Canada
    - Spain
    - Austria
    - Great Britain
    - Hungary
    - Belgium
    - Netherlands
    - Italy
    - Azerbaijan
    - Singapore
    - Austin
    - Mexico
    - Brazil
    - Las Vegas
    - Qatar
    - Abu Dhabi

Returns:
    None: The function plots the lap time comparison for both drivers using Plotly.

Raises:
    ValueError: If the number of drivers in the team is not equal to 2.

Example:
    This script compares the lap times of both McLaren drivers (e.g., Oscar Piastri and Lando Norris) in the Miami 2024 race.
"""

team = 'Red Bull Racing'
race = 'Miami'
year = '2024'

team_drivers = [driver for driver, info in dicts_2024.drivers_info_2024.items() if info['team_name'] == team]

if len(team_drivers) != 2:

    raise ValueError(f"Expected 2 drivers for team {team}, but found{len(team_drivers)}")

for driver in team_drivers:

    get_lap_times(driver, race, year=year)

data_driver_1 = pd.read_csv(f'C:/Users/Francisco Valerio/Desktop/F1 project/F1-project/data/{race}_{year}/{dicts_2024.drivers_info_2024[team_drivers[0]]["team_name"]}/{dicts_2024.drivers_info_2024[team_drivers[0]]["acronym"]}_lap_times_{race}_{year}.csv')
data_driver_2 = pd.read_csv(f'C:/Users/Francisco Valerio/Desktop/F1 project/F1-project/data/{race}_{year}/{dicts_2024.drivers_info_2024[team_drivers[1]]["team_name"]}/{dicts_2024.drivers_info_2024[team_drivers[1]]["acronym"]}_lap_times_{race}_{year}.csv')

data_driver_1['lap_duration'] = data_driver_1['lap_duration'].astype(float)
data_driver_2['lap_duration'] = data_driver_2['lap_duration'].astype(float)

min_laps = min(len(data_driver_1), len(data_driver_2))

data_driver_1 = data_driver_1.iloc[:min_laps]
data_driver_2 = data_driver_2.iloc[:min_laps]

data_driver_1['Driver'] = team_drivers[0]
data_driver_2['Driver'] = team_drivers[1]

combined_data = pd.concat([data_driver_1, data_driver_2])

lap_times = px.line(combined_data,
                    x = 'lap_number',
                    y = 'lap_duration',
                    color = 'Driver',
                    title = f'Comparación de tiempos de vuelta {team_drivers[0]} - {team_drivers[1]} ({race} - {year})',
                    labels={'lap_duration': 'Tiempo de vuelta (s)', 'lap_number': 'Vuelta'},
                    markers=True,
                    hover_data=['duration_sector_1', 'duration_sector_2', 'duration_sector_3'],
                    color_discrete_sequence=px.colors.qualitative.Plotly
                    )

lap_times.update_layout(
    title=dict(font=dict(size=18)),
    xaxis_title=dict(text="Vuelta", font=dict(size=18)),
    yaxis_title=dict(text="Tiempo de vuelta (s)", font=dict(size=18)),
    legend=dict(font=dict(size=14)),
)

lap_times.update_traces(
    marker=dict(size=10),
    line=dict(width=3)
)

lap_times.show()


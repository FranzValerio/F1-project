import pandas as pd
import plotly.express as px

data_checo_singapore_2024 = pd.read_csv('data/Singapore_2024/PER_lap_times_Singapore2024.csv')

data_max_singapore_2024 = pd.read_csv('data/Singapore_2024/VER_lap_times_Singapore2024.csv')

data_lando_singapore_2024 = pd.read_csv('data/Singapore_2024/NOR_lap_times_Singapore2024.csv')

data_checo_singapore_2024['lap_duration'] = data_checo_singapore_2024['lap_duration'].astype(float)
data_max_singapore_2024['lap_duration'] = data_max_singapore_2024['lap_duration'].astype(float)
data_lando_singapore_2024['lap_duration'] = data_lando_singapore_2024['lap_duration'].astype(float)

min_laps = min(len(data_checo_singapore_2024), len(data_max_singapore_2024), len(data_lando_singapore_2024))

data_checo_singapore_2024 = data_checo_singapore_2024.iloc[:min_laps]
data_max_singapore_2024 = data_max_singapore_2024.iloc[:min_laps]
data_lando_singapore_2024 = data_lando_singapore_2024.iloc[:min_laps]

data_checo_singapore_2024['Driver'] = 'Checo'
data_max_singapore_2024['Driver'] = 'Max'
data_lando_singapore_2024['Driver'] = 'Norris'

combined_data = pd.concat([data_checo_singapore_2024, data_max_singapore_2024, data_lando_singapore_2024])

lap_times = px.line(combined_data,
                    x = 'lap_number',
                    y = 'lap_duration',
                    color = 'Driver',
                    title = "Comparación de tiempos de vuelta NOR - VER - PER (Singapur 2024)",
                    labels = {'lap_duration': 'Tiempo de vuelta (s)', 'lap_number': 'Vuelta'},
                    markers=True,
                    hover_data=['duration_sector_1', 'duration_sector_2', 'duration_sector_3'],
                    color_discrete_map={
                        'Checo': '#3671C6',
                        'Max': '#3671C6',
                        'Norris': '#F58020'
                    }
                    )

lap_times.update_layout(
    title=dict(font=dict(size=18)),
    xaxis_title = dict(text="Vuelta", font=dict(size=18)),
    yaxis_title = dict(text="Tiempo de vuelta (s)", font=dict(size=18)),
    legend = dict(font=dict(size = 14)),
)

lap_times.update_traces(
    marker=dict(size=10),
    line=dict(width=3)
)

lap_times.show()
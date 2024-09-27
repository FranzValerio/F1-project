'''
dicts_2024

This file contains two dictionaries: "sessions_info_2024" and "drivers_info_2024".

sessions_info_2024 maps the name of the country where the race was held and its corresponding session_key for 
that race.

drivers_info contains the information of the 2024 drivers, including their acronym, driver number and team name

session_key and driver_number are needed to scrap the lap times during a specific race
'''

sessions_info_2024 = {
    'Bahrain': {
        'circuit_short_name': 'Sakhir',
        'session_name': 'Race',
        'session_key': 9472,
        'total_laps': 57},
    'Saudi Arabia': {
        'circuit_short_name': 'Jeddah',
        'session_name': 'Race',
        'session_key': 9480,
        'total_laps': 50},
    'Australia': {
        'circuit_short_name': 'Melbourne',
        'session_name': 'Race',
        'session_key': 9488, 
        'total_laps': 58},
    'Japan': {
        'circuit_short_name': 'Suzuka',
        'session_name': 'Race',
        'session_key': 9496, 
        'total_laps': 53},
    'China': {
        'circuit_short_name': 'Shanghai',
        'session_name': 'Race',
        'session_key': 9673,
        'total_laps': 56}, 
    'Miami': {
        'circuit_short_name': 'Miami',
        'session_name': 'Race',
        'session_key': 9507, 
        'total_laps': 57},  
    'Emilia-Romagna': {
        'circuit_short_name': 'Imola',
        'session_name': 'Race',
        'session_key': 9515,
        'total_laps': 63},
    'Monaco': {
        'circuit_short_name': 'Monte Carlo',
        'session_name': 'Race',
        'session_key': 9523,
        'total_laps': 78},
    'Canada': {
        'circuit_short_name': 'Montreal',
        'session_name': 'Race',
        'session_key': 9531,
        'total_laps': 70}, 
    'Spain': {
        'circuit_short_name': 'Catalunya',
        'session_name': 'Race',
        'session_key': 9539, 
        'total_laps': 66}, 
    'Austria': {
        'circuit_short_name': 'Spielberg',
        'session_name': 'Race',
        'session_key': 9550, 
        'total_laps': 71},
    'Great Britain': {
        'circuit_short_name': 'Silverstone',
        'session_name': 'Race',
        'session_key': 9558, 
        'total_laps': 52},
    'Hungary': {
        'circuit_short_name': 'Hungaroring',
        'session_name': 'Race',
        'session_key': 9566, 
        'total_laps': 70},
    'Belgium': {
        'circuit_short_name': 'Spa-Francorchamps',
        'session_name': 'Race',
        'session_key': 9574, 
        'total_laps': 44},
    'Netherlands': {
        'circuit_short_name': 'Zandvoort',
        'session_name': 'Race',
        'session_key': 9582, 
        'total_laps': 72},
    'Italy': {
        'circuit_short_name': 'Monza',
        'session_name': 'Race',
        'session_key': 9590,
        'total_laps': 53
    },
    'Azerbaijan': {
        'circuit_short_name': 'Baku',
        'session_name': 'Race',
        'session_key': 9598, 
        'total_laps': 51},
    'Singapore': {
        'circuit_short_name': 'Singapore',
        'session_name': 'Race',
        'session_key': 9606, 
        'total_laps': 62},
    'Austin': {
        'circuit_short_name': 'Austin',
        'session_name': 'Race',
        'session_key': 0,
        'total_laps': 56 
    },
    'Mexico': {
        'circuit_short_name': 'Mexico City',
        'session_name': 'Race',
        'session_key': 0,
        'total_laps': 71
    },
    'Brazil': {
        'circuit_short_name': 'Interlagos',
        'session_name': 'Race',
        'session_key': 0,
        'total_laps': 71
    },
    'Las Vegas': {
        'circuit_short_name': 'Las Vegas',
        'session_name': 'Race',
        'session_key': 0,
        'total_laps':50
    },
    'Qatar': {
        'circuit_short_name': 'Lusail',
        'session_name': 'Race',
        'session_key': 0,
        'total_laps': 57
    },
    'Abu Dhabi': {
        'circuit_short_name': 'Yas Marina',
        'session_name': 'Race',
        'session_key': 0,
        'total_laps': 58
    }
    }

drivers_info_2024 = {
    'Max Verstappen': {'acronym': 'VER', 'driver_number': 1, 'team_name': 'Red Bull Racing'},
    'Sergio Pérez': {'acronym': 'PER', 'driver_number': 11, 'team_name': 'Red Bull Racing'},
    'Lando Norris': {'acronym': 'NOR', 'driver_number': 4, 'team_name': 'McLaren Formula 1 Team'},
    'Oscar Piastri': {'acronym': 'PIA', 'driver_number': 81, 'team_name': 'McLaren Formula 1 Team'},
    'Lewis Hamilton': {'acronym': 'HAM', 'driver_number': 44, 'team_name': 'Mercedes-AMG PETRONAS F1 Team'},
    'George Russell': {'acronym': 'RUS', 'driver_number': 63, 'team_name': 'Mercedes-AMG PETRONAS F1 Team'},
    'Charles Leclerc': {'acronym': 'LEC', 'driver_number': 16, 'team_name': 'Scuderia Ferrari'},
    'Carlos Sainz': {'acronym': 'SAI', 'driver_number': 55, 'team_name': 'Scuderia Ferrari'},
    'Oliver Bearman': {'acronym': 'BEA', 'driver_number': 50, 'team_name': 'Scuderia Ferrari'},
    'Fernando Alonso': {'acronym': 'ALO', 'driver_number': 14, 'team_name': 'Aston Martin Aramco F1 Team'},
    'Lance Stroll': {'acronym': 'STR', 'driver_number': 18, 'team_name': 'Aston Martin Aramco F1 Team'},
    'Yuki Tsunoda': {'acronym': 'TSU', 'driver_number': 22, 'team_name': 'Visa Cash App RB Formula One Team'},
    'Daniel Ricciardo': {'acronym': 'RIC', 'driver_number': 3, 'team_name': 'Visa Cash App RB Formula One Team'},
    'Pierre Gasly': {'acronym': 'GAS', 'driver_number': 10, 'team_name': 'BWT Alpine F1 Team'},
    'Esteban Ocon': {'acronym': 'OCO', 'driver_number': 31, 'team_name': 'BWT Alpine F1 Team'},
    'Alexander Albon': {'acronym': 'ALB', 'driver_number': 23, 'team_name': 'Williams Racing'},
    'Logan Sargeant': {'acronym': 'SAR', 'driver_number': 2, 'team_name': 'Williams Racing'},
    'Franco Colapinto': {'acronym': 'COL', 'driver_number': 43, 'team_name': 'Williams Racing'},
    'Valterri Bottas': {'acronym': 'BOT', 'driver_number': 77, 'team_name': 'Stake F1 Team Kick Sauber'},
    'Guanyu Zhou': {'acronym': 'ZHO', 'driver_number': 24, 'team_name': 'Stake F1 Team Kick Sauber'},
    'Nico Hulkenberg': {'acronym': 'HUL', 'driver_number': 27, 'team_name': 'MoneyGram Haas F1 Team'},
    'Kevin Magnussen': {'acronym': 'MAG', 'driver_number': 20, 'team_name': 'MoneyGram Haas F1 Team'}
}
from urllib.request import urlopen
import json
from urllib.parse import quote  # This will handle the URL encoding

"""
session_keys.py

Fetches session keys for all 2024 Formula 1 races from the OpenF1 API and stores them in a dictionary.

This script loops through a list of circuits hosting Formula 1 races in the 2024 season, retrieves the session key 
for each race (specifically the 'Race' session) from the OpenF1 API, and stores the session keys in a dictionary 
(`sessions_info`). The session key is essential for further API calls to retrieve lap times or other race-related data.

Parameters:
    circuits (list of dict): A list of dictionaries where each dictionary contains the short name of the circuit 
                             ('circuit_short_name') and the race name ('race_name').
    year (int): The year of the race season (default is 2024).

Returns:
    None: The script prints the session keys for each race and stores them in the `sessions_info` dictionary.

Raises:
    Exception: Prints an error message if an error occurs during the API request.

Example:
    After running the script, the session keys for all races will be printed:

    Output:
    Race: Bahrain, session_key: 9472
    Race: Saudi Arabia, session_key: 9480
    Race: Australia, session_key: 9488
    ...
    All Session Keys for 2024 season:
    {'Bahrain': 9472, 'Saudi Arabia': 9480, 'Australia': 9488, ...}
"""

circuits = [
    {'circuit_short_name': 'Sakhir', 'race_name': 'Bahrain'},
    {'circuit_short_name': 'Jeddah', 'race_name': 'Saudi Arabia'},
    {'circuit_short_name': 'Melbourne', 'race_name': 'Australia'},
    {'circuit_short_name': 'Suzuka', 'race_name': 'Japan'},
    {'circuit_short_name': 'Shanghai', 'race_name': 'China'},
    {'circuit_short_name': 'Miami', 'race_name': 'United States (Miami)'},
    {'circuit_short_name': 'Imola', 'race_name': 'Italy (Imola)'},
    {'circuit_short_name': 'Monte Carlo', 'race_name': 'Monaco'},
    {'circuit_short_name': 'Montreal', 'race_name': 'Canada'},
    {'circuit_short_name': 'Catalunya', 'race_name': 'Spain'},
    {'circuit_short_name': 'Spielberg', 'race_name': 'Austria'},
    {'circuit_short_name': 'Silverstone', 'race_name': 'Great Britain'},
    {'circuit_short_name': 'Hungaroring', 'race_name': 'Hungary'},
    {'circuit_short_name': 'Spa-Francorchamps', 'race_name': 'Belgium'},
    {'circuit_short_name': 'Zandvoort', 'race_name': 'Netherlands'},
    {'circuit_short_name': 'Monza', 'race_name': 'Italy (Monza)'},
    {'circuit_short_name': 'Baku', 'race_name': 'Azerbaijan'},
    {'circuit_short_name': 'Singapore', 'race_name': 'Singapore'},
    {'circuit_short_name': 'Austin', 'race_name': 'United States (Austin)'},
    {'circuit_short_name': 'Mexico City', 'race_name': 'Mexico'},
    {'circuit_short_name': 'Interlagos', 'race_name': 'Brazil'},
    {'circuit_short_name': 'Las Vegas', 'race_name': 'United States (Las Vegas)'},
    {'circuit_short_name': 'Lusail', 'race_name': 'Qatar'},
    {'circuit_short_name': 'Yas Marina', 'race_name': 'Abu Dhabi'},

]

# Dictionary to store country names and their session keys
sessions_info = {}

# Year of the season
year = 2024

# Loop through each country and retrieve the session_key for each race
for circuit in circuits:
    try:
        # URL-encode the circuit_short_name to handle spaces and special characters
        encoded_circuit = quote(circuit['circuit_short_name'])
        session_name = 'Race'
        
        # Make the API request for the latest session in the given circuit and year
        url = f'https://api.openf1.org/v1/sessions?circuit_short_name={encoded_circuit}&session_name={session_name}&year={year}'
        response = urlopen(url)
        data = json.loads(response.read().decode('utf-8'))

        # Check if data is returned
        if data:
            # Get the session_key from the first item in the list
            session_key = data[0].get('session_key')
            race_name = circuit['race_name']
            sessions_info[race_name] = session_key
            print(f"Race: {race_name}, session_key: {session_key}")
        else:
            print(f"No session data returned for {circuit['race_name']}")
    
    except Exception as e:
        print(f"Error fetching data for {circuit['race_name']}: {e}")

# Print the final dictionary of session keys
print("\nAll Session Keys for 2024 season:")
print(sessions_info)

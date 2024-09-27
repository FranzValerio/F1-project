import os
import json
from urllib.request import urlopen
from urllib.parse import quote  # For URL encoding special characters
import dicts_2024

# Dictionary to store the updated session keys and other data for the 2024 season
updated_sessions_info_2024 = {}

# Year of the season
year = 2024

# Loop through each circuit in the existing dicts_2024 sessions_info_2024
for race_name, race_info in dicts_2024.sessions_info_2024.items():
    try:
        # URL-encode the circuit_short_name to handle spaces and special characters
        encoded_circuit = quote(race_info['circuit_short_name'])
        session_name = race_info['session_name']

        # Make the API request for the session key of the specified race
        url = f'https://api.openf1.org/v1/sessions?circuit_short_name={encoded_circuit}&session_name={session_name}&year={year}'
        response = urlopen(url)
        data = json.loads(response.read().decode('utf-8'))

        # Check if data is returned and fetch the session_key
        if data:
            session_key = data[0].get('session_key')
            # Update the dictionary with the session_key and total_laps from the existing data
            updated_sessions_info_2024[race_name] = {
                'circuit_short_name': race_info['circuit_short_name'],
                'session_name': race_info['session_name'],
                'session_key': session_key,
                'total_laps': race_info['total_laps']
            }
            print(f"Race: {race_name}, session_key: {session_key}")
        else:
            print(f"No session data returned for {race_name}")
    
    except Exception as e:
        print(f"Error fetching data for {race_name}: {e}")

# Save the updated sessions info dictionary in a similar format as sessions_info_2024
print("\nUpdated Session Keys for 2024 season:")
print(updated_sessions_info_2024)

# Optionally, you can save the results as a JSON file for future use
with open('updated_sessions_info_2024.json', 'w') as json_file:
    json.dump(updated_sessions_info_2024, json_file, indent=4)

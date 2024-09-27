from urllib.request import urlopen
import json

"""
last_session_key.py

Fetches the session key for the most recent race session from the OpenF1 API.

This script retrieves the session key for a given race session (e.g., the 'Race' session for the 'Singapore' race in 2024) 
by making a GET request to the OpenF1 API. The session key is essential for further API calls to retrieve lap times or other data.

Parameters:
    method (str): The API method to call (default is 'sessions').
    country_name (str): The name of the country where the race takes place (e.g., 'Singapore').
    session_name (str): The name of the session for the race (e.g., 'Race').
    year (str): The year of the race (e.g., '2024').

Returns:
    None: Prints the session key if data is returned from the API, or a message indicating no data was returned.
    
Example:
    The session key for the 'Race' session in Singapore 2024 will be printed.
    
    Output:
    The session_key for Singapore 2024 is: 9606
"""

method = 'sessions'
country_name = 'Singapore'
session_name = 'Race'
year = '2024'

base_url = f'https://api.openf1.org/v1/{method}?country_name={country_name}&session_name={session_name}&year={year}'

response = urlopen(base_url)

data = json.loads(response.read().decode('utf-8'))

if data:

    session_key = data[0].get('session_key')

    print(f"The session_key for {country_name} {year} is: {session_key}")

else:

    print("No data returned from the API")

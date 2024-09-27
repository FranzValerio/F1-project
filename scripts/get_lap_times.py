from urllib.request import urlopen
from urllib.error import HTTPError
import json
import pandas as pd
import time
import dicts_2024
from tqdm import tqdm
import os

"""
get_lap_times.py

Fetches lap times for a specified driver and race, saves the data in a CSV file, and returns the file path.

This function retrieves lap times for a given driver and race from the OpenF1 API. The data is saved in a structured
directory under the specified base path in the format `{race_name}_{year}/{team_name}/{driver_acronym}_lap_times_{race_name}_{year}.csv`.

The function uses a progress bar to show the scraping process for each lap and handles errors gracefully when API requests fail.

Parameters:
    driver_name (str): The name of the driver (e.g., 'Max Verstappen').
    race_name (str): The name of the race (e.g., 'Singapore').
    year (int, optional): The year of the race (default is 2024).
    base_path (str, optional): The base directory where the data will be saved. Default is 
                               'C:/Users/Francisco Valerio/Desktop/F1 project/data'.

Returns:
    str: The file path of the CSV file that contains the lap times.

Raises:
    ValueError: If the driver or race name is invalid.
    HTTPError: If there is an issue with the API request for a specific lap.
"""

def get_lap_times(driver_name, race_name, year = 2024, base_path = 'C:/Users/Francisco Valerio/Desktop/F1 project/F1-project/data'):

    driver_info = dicts_2024.drivers_info_2024.get(driver_name)
    session_info = dicts_2024.sessions_info_2024.get(race_name)    

    if driver_info and session_info:

        driver_number = driver_info['driver_number']
        driver_acronym = driver_info['acronym']
        team_name = driver_info['team_name']
        session_key = session_info['session_key']
        total_laps = session_info['total_laps']

        #print(f"Total laps for {race_name}: {total_laps}")


        base_url = f'https://api.openf1.org/v1/laps?session_key={session_key}&driver_number={driver_number}&lap_number={{}}'

        race_data = []

        print("Starting Lap Times scraping:")
        print("-"*100)

        for lap_number in tqdm(range(2, total_laps + 1), desc=f"Fetching lap times for {driver_name} in {race_name} {year}", unit="lap"):

            try:

                response = urlopen(base_url.format(lap_number))
                data = json.loads(response.read().decode('utf-8'))

                if data:

                    race_data.append(data[0])
                
                else:
                    print()
                    print(f"No data returned for lap {lap_number}. Response: {data}")

                time.sleep(1)

            except HTTPError as e:

                print(f"HTTP Error for lap {lap_number}: {e.code} {e.reason}")

    else:
        print(f"Invalid driver or race: {driver_name} or {race_name}")

    folder_path = os.path.join(base_path, f"{race_name}_{year}", team_name)
    
    os.makedirs(folder_path, exist_ok=True)

    csv_file_path = os.path.join(folder_path , f'{driver_acronym}_lap_times_{race_name}_{year}.csv')

    df = pd.DataFrame(race_data)

    df.to_csv(csv_file_path, index = False)

    print()
    print(f"CSV file created at: {csv_file_path}")

    return csv_file_path
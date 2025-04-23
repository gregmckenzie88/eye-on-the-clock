#!/usr/bin/env python3
"""
departure_timer.py: Estimate travel time from a fixed origin to a destination using the SerpApi Distance Matrix API and output a departure timer.

Usage:
  python3 departure_timer.py "Destination address by Mode"

Example:
  python3 departure_timer.py "Pearson Airport by Public Transit"
  Time to departure: 56 minutes
  Destination: Pearson Airport
  Transportation: Public transit

Environment Variables:
  SERP_API_KEY: Your SerpApi API key.
  DEPARTURE_ORIGIN: (Optional) Origin address. Defaults to "381 Yonge Street Toronto".
"""
import os
import sys
import argparse
import urllib.parse
import urllib.request
import json
import math

def main():
    parser = argparse.ArgumentParser(description="Estimate travel time and output departure timer.")
    parser.add_argument('query', nargs='+',
                        help="Query in format 'Destination by Mode', e.g. 'Pearson Airport by Public Transit'")
    args = parser.parse_args()
    query = ' '.join(args.query).strip()
    idx = query.lower().rfind(' by ')
    if idx == -1:
        sys.exit("Error: Could not parse input. Expected format: 'Destination by Mode'.")
    dest = query[:idx].strip(' .')
    mode_raw = query[idx+4:].strip(' .')
    if not dest:
        sys.exit("Error: Destination missing before 'by'.")
    if not mode_raw:
        sys.exit("Error: Transportation mode missing after 'by'.")

    mode_low = mode_raw.lower()
    if 'transit' in mode_low:
        google_mode = 'transit'
        mode_output = 'Public transit'
    elif 'drive' in mode_low:
        google_mode = 'driving'
        mode_output = 'Driving'
    elif 'walk' in mode_low:
        google_mode = 'walking'
        mode_output = 'Walking'
    elif 'bike' in mode_low or 'bicycling' in mode_low:
        google_mode = 'bicycling'
        mode_output = 'Bicycling'
    else:
        sys.exit(f"Error: Transportation mode '{mode_raw}' not recognized. "
                 "Supported modes: driving, walking, bicycling, transit.")

    api_key = os.environ.get('SERP_API_KEY')
    if not api_key:
        sys.exit("Error: SERP_API_KEY environment variable not set.")

    origin = os.environ.get('DEPARTURE_ORIGIN', '381 Yonge Street Toronto')
    params = {
        'engine': 'google_maps_distance_matrix',
        'origins': origin,
        'destinations': dest,
        'mode': google_mode,
        'serp_api_key': api_key
    }
    url = 'https://serpapi.com/search.json?' + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
    except Exception as e:
        sys.exit(f"Error: Request to SERP API failed: {e}")

    if 'error' in data:
        sys.exit(f"Error: SERP API error: {data.get('error')}")

    # Extract distance matrix result
    matrix = data.get('distance_matrix', data)
    rows = matrix.get('rows')
    if not rows or not rows[0].get('elements'):
        sys.exit("Error: Unexpected API response format from SERP API.")
    element = rows[0]['elements'][0]
    if element.get('status') != 'OK':
        sys.exit(f"Error: No route found ({element.get('status')}).")

    duration_sec = element['duration']['value']
    minutes = math.ceil(duration_sec / 60)

    print(f"Time to departure: {minutes} minutes")
    print(f"Destination: {dest}")
    print(f"Transportation: {mode_output}")

if __name__ == '__main__':
    main()
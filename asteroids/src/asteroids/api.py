import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_asteroids(date: str) -> dict:
    """Fetch asteroids approaching Earth around a given date from NASA API"""
    api_key = os.getenv("NASA_API_KEY")
    url = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {
        "start_date": date,
        "end_date": date,
        "api_key": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    asteroids = []

    for obj in data["near_earth_objects"][date]:
        name = obj["name"]
        approach_data = obj["close_approach_data"][0]
        distance_km = float(approach_data["miss_distance"]["kilometers"])
        diameter_data = obj["estimated_diameter"]["meters"]
        diameter_m = (diameter_data["estimated_diameter_min"] + diameter_data["estimated_diameter_max"]) / 2

        asteroids.append({
            "name": name,
            "distance_km": round(distance_km, 2),
            "diameter_m": round(diameter_m, 2),
            "approach_date": date
        })

    return {"date": date, "asteroids": asteroids}


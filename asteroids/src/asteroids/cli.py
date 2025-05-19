from .api import get_asteroids
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", help="Date to check for asteroids (YYYY-MM-DD)", required=True)
    args = parser.parse_args()

    result = get_asteroids(args.date)
    result["asteroids"].sort(key=lambda a: a["distance_km"])

    print(f"\nClosest asteroids around {result['date']}:")
    for asteroid in result["asteroids"]:
        name = asteroid["name"]
        diameter = asteroid["diameter_m"]
        distance = asteroid["distance_km"]
        print(f"- {name}: {diameter:.2f}m diameter, {distance:.2f}km from Earth")

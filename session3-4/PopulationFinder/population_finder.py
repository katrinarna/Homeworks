import pandas as pd
import argparse

df = pd.read_csv("/Users/katrinarnadottir/Documents/Homeworks/session3-4/PopulationFinder/worldcities.csv")

#print(df.head())
#print(df.tail())
#print(df.columns)
#print(df.describe())
#print(df.info())

parser = argparse.ArgumentParser(description="Find the population of a given city.")
parser.add_argument("--city", help="City name to find the population for")

parser.add_argument("--country", help="Name of the country")

args = parser.parse_args()

if args.city:
    match = df[df["city"].str.lower() == args.city.lower()]
    if match.empty:
        print(f"Error: City '{args.city}' not found.")
    else:
        population = int(match.iloc[0]["population"])
        print(f"The population of {args.city} is {population:,}")


elif args.country:
    country_match = df[df["country"].str.lower() == args.country.lower()]
    if country_match.empty:
        print(f"Error: Country '{args.country}' not found.")
    else:
        largest = country_match.sort_values("population", ascending=False).iloc[0]
        city = largest["city"]
        population = int(largest["population"])
        print(f"The population of {city} is {population:,}")


else:
    print("Please provide either --city or --country.")
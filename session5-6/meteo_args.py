import argparse
import pandas as pd
clean_df = pd.read_csv("clean_meteo.csv")
clean_df['fecha'] = pd.to_datetime(clean_df['fecha'], errors='coerce')

parser = argparse.ArgumentParser(description="Analyze weather data")
parser.add_argument("--date", help="Get average temperature for a specific date (YYYY-MM-DD)")
args = parser.parse_args()

if args.date:
    try:
        query_date = pd.to_datetime(args.date)
        
        match = clean_df[clean_df['fecha'] == query_date]

        if match.empty:
            print(f"No data found for {args.date}.")
        else:
            temp = match.iloc[0]['tmed']
            print(f"The average temperature for {args.date} was {temp} degrees.")
    except Exception as e:
        print("Invalid date format. Use YYYY-MM-DD.")
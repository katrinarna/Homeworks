import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser(description="Migrate a CSV file to various formats")

parser.add_argument("--input", required=True, help="Input CSV file name")

parser.add_argument(
    "--format",
    required=True,
    choices=["csv", "xlsx", "json", "npz"],
    help="Output file format: csv, xlsx, json, or npz"
)

parser.add_argument("--column", help="Column name to save when format is npz")

args = parser.parse_args()

try:
    df = pd.read_csv(args.input)
except FileNotFoundError:
    print(f"Error: File '{args.input}' not found.")
    raise


if args.format == "npz":
    if not args.column:
        print("Error: --column is required when format is npz.")
        raise ValueError("Missing column for npz export.")

    if args.column not in df.columns:
        print(f"Error: Column '{args.column}' not found in the dataset.")
        raise ValueError("Invalid column name.")

    np.savez("data34_converted.npz", data=df[args.column].to_numpy())
    print("The data has been migrated to data34_converted.npz")
    raise SystemExit


if args.format == "csv":
    df.to_csv("data34_converted.csv", index=False)
    print("The data has been migrated to data34_converted.csv")

elif args.format == "xlsx":
    df.to_excel("data34_converted.xlsx", index=False)
    print("The data has been migrated to data34_converted.xlsx")

elif args.format == "json":
    df.to_json("data34_converted.json", orient="records", indent=2)
    print("The data has been migrated to data34_converted.json")


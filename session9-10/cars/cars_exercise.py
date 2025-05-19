import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/katrinarnadottir/Documents/Homeworks/session9-10/cars/cars.csv')
#print(df.head())
#print(df.columns)

cars = df[["Model", "Power", "Top Speed", "From year"]].copy()
cars.columns = ["model_name", "horsepower", "top_speed", "year"]

cars["horsepower"] = cars["horsepower"].astype(str).str.extract(r"(\d+(?:\.\d+)?)").astype(float)

cars["top_speed"] = cars["top_speed"].astype(str).str.extract(r"(\d+(?:\.\d+)?)").astype(float)

cars["year"] = pd.to_numeric(cars["year"], errors="coerce")

cars = cars.dropna(subset=["model_name", "horsepower", "top_speed", "year"])
cars = cars.drop_duplicates()

#print(cars.head())

# Plot horsepower vs. top speed
plt.figure(figsize=(10, 6))
plt.scatter(cars["horsepower"], cars["top_speed"], alpha=0.5, edgecolors='k')
plt.xlabel("Horsepower")
plt.ylabel("Top Speed (km/h)")
plt.title("Horsepower vs. Top Speed")
plt.grid(True)
#plt.show()

# Filter cars from 2000 onwards
recent_cars = cars[cars["year"] >= 2000]

plt.figure(figsize=(10, 6))
plt.scatter(recent_cars["horsepower"], recent_cars["top_speed"], alpha=0.5, edgecolors='k')
plt.xlabel("Horsepower")
plt.ylabel("Top Speed (km/h)")
plt.title("Horsepower vs. Top Speed (Cars from 2000+)")
plt.grid(True)
plt.show()

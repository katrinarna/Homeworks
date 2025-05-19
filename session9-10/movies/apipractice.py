import pandas as pd
from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv("TMDB_API_KEY")

url = "https://api.themoviedb.org/3/movie/popular"

params = {
    "api_key": api_key,
    "language": "en-US",
    "page": 1
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data["results"])
print(df[["title", "release_date", "vote_average", "popularity"]].head())


import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.scatter(df["vote_average"], df["popularity"], alpha=0.7, c="orchid", edgecolors='black')
plt.title("Popularity vs. Average Vote")
plt.xlabel("Vote Average")
plt.ylabel("Popularity")
plt.grid(True)
#plt.show()

top_rated = df.sort_values("vote_average", ascending=False).head()
print(top_rated[["title", "vote_average"]])

avg_popularity = df["popularity"].mean()
print(f"Average popularity score: {avg_popularity:.2f}")


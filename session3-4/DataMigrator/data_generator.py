import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "Diana"],
    "age": [25, 30, 35, 40],
    "salary": [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)
df.to_csv("data34.csv", index=False)


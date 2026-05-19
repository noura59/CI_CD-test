import pandas as pd

data = {
    "name": ["Ali", "Sara"],
    "age": [22, 25]
}

df = pd.DataFrame(data)

df.to_csv("output.csv", index=False)

print("CSV file created successfully")
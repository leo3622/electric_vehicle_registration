import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def fetch_data(url):
    response = requests.get(url)
    params = {"limit": 1000, "offset": 0}
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        return pd.DataFrame()
    
def save_data(df, filename, mode='w', header=True):
    df.to_csv(filename, mode=mode, header=header, index=False)
    print(f"Data saved to {filename}")

def download_and_save_data():
    for i in range(0, 10000, 1000):
        df = fetch_data(f"https://data.wa.gov/resource/f6w7-q2d2.json?$limit=1000&$offset={i}")
        save_data(df, "data/raw/electric_vehicles_data.csv", mode='a' if i > 0 else 'w', header=(i == 0))
    print("Data download complete.")

def find_outliers(df, column_name):
    column = df[column_name]
    sns.boxplot(x=column, data=df)
    plt.title(f"Boxplot of {column.name}")
    plt.show()
    
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outlier_rows = df[(column < lower_bound) | (column > upper_bound)]
    return outlier_rows
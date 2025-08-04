import requests
import pandas as pd

def fetch_data(url):
    response = requests.get(url)
    params = {"limit": 1000, "offset": 0}
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        return pd.DataFrame()
    
def save_data(df, filename):
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
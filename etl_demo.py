import pandas as pd
import requests
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
btc_data = response.json()

df = pd.DataFrame({
    "currency": ["USD"],
    "rate": [btc_data["bpi"]["USD"]["rate_float"]],
    "updated": [btc_data["time"]["updatedISO"]]
})

print("Extracted DataFrame:")
print(df)

df.to_csv("btc_rate.csv", index=False)

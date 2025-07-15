
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import pandas as pd

def extract_transform_save():
    res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = res.json()
    df = pd.DataFrame({
        "currency": ["USD"],
        "rate": [data["bpi"]["USD"]["rate_float"]],
        "updated": [data["time"]["updatedISO"]]
    })
    df.to_csv("/tmp/btc_airflow.csv", index=False)

with DAG("btc_price_pipeline", start_date=datetime(2023,1,1), schedule_interval="@hourly", catchup=False) as dag:
    task = PythonOperator(
        task_id="extract_transform_save",
        python_callable=extract_transform_save
    )

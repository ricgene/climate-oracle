import os
import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/climatetrace/search")
def climatetrace(subsectors: str, countries: str):
    url = "https://api.climatetrace.org/v4/assets"
    params = {
        "subsectors": subsectors,
        "countries": countries,
        "limit": 50
    }
    resp = requests.get(url=url, params=params)
    json_resp = resp.json()
    return json_resp


@app.get("/noaa/stations")
def noaa_stations():
    url = "https://www.ncei.noaa.gov/cdo-web/api/v2/stations"
    params = {
        "limit": 50
    }
    headers = {
        "token": os.getenv("NOAA_TOKEN")
    }
    resp = requests.get(url=url, params=params, headers=headers)
    json_resp = resp.json()
    return json_resp
import os
import requests

BASE_URL = "https://www.ncei.noaa.gov/cdo-web/api/v2"

def get_data_categories(limit=50):
    url = BASE_URL + "/datacategories"
    params = {
        "limit": limit
    }
    headers = {
        "token": os.getenv("NOAA_TOKEN")
    }
    resp = requests.get(url=url, params=params, headers=headers)
    json_resp = resp.json()
    return json_resp


def get_data_types(limit=50):
    url = BASE_URL + "/datatypes"
    params = {
        "limit": limit
    }
    headers = {
        "token": os.getenv("NOAA_TOKEN")
    }
    resp = requests.get(url=url, params=params, headers=headers)
    json_resp = resp.json()
    return json_resp


def get_locations(limit=50):
    url = BASE_URL + "/locations"
    params = {
        "limit": limit
    }
    headers = {
        "token": os.getenv("NOAA_TOKEN")
    }
    resp = requests.get(url=url, params=params, headers=headers)
    json_resp = resp.json()
    return json_resp


def get_location_categories(limit=50):
    url = BASE_URL + "/locationcategories"
    params = {
        "limit": limit
    }
    headers = {
        "token": os.getenv("NOAA_TOKEN")
    }
    resp = requests.get(url=url, params=params, headers=headers)
    json_resp = resp.json()
    return json_resp


def get_stations(limit=50):
    url = BASE_URL + "/stations"
    params = {
        "limit": limit
    }
    headers = {
        "token": os.getenv("NOAA_TOKEN")
    }
    resp = requests.get(url=url, params=params, headers=headers)
    json_resp = resp.json()
    return json_resp
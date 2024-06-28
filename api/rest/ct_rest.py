import requests

BASE_URL = "https://api.climatetrace.org/v4"


def get_assets(subsectors, country_codes, limit=50):
    url = BASE_URL + "/assets"
    params = {
        "subsectors": ",".join(subsectors),
        "countries": ",".join(country_codes)
    }
    resp = requests.get(url=url, params=params)
    json_resp = resp.json()
    return json_resp

def get_sectors(limit=50):
    url = BASE_URL + "/definitions/sectors"
    params = {
        "limit": limit
    }
    resp = requests.get(url=url, params=params)
    json_resp = resp.json()
    return json_resp


def get_subsectors(limit=50):
    url = BASE_URL + "/definitions/subsectors"
    params = {
        "limit": limit
    }
    resp = requests.get(url=url, params=params)
    json_resp = resp.json()
    return json_resp


def get_countries(limit=50):
    url = BASE_URL + "/definitions/countries"
    params = {
        "limit": limit
    }
    resp = requests.get(url=url, params=params)
    json_resp = resp.json()
    return json_resp


def get_groups(limit=50):
    url = BASE_URL + "/definitions/groups"
    params = {
        "limit": limit
    }
    resp = requests.get(url=url, params=params)
    json_resp = resp.json()
    return json_resp


def get_continents():
    url = BASE_URL + "/definitions/continents"
    resp = requests.get(url=url)
    json_resp = resp.json()
    return json_resp


def get_gases(limit=50):
    url = BASE_URL + "/definitions/gases"
    params = {
        "limit": limit
    }
    resp = requests.get(url=url, params=params)
    json_resp = resp.json()
    return json_resp
from fastapi import APIRouter

from ..rest import noaa_rest

router = APIRouter(
    prefix="/noaa",
    tags=["noaa"]
)
BASE_URL = "https://www.ncei.noaa.gov/cdo-web/api/v2"


@router.get("/datacategories")
def get_data_categories():
    return noaa_rest.get_data_categories()['results']


@router.get("/datatypes")
def get_data_types():
    return noaa_rest.get_data_categories()['results']


@router.get("/locations")
def get_locations():
    return noaa_rest.get_data_categories()['results']


@router.get("/locationcategories")
def get_location_categories():
    return noaa_rest.get_data_categories()['results']


@router.get("/stations")
def get_stations():
    return noaa_rest.get_data_categories()['results']
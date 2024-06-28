import os
import requests
from fastapi import FastAPI, APIRouter, HTTPException

from .routers import ct_router, noaa_router
from .schemas import ct_schemas
from .rest import ct_rest, noaa_rest

app = FastAPI()

router = APIRouter(
    prefix="/main",
    tags=["main"]
)

@router.post("/search")
def search_assets(search_params: ct_schemas.SearchParams):
    country_list = {c['name']: c['alpha3'] for c in ct_rest.get_countries()}
    search_countries = []
    for country in search_params.countries:
        if country not in country_list:
            raise HTTPException(status_code=404, detail=f"Country {country} not found.")
        search_countries.append(country_list[country])
    return ct_rest.get_assets(search_params.subsectors, search_countries)

app.include_router(router)
app.include_router(ct_router.router)
app.include_router(noaa_router.router)

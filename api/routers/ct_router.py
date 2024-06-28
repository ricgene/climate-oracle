from fastapi import APIRouter

from ..rest import ct_rest

router = APIRouter(
    prefix="/ct",
    tags=["ct"]
)


@router.get("/definitions/sectors")
def get_sectors():
    return ct_rest.get_sectors()


@router.get("/definitions/subsectors")
def get_subsectors():
    return ct_rest.get_subsectors()


@router.get("/definitions/countries")
def get_countries():
    return ct_rest.get_countries()


@router.get("/definitions/groups")
def get_groups():
    return ct_rest.get_groups()


@router.get("/definitions/continents")
def get_continents():
    return ct_rest.get_continents()


@router.get("/definitions/gases")
def get_gases():
    return ct_rest.get_gases()
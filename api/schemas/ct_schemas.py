from typing import List

from pydantic import BaseModel

class SearchParams(BaseModel):
    countries: List[str]
    subsectors: List[str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "countries": [
                        "China",
                        "Australia"
                    ],
                    "subsectors": [
                        "cement"
                    ]
                }
            ]
        }
    }
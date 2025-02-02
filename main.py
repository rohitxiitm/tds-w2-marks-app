from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/api")
def api(name: List[str] = Query(None)):
    # Read data from data.json file
    with open("data.json", "r") as f:
        data = json.load(f)

    # If no names are provided, return all data
    if not name:
        return data

    # Build a dictionary for O(1) lookups
    data_dict = {entry["name"]: entry for entry in data}

    # Collect results in the exact order of the query string
    results = []
    for n in name:
        if n in data_dict:
            results.append(data_dict[n]["marks"])

    return {"marks": results}

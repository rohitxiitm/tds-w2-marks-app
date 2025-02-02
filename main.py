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
def api(names: List[str] = Query(None)):
    # Read data from data.json file
    with open("data.json", "r") as f:
        data = json.load(f)

    # If no names provided, return all data
    if not names:
        return data

    # Filter data based on requested names
    filtered_data = [item for item in data if item["name"] in names]
    return filtered_data

import os
import random
import requests
import uvicorn as uvicorn
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    r_id = random.randint(1, 1000)
    r = requests.get(f"http://www.omdbapi.com/?apikey=715d7bee&t={r_id}")
    return r.json()

@app.get("/list/")
async def get_list(q: list | None = Query()):
    film_list = []
    for id in q:
        r = requests.get(f"http://www.omdbapi.com/?apikey=715d7bee&t={id}")
        film_list.append(r.json())
    return film_list

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT', 80)))
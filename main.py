from fastapi import FastAPI
from time import sleep

app = FastAPI()

@app.get("/get-amp")
async def root():
    sleep(10)
    return {"openModal": True}
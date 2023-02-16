import uvicorn
from fastapi import FastAPI
from app.mongodb import get_data

app = FastAPI()


@app.get("/users/")
async def create_user():
    return 'name'


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

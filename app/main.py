import uvicorn
from fastapi import FastAPI
from app.mongodb import get_data, get_all_data

app = FastAPI()


@app.get("/user/id/")
async def get_user(user_id: int):
    users = get_data(user_id)
    return users


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

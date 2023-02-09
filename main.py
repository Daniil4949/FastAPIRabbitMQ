import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.post("/user/")
async def create_user():
    return {"user_id": 1}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

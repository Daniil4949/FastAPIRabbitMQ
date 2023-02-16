from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo

# Replace <connection string> with your MongoDB deployment's connection string.
conn_str = "mongodb://root:password@172.20.0.2:27017"
# Set the Stable API version on the client.
client = pymongo.MongoClient(conn_str, server_api=ServerApi('1'), serverSelectionTimeoutMS=5000)

mydb = client["mydatabase"]
users = mydb["users"]


def insert_data(data: str):
    user_id: str = data.split()[0]
    user_info: str = " ".join(data.split()[1:])
    print(user_info)
    result = users.insert_one({user_id: user_info})
    return result


def get_data(id: int):
    result = []
    for element in users.find({}, {"user_id": str(id)}):
            result.append(element)
    return result


# get_data(6)



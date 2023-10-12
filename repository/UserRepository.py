import requests
import json
from model.User import User

def getUser(userId:str):
    url = f"http://localhost:8080/api/v1/user/{userId}"
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    loads = response.json()
    print(loads)
    user = User(**loads)
    print(user.id)
    print(user.firstname)
    print(user.lastname)
    # и тд
    return user

print(getUser("5367"))
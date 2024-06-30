import requests
from credential import *

header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": input("What did you do today??"),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    'age': AGE
}

auth = ("Aditya", "Adity@2004")

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=params, headers=header)
response.raise_for_status()

data = response.json()

for exercise in data["exercises"]:
    new_row = {
        "workout": {
            "date": TODAY.strftime("%d/%m/%Y"),
            "time": TODAY.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response = requests.post(url="https://api.sheety.co/a3bebf278066f5d7ef338ae0fbbe25e7/workoutTracker/workouts",
                             json=new_row,
                             auth=auth)
    print(response.text)
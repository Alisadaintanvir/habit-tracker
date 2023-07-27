import os

import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Creating User
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = os.environ.get("user_name")
TOKEN = os.environ.get("TOKEN")
pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)


# Creating Graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Jogging Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}


headers = {
    "X-USER-TOKEN": TOKEN
}
# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)

# Get current date
today = datetime.now()

# Posting Pixel
pixel_post_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_params['id']}"
# pixel_post_params = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": input("How many kilometers did you run? : ")
# }

# pixel_post_response = requests.post(url=pixel_post_endpoint, json=pixel_post_params, headers=headers)
# print(pixel_post_response.text)

# Update a pixel
# pixel_update_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_params['id']}/{pixel_post_params['date']}"
# pixel_update_params = {
#     "quantity": input("Update value: ")
# }
#
# update_response = requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=headers)
# print(update_response.text)


# Delete a pixel
# delete_response = requests.delete(url=pixel_post_endpoint, headers=headers)
# print(delete_response.text)

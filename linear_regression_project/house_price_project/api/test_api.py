import requests

url = "http://127.0.0.1:8000/predict"
data = {
    "area": 3500,
    "bedrooms": 5,
    "age": 6,
    "distance": 6
}
print("Sending request to API...")
response = requests.post(url, json=data)
print(response.json())
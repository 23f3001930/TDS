import requests

url = "https://tds-2o06e4962-23f3001930.vercel.app/query"

response = requests.post(url, json={
    "question": "What is the purpose of pandas pivot_table?",
    "image": None
})

print(response.json())

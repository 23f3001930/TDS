import requests

response = requests.post("https://tds-mkg513boq-23f3001930.vercel.app/query", json={
    "question": "What is the purpose of pandas pivot_table?",
    "image": None
})

print(response.status_code)
print(response.json())

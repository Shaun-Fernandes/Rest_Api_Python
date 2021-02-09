import requests
import pandas as pd

genders = [{"gender": 1}, {"gender": 2}]
responses = []

for gender in genders:
    responses.append(requests.post("https://b80c869c8234.ngrok.io/GetFullName", json=gender))

data = []
for resp in responses:
    if resp.status_code != 200:
        print(f"Error in post requests {resp.status_code}")
        exit()
    data.append(resp.json())

df = pd.DataFrame(data)
df.to_csv("responses.csv", index=False)

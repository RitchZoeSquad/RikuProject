import requests
import json

url = "https://prompts.riku.ai/webhook/run"

payload = json.dumps({
  "Name": ">",
  "Secret": ">",
  "Prompt ID": "1648599202269x693769025531412500",
  "Input 1": "Create Python Program to scrape zoesquad.me using requests",
  "n": 4
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

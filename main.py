import json
import os

import requests
import time

channel = "channel id"

base = f"https://discord.com"

route = f"/api/v9/channels/{channel}/messages?limit=100"

# for best use copy your headers
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    "Authorization": "your token",
    "cookie": "your cookie",
    "priority": "u=1, i",
    "referer": "https://discord.com/channels/category/randomchannel", # replace category with any category id of the server and randomchannel with any channel
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "your useragent",
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "de",
    "x-super-properties": "copy from own request",
    "x-discord-timezone": "copy from request"
}


last = ""

i = 0

file_name = "file-name"

if os.path.exists(f'{file_name}.json'):
    with open(f'{file_name}.json', 'r') as file:
        loaded = json.load(file)
        if isinstance(loaded, list):
            messages = loaded
        else:
            messages = [loaded]
else:
    messages = []

count = 0

while True:
    url = base + route + (f"&before={last}" if i != 0 else "")
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        data = r.json()
        # Stop if no more data is returned
        count += len(data)
        if not data:
            print(f"No more messages to fetch. {r.status_code}")
            break

        # Check if data is a list; otherwise handle it as a single dictionary
        if isinstance(data, list):
            messages.extend(data)
            # Update 'last' only if data is a non-empty list
            last = data[-1]["id"]
        elif isinstance(data, dict):
            messages.append(data)
            # If the API unexpectedly returns a dict, we break out of the loop
            print("Received a single message as a dict; stopping further requests.")
            break
        else:
            print("Unexpected data format, stopping the loop.")
            break

        with open(f'{file_name}.json', 'w') as file:
            json.dump(messages, file, indent=4)

        i += 1
        print(f"{url} | Done | {r.status_code} | {count}")
        time.sleep(1)
    else:
        print(f"Error: {r.status_code}")
        break

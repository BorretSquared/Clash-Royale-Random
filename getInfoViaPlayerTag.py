import sys
import io
import requests
import json
from randomPlayerTags import loadApiKey  # Import the loadApiKey function

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def apiRequest(key, url):
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {key}',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None    

def getPlayerInfo(key, playerTag):
    url = f"https://api.clashroyale.com/v1/players/%23{playerTag}"
    return apiRequest(key, url) 

key = loadApiKey()  # Load the API key using the imported function

try:
    with open('data/playerInfo.txt', 'r') as infoFile:
        lastLine = sum(1 for line in infoFile)
except FileNotFoundError:
    lastLine = 0

with open('data/playerTags.txt') as file:
    for i, line in enumerate(file):
        if i < lastLine:
            continue
        line = line.strip()  # remove leading/trailing whitespace
        if line:  # check if line is not empty
            playerInfo = getPlayerInfo(key, line)
            if playerInfo:
                with open('data/playerInfo.txt', 'a') as info:  # Open the file in append mode
                    if info.tell() != 0:
                        info.write("\n")
                    info.write(str(playerInfo['trophies']) + " " + str(playerInfo['expLevel']) + " " + playerInfo['tag'][1:])  # 8099 45 CR29LVQJU


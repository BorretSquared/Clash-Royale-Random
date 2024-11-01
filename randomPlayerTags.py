import requests
import json

def loadApiKey():
    # Load the API key from config.json.
    with open('config.json', 'r') as f:
        return json.load(f)['apiKey']

def loadRandomLimit():
    # Load the random limit from config.json.
    with open('config.json', 'r') as f:
        limit = json.load(f)['randomLimit']
        return int(limit) if limit is not None else None

def apiRequest(key, url):
    # Make an API request and return the JSON response.
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {key}',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None   

def getApiData(key, urlTemplate, tag):
    # Get data from the API using the given URL template and tag.
    url = urlTemplate.format(tag=tag)
    return apiRequest(key, url)

# Lambda functions to get player info, battle log, and clan members
getPlayerInfo = lambda key, tag: getApiData(key, "https://api.clashroyale.com/v1/players/%23{tag}", tag)
getBattleLog = lambda key, tag: getApiData(key, "https://api.clashroyale.com/v1/players/%23{tag}/battlelog", tag)
getClanMembers = lambda key, tag: getApiData(key, "https://api.clashroyale.com/v1/clans/%23{tag}/members", tag)

def getPlayersViaOneTag(key, tag, playerTags, randomLimit):
    # Get a list of random players from the battle log of a given tag, adhering to the random limit.
    battleLog = getBattleLog(key, tag)
    if battleLog:
        # Save battle log to a file
        with open('data/battleLog.json', "w") as textFile:
            json.dump(battleLog, textFile)
            for battle in battleLog:
                if randomLimit is not None and len(playerTags) >= randomLimit:
                    break
                for opponent in battle['opponent']:
                    opponentTag = opponent['tag'][1:]
                    if opponentTag not in playerTags:
                        playerTags.add(opponentTag)
                        if 'clan' in opponent:
                            clanTag = opponent['clan']['tag'][1:]
                            getClanMembersAndAddTags(key, clanTag, playerTags, randomLimit)
                        if randomLimit is not None and len(playerTags) >= randomLimit:
                            break

def getClanMembersAndAddTags(key, clanTag, playerTags, randomLimit):
    # Get clan members and add their tags to the playerTags set up to the random limit.
    clanMembersResponse = getClanMembers(key, clanTag)
    if clanMembersResponse:
        for item in clanMembersResponse['items']:
            memberTag = item['tag'][1:]
            if randomLimit is not None and len(playerTags) >= randomLimit:
                break
            playerTags.add(memberTag)

if __name__ == '__main__': # only run if main file
    # Load API key and random limit from config
    key = loadApiKey()
    randomLimit = loadRandomLimit()
    playerTags = set()

    # Read base player tags from file and get players via their tags
    with open('basePlayers.txt') as file:
        for line in file:
            line = line.strip()
            if line:
                getPlayersViaOneTag(key, line, playerTags, randomLimit)
                if randomLimit is not None and len(playerTags) >= randomLimit:
                    break

    # Write collected player tags to file
    with open('data/playerTags.txt', 'w') as tags:
        for tag in playerTags:
            tags.write(tag + '\n')

# Clash-Royale-Random
A Python Program Which Utilizes the Clash Royale API to Aquire Sudo Random Players + An Example Data Graph w/ Data Usage

## Pre-requisites
An API key from https://developer.clashroyale.com/, put this in the config.json
Install required libraries via 
```pip install -r requirements.txt```

## Usage
1. The randomLimit in config.json can be set to none for the program to be run indefinitely, or use any given number
2. In the basePlayers.txt file, ensure that you have 1-20 players acquired from the games' built in TV Royale feature, players included are a template and aren't recommended to be used.
3. Run ```randomPlayerTags.py```, tags will be dumped at ```data\playerTags.txt```

## Additional Programs
The ```getInfoViaTag.py``` file can be run seperately to get a player's trophies, levels, and tag (in order). This will take longer to run.

The ```scatterPlot.py``` file can be run to use the Info in a graph
![Graph](https://github.com/BorretSquared/Clash-Royale-Random/blob/main/ExampleGraph.png)


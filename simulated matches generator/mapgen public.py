import os, ezsheets, random

os.chdir('path goes here')

reachMaps = {'1': 'Anchor 9', '2': 'Boardwalk', '3': 'Boneyard', '4': 'Breakpoint', '5': 'Condemned', '6': 'Countdown', '7': 'Forge World', '8': 'Highlands', '9': 'Powerhouse', '10': 'Reflection', '11': 'Spire', '12': 'Sword Base', '13': 'Tempest', '14': 'Zealot'}

ss = ezsheets.Spreadsheet('url here')

print(ss.title)

sheet = ss[0]

for i in range(3, 1000): # Random map generation
    mapValue = random.randint(1, 14)
    sheet[3, i] = str(reachMaps[str(mapValue)])

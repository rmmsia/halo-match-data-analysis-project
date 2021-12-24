import os, ezsheets, random, timeit

startTime = timeit.default_timer()

os.chdir('path here')

ss = ezsheets.Spreadsheet('url here')

print(f'Now editing {ss.title}')

sheet = ss[0]

# Dictionaries
winorloss = {'1': 'Loss', '2': 'Win'}
wlHK = {'1': 'Loss', '2': 'Win', '3': 'Win', '4': 'Win'}
wlLK = {'1': 'Loss', '2': 'Loss', '3': 'Loss', '4': 'Win'}


# Match death generation
for rowNum in range(3, 102):
    deaths = int(random.randint(3, 20))
    sheet[7, rowNum] = deaths
print('Match Deaths generation done.')


# DMR Kills generation
for rowNum in range(3, 102):
    dmrKills = int(random.randint(5, 15))
    sheet[8, rowNum] = dmrKills
print('DMR Kills generation done.')

# Sniper Kills generation
for rowNum in range(3, 102):
    sniperKills = int(random.randint(0, 10))
    sheet[9, rowNum] = sniperKills
print('Sniper Kills generation done.')

# Pistol Kills generation
for rowNum in range(3, 102):
    pistolKills = int(random.randint(0, 12))
    sheet[10, rowNum] = pistolKills
print('Pistol Kills generation done.')

# Grenade Launcher Kills generation
for rowNum in range(3, 102):
    GLKills = int(random.randint(0, 5))
    sheet[11, rowNum] = GLKills
print('Grenade Launcher Kills generation done.')

# Melee Kills generation
for rowNum in range(3, 102):
    meleeKills = int(random.randint(0, 10))
    sheet[12, rowNum] = meleeKills
print('Melee Kills generation done.')


# Check if totalKills exceeds 50
for rowNum in range(3, 102):
    if int(sheet[6, rowNum]) > 50:
        while True:
            dmrKills = int(random.randint(5, 15))
            sniperKills = int(random.randint(0, 10))
            pistolKills = int(random.randint(0, 12))
            GLKills = int(random.randint(0, 5))
            meleeKills = int(random.randint(0, 10))
            sheet[8, rowNum] = dmrKills
            sheet[9, rowNum] = sniperKills
            sheet[10, rowNum] = pistolKills
            sheet[11, rowNum] = GLKills
            sheet[12, rowNum] = meleeKills
            if sheet[6, rowNum] > 50:
                continue
            else:
                break
    else:
        print(f'{rowNum} okay!')

# Win / loss generation
for rowNum in range(3, 102):
    if int(sheet[6, rowNum]) > 25:
        wl = random.randint(1, 4)
        sheet[5, rowNum] = str(wlHK[str(wl)])

    if int(sheet[6, rowNum]) < 10:
        wl = random.randint(1, 4)
        sheet[5, rowNum] = str(wlLK[str(wl)])

    else:
        wl = random.randint(1, 2)
        sheet[5, rowNum] = str(winorloss[str(wl)])

print()
print('Data generation complete!')

stop = timeit.default_timer()
print('Time taken: ', stop - start)

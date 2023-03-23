from itertools import islice
import json

f = open("raw.json")
caves = json.load(f)

caves2 = [caves[x:x+12] for x in range(0, len(caves), 12)]

caves3 = []
for cave in caves2:
    cave.append(cave.pop(0))
    cave.pop(0)
    caves3.append(cave)

# with open('clean.json', 'w') as f:
#     json.dump(caves3, f)

for cave in caves3:
    print(cave)

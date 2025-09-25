import json
s = "now we is back to the long ass string that we had chosen at the start of this code"

d ={}

for ch in s:
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1

print(json.dumps(d, indent = 3))
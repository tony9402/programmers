import os
import sys

for level in range(1, 6): # 1 ~ 5
    folder  = f"LEVEL{level}"
    data    = list()
    newData = list()
    with open(f"./{folder}/list.md", 'r') as f:
        data = f.readlines()
        data = [ curdata.strip() for curdata in data ]
        f.close()

    newData.append(data[0])
    data = data[1:]

    for info in data:
        ID = info.split('$')[2]

        if os.path.exists(f'./solution/{folder}/{ID}/'):
            newData.append(f"{info}[바로가기](../solution/{folder}/{ID})")
        else:
            newData.append(info)

    with open(f"./{folder}/list.md", 'w') as f:
        newData = [ f"{line}\n" for line in newData ]
        f.writelines(newData)
        f.close()

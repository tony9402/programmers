import os
import sys

# README.md
#
# header.md
# list.md -> make_table
# footer.md

headers = list()
footers = list()
tables  = list()
with open('./markdown/header.md', 'r') as f:
    headers = f.readlines()
    f.close()

with open('./markdown/footer.md', 'r') as f:
    footers = f.readlines()
    f.close()

with open('./markdown/list.md', 'r') as f:
    data = f.readlines()
    f.close()

tableHeader = data[0].strip().split(',')
tables.append(f"| {' | '.join(tableHeader)} |")
tables.append(f"| {':--: |' * len(tableHeader)}")
for idx in range(1, len(data)):
    level, status = data[idx].strip().split(',')

    # len(problems)
    problems  = list()
    recommend = list()
    with open(f"{level}/list.md", 'r') as f:
        problems = f.readlines()[1:]
        recommend = [ True for data in problems if data.strip().split("$")[0] != '' ]
        f.close()

    line = f"| {level} | [바로 가기](./{level}) | {len(recommend)} | {len(problems)} | ![status][{status}] |"
    tables.append(line)

tables = [ f"{line}\n" for line in tables ]

# README.md

import datetime
import pytz

timeformat = datetime.datetime.now(pytz.timezone('Asia/Seoul'))

with open('./README.md', 'w') as f:
    f.writelines(headers)
    f.write('\n')
    
    # table
    f.writelines(tables)
    f.write(f"\n\n**실행한 날짜(log) : {timeformat.strftime('%Y/%m/%d %H:%M:%S %Z')}**")

    f.write('\n')
    f.writelines(footers)
    f.close()

import os
import subprocess as sb
import sys

""" MEMO
[recommend],[title],[link(url)],[tier(SolvedAC)],[algorithm tags]
[recommend] -> [0 if not recommend else anything]
[title] -> [ 입국심사 ]
[link(url)] -> [https://programmers.co.kr/learn/courses/30/lessons/43238]
[tier(SolvedAC)] -> 14
[algorithm tags] -> [ 이분탐색 ]

# example
1$"입국심사"$43238$$[]
"""

# default
LEVEL = list(range(1, 6))
TABLE_HEADER = [ "순번" ,"추천 문제", "문제 이름", "솔브드 티어", "알고리즘 태그", "풀이 링크" ]

def SolvedACTier(tier):
    url = f"https://static.solved.ac/tier_small/{tier}.svg"
    return f"<img height=\"25px\" width=\"25px\" src=\"{url}\"/>"

# README list.md and make table (markdown)
for level in LEVEL:
    currentFolder = f"LEVEL{level}"
    
    listFile = f"{currentFolder}/list.md"
    headerFile = f"{currentFolder}/header.md"
    READMEFile = f"{currentFolder}/README.md"

    if not os.path.exists(listFile) or not os.path.exists(headerFile):
        continue


    datas = None
    with open(listFile, 'r') as f:
        # except line 1
        datas = [ line.strip() for line in f.readlines()[1:] if len(line.strip()) ]
        f.close()
    
    # Parsing
    recommendProblems = [  ]
    otherProblems     = [  ]
    for data in datas:
        recommend, title, link, tier, tags, solution = data.strip().split('$')
        assert title[0]  == '"'
        assert title[-1] == '"'
        assert link      != ''
        assert tags[0]   == '['
        assert tags[-1]  == ']'

        recommendB = False
        if recommend != '':
            recommendB = True
            recommend = ":heavy_check_mark:"

        if tier.strip() == "":
            tier = '0' # unrated

        title = title[1:-1]
        link  = f"https://programmers.co.kr/learn/courses/30/lessons/{link}"

        if 0 <= int(tier) <= 30: # 
            tier = SolvedACTier(tier)
        else:
            assert False, f"Tier ERROR (tier : {tier})"
        
        # Hmm..
        ###  TODO  ###
        tags = tags[1:-1]
        if tags != "":
            tags = tags.strip().split(',')
            tags = ",".join([ tag.strip() for tag in tags ])

        resultLine = f"|{recommend}|[{title}]({link})|{tier}|{tags}|{solution}|"
        if recommendB:
            recommendProblems.append(resultLine)
        else:
            otherProblems.append(resultLine)

    # Make Table (type == list)
    tables = [ f"| {'|'.join(TABLE_HEADER)} |" ]
    tables.append(f"| {':--:|' * len(TABLE_HEADER)}")

    index = 0
    for recProblem in recommendProblems:
        tables.append(f"| {index:02d} {recProblem}")
        index += 1
    for othProblem in otherProblems:
        tables.append(f"| {index:02d} {othProblem}")
        index += 1

    # README.md < header.md and README.md << "TABLES"
    headers = list()
    with open(f"{headerFile}", 'r') as f:
        headers = f.readlines()
        f.close()

    with open(f"{READMEFile}", 'w') as f:
        f.writelines(headers)
        tables = [ f"{currentLine}\n" for currentLine in tables ]
        f.write("\n")
        f.writelines(tables)
        f.close()

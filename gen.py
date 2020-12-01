#!/usr/bin/python3

import requests
import sys
from datetime import datetime

def generate(contestId, abbrev, shortName):
    url = f'https://codeforces.com/api/contest.standings?contestId={contestId}&from=1&count=1&showUnofficial=false'
    print(f'Fetching: {url}')
    r = requests.get(url)
    data = r.json()['result']
    title = data['contest']['name']
    start = datetime.fromtimestamp(data['contest']['startTimeSeconds'])
    print(f'Contest: <{title}>')

    f = open(f'_posts/{start.strftime("%Y-%m-%d")}-{abbrev}.md', 'a')
    print('---', file=f)
    print(f'title: {shortName}', file=f)
    print('---', file=f)
    print('', file=f)
    print(f'[{title}](https://codeforces.com/contest/{contestId})', file=f)
    print(file=f)
    print('* * *', file=f)

    for problem in data['problems']:
        index = problem['index']
        name = problem['name']
        print(f"{{% include p/{contestId}{index}.md %}}", file=f)
        print('* * *', file=f)

        p = open(f'_includes/p/{contestId}{index}.md', 'a')
        print(f'# **{contestId}{index}** [{name}](https://codeforces.com/contest/{contestId}/problem/{index})', file=p)
        print(file=p)
        tags = ' '.join(['`' + tag + '`' for tag in problem['tags']])
        print(f'[//]: # 🏷 {tags}', file=p)
        print(file=p)
        print('TODO', file=p)
        p.close()

    print('', file=f)
    print(f"<object data='notes/{abbrev}.pdf' width='1000' height='1000' type='application/pdf'/>", file=f)
    f.close()

def main():
    if len(sys.argv) != 4:
        print(f'Usage: {sys.argv[0]} <CONTEST_ID> <ABBREV> <SHORT_NAME>')
        exit(0)
    contestId = sys.argv[1]
    abbrev = sys.argv[2]
    shortName = sys.argv[3]
    print(f'Loading contest {contestId} (abbrev: {abbrev}, short name: {shortName})')
    generate(contestId, abbrev, shortName)

if __name__ == "__main__":
    main()

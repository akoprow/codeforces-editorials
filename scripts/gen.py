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

    with open('scripts/genall.sh', 'a') as f:
        print(f'./gen.py {contestId} {abbrev} "{shortName}"', file=f)

    with open(f'_posts/{start.strftime("%Y-%m-%d")}-{abbrev}.md', 'a') as f:
        print('---', file=f)
        print(f'title: {shortName}', file=f)
        print('---', file=f)
        print('', file=f)
        print(f'[{title}](https://codeforces.com/contest/{contestId})', file=f)
        print(file=f)

        for problem in data['problems']:
            index = problem['index']
            name = problem['name']
            tags = ', '.join(problem['tags'])
            rating = problem.get('rating', None)
            fn = f'p/{contestId[0:3]}/{contestId}{index}.md'
            print(f"{{% include {fn} %}}", file=f)

            with open(f'_includes/{fn}', 'a') as p:
                ratingArg = f'rating={rating}' if rating else ''
                print(f'{{% include exercise.md name="{name}" id="{contestId}{index}" labels="{tags}" {ratingArg} %}}', file=p)
                print(file=p)
                print(f'```', file=p)
                print(f'TODO', file=p)
                print(f'```', file=p)

        print(file=f)
        print('* * *', file=f)
        print(file=f)
        print(f"<object data='notes/{abbrev}.pdf' width='1000' height='1000' type='application/pdf'/>", file=f)

    with open('_data/problems.yaml', 'a') as f:
        for problem in data['problems']:
            index = problem['index']
            name = problem['name']
            labels = ', '.join(problem['tags'])
            rating = problem.get('rating', None)

            print(f"- id: '{contestId}{index}'", file=f)
            print(f"  title: '{name}'", file=f)
            print(f"  labels: '{labels}'", file=f)
            if rating:
                print(f"  rating: '{rating}'", file=f)
            print(file=f)


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

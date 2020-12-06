#!/usr/bin/python3

import requests
import sys

def generate(contestId):
    url = f'https://codeforces.com/api/contest.standings?contestId={contestId}&from=1&count=1&showUnofficial=false'
    print(f'Fetching: {url}')
    r = requests.get(url)
    data = r.json()['result']
    title = data['contest']['name']
    print(f'Contest: <{title}>')

    for problem in data['problems']:
        index = problem['index']
        name = problem['name']
        tags = ' '.join(['`' + tag + '`' for tag in problem['tags']])
        rating = problem.get('rating', None)

        p = open(f'_includes/p/{contestId[0:3]}/{contestId}{index}.md', 'a')
        print(f'rating={rating}', file=p)
        p.close()


def main():
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <CONTEST_ID>')
        exit(0)
    contestId = sys.argv[1]
    print(f'Loading contest {contestId}')
    generate(contestId)

if __name__ == "__main__":
    main()

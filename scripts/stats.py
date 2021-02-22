#!/usr/bin/python3

import requests
import sys
from collections import defaultdict
from datetime import datetime

def generate(label):
    url = f'https://codeforces.com/api/contest.list'
    r = requests.get(url)
    contests = r.json()['result']
    contestYear = {}
    for contest in contests:
        year = datetime.fromtimestamp(contest['startTimeSeconds']).year
        contestYear[contest['id']] = year

    url = f'https://codeforces.com/api/problemset.problems'
    r = requests.get(url)
    data = r.json()['result']['problems']

    yearAll = defaultdict(int)
    yearLabel = defaultdict(int)
    ratingAll = defaultdict(int)
    ratingLabel = defaultdict(int)

    for problem in data:
        year = contestYear[problem['contestId']]
        yearAll[year] += 1
        if label in problem['tags']:
            yearLabel[year] += 1
        if 'rating' in problem:
            rating = problem['rating']
            ratingAll[rating] += 1
            if label in problem['tags']:
                ratingLabel[rating] += 1

    print('By rating')
    for rating in sorted(ratingAll):
        print(f'{rating},{ratingAll[rating]},{ratingLabel[rating]}')

    print('By year')
    for year in sorted(yearAll):
        print(f'{year},{yearAll[year]},{yearLabel[year]}')


def main():
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <LABEL>')
        exit(0)
    label = sys.argv[1]
    generate(label)

if __name__ == "__main__":
    main()

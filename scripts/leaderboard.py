#!/usr/bin/python3

import requests
import sys
from collections import defaultdict
from datetime import datetime
from tqdm import tqdm

def main():
    url = f'https://codeforces.com/api/user.ratedList'
    r = requests.get(url)
    users = r.json()['result']

    print('handle,rating,country,city,solved')
    for user in tqdm(users):
        handle = user['handle']
        rating = user['rating']
        country = user['country'] if 'country' in user else ''
        city = user['city'] if 'city' in user else ''

        url = f'https://codeforces.com/api/user.status?handle={handle}'
        r = requests.get(url)
        submissions = r.json()['result']
        def id(submission):
            problem = submission['problem']
            problem['name'] + str(problem['contestId']) if 'contestId' in problem else ''
        solved = [ id(submission) for submission in submissions if submission['verdict'] == 'OK']
        solvedNum = len(set(solved))

        print(f"{handle}, {rating}, {country}, {city}, {solvedNum}")


if __name__ == "__main__":
    main()

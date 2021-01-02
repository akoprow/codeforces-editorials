#!/usr/bin/python3

from pathlib import Path
from tqdm import tqdm

def show(label, exercises):
    if exercises:
        missing = ''.join(['\n  -' + str(m) for m in exercises])
        print(f'\n{label}:{missing}')


def main():
    missingEditorials = []
    missingRatings = []
    missingCode = []

    for path in tqdm(sorted(Path('_includes/p').rglob('*.md'))):
        with open(path, 'rt') as f:
            content = f.readlines()
            hasRating = 'rating=' in content[0]
            hasCode = 'code=' in content[0]
            hasTutorial = all(['TODO' not in line for line in content])
            print(f'{path} rating:{hasRating} code:{hasCode} tutorial:{hasTutorial}')
            if hasTutorial and not hasCode:
                missingCode.append(path)
            if hasCode and not hasTutorial:
                missingEditorials.append(path)
            if not hasRating:
                missingRatings.append(path)

    show('Missing editorials', missingEditorials)
    show('Missing ratings', missingRatings)
    show('Missing code', missingCode)

if __name__ == "__main__":
    main()

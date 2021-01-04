#!/usr/bin/python3

import re
from pathlib import Path
from tqdm import tqdm

def main():
    for path in tqdm(sorted(Path('_includes/p').rglob('*.md'))):
        with open(path, 'rt') as f:
            ex = f.readlines()[0]
            id = re.search(r"_includes/p/\d+/(.+)\.md", str(path))
            if not id:
                raise Exception(f'Unknown id for file: {path}')
            name = re.search(r'name="([^"]+)"', ex)
            if not name:
                raise Exception(f'Unknown name in: {ex}')
            rating = re.search(r'rating=(\d+)', ex)
            labels = re.search(r'labels="([^"]+)"', ex)
            if not labels:
                raise Exception(f'Unknown labels in: {ex}')
            code = re.search(r'code="([^"]+)"', ex)

            print(f"- id: '{id.group(1)}'")
            print(f"  title: '{name.group(1)}'")
            print(f"  labels: '{labels.group(1)}'")
            if rating:
                print(f'  rating: {rating.group(1)}')
            if code:
                print(f"  code: '{code.group(1)}'")
            else:
                print(f'  todo: true')
            print()


if __name__ == "__main__":
    main()

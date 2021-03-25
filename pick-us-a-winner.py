import json
import sys
import random

draft_file_name = sys.argv[1]

print(f'Executing raffle for event: {draft_file_name}')

with open(draft_file_name) as json_file:
    data = json.load(json_file)
    entry = data['entries']
    random.shuffle(entry)
    random.shuffle(entry)
    random.shuffle(entry)
    print('And the winner is:')
    print(entry[0])

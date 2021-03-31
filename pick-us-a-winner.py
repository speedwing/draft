import json
import sys
import random

draft_file_name = sys.argv[1]

print(f'Executing raffle for event: {draft_file_name}')

with open(draft_file_name) as json_file:
    data = json.load(json_file)
    entries = data['entries']
    random.shuffle(entries)
    random.shuffle(entries)
    random.shuffle(entries)
    print('And the winner is:')
    print(entries[0])
    print('\n\n\n')
    print('Fallback:')
    for entry in entries[1:]:
        print(entry)
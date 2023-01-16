#!/usr/bin/env python3
'''
This hook prevents files with the same name but different capitalization
from being added to the repo.  Such files cause headaches for Mac users
because Mac file names are case insensitive.
'''
import os
import sys
from collections import defaultdict


fnames = defaultdict(list)
exclude = ['.git']

for path, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in exclude]

    for name in files:
        name = os.path.join(path, name)
        fnames[str.lower(name)].append(name)

    for dirname in dirs:
        name = os.path.join(path, dirname)
        fnames[str.lower(name)].append(name)

all_dupes = []
for k, v in fnames.items():
    if len(v) > 1:
        all_dupes.append(v)

if len(all_dupes) > 0:
    print('git commit was rejected by course policy. Please see below:\n')
    print('Files cannot have the same case-insensitive name.')
    print(('There is more than file in your repository with these names '
           'varying only in capitalization:'))
    for dupe in all_dupes:
        print('')
        for item in dupe:
            print(item)
    print('\nPlease rename at least one variant of the files listed above.')
    sys.exit(1)

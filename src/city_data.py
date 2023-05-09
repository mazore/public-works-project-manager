import os.path
import sys

if getattr(sys, 'frozen', False):
    path = os.path.join(sys._MEIPASS, 'files/city_ids.csv')
else:
    path = 'files/city_ids.csv'

print('loading city data')
CITY_ID_NAME_MAP = {}
is_header = True
for line in open(path):
    if is_header:
        is_header = False
        continue
    id, name = line.strip('\n').split(',', 1)
    CITY_ID_NAME_MAP[id] = name

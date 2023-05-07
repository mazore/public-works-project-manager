print('loading city data')
CITY_ID_NAME_MAP = {}
is_header = True
for line in open('city_ids.csv'):
    if is_header:
        is_header = False
        continue
    id, name = line.strip('\n').split(',', 1)
    CITY_ID_NAME_MAP[id] = name

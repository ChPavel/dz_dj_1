import json
import csv

ADS = 'ads'
CATEGORIES = 'categories'
LOCATIONS = 'locations'
USERS = 'users'


def convjson(csv_file, json_file, model):
    result = []
    with open(csv_file, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            to_add = {'model': model, 'pk': int(row['Id'] if 'Id' in row else row['id'])}
            if 'id' in row:
                del row['id']
            else:
                del row['Id']

            if 'location_id' in row:
                row['location'] = [int(row['location_id'])]
                del row['location_id']

            if 'is_published' in row:
                if row['is_published'] == 'TRUE':
                    row['is_published'] = True
                else:
                    row['is_published'] = False

            if 'price' in row:
                row['price'] = int(row['price'])

            to_add['fields'] = row
            result.append(to_add)

    with open(json_file, 'w', encoding="utf-8") as f:
        f.write(json.dumps(result, ensure_ascii=False))


convjson(f"{ADS}.csv", f"{ADS}.json", 'ads.ad')
convjson(f"{CATEGORIES}.csv", f"{CATEGORIES}.json", 'ads.category')
convjson(f"{LOCATIONS}.csv", f"{LOCATIONS}.json", 'users.location')
convjson(f"{USERS}.csv", f"{USERS}.json", 'users.user') # users.user т.е. название апа.название файла

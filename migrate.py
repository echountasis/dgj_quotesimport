import csv
import requests


URL = "https://10au8vx47a.execute-api.us-east-2.amazonaws.com/prod/quote"

with open('quotes4.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            line_count += 1

            PARAMS = {
                "dayOfYear": int(row[1]),
                "year": int(row[4]),
                "quote": row[2],
                "author": row[3]
            }

            r = requests.post(url=URL, json=PARAMS)
            print(line_count, r)

    print(f'Processed {line_count} lines.')

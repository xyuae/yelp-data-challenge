import csv
import json

column_names = ['review_id', 'user_id', 'business_id', 'stars', 'date', 'text', 'useful', 'funny', 'cool', 'type']

def get_row(line_contents, column_names):           

    """Return a csv compatible row given column names and a dict."""

    row = []

    for column_name in column_names:

        line_value = line_contents[column_name]

        if isinstance(line_value, unicode):

            row.append('{0}'.format(line_value.encode('utf-8')))

        elif line_value is not None:

            row.append('{0}'.format(line_value))

        else:

            row.append('')

    return row

with open('review.csv', 'wb+') as fout:
	csv_file = csv.writer(fout)
	csv_file.writerow(column_names)
	count = 0
	with open('yelp_academic_dataset_review.json') as fin:
		for line in fin:
			line_contents = json.loads(line)
			count = count + 1
			csv_file.writerow(get_row(line_contents, column_names))
	print(count)
	

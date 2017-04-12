import csv
import json

column_names = ['user_id', 'name', 'review_count', 'useful', 'funny', 'cool', 'fans', 'average_stars','compliment_hot', 'compliment_more', 'compliment_profile', 'compliment_cute', 'compliment_list', 'compliment_note', 'compliment_plain', 'compliment_cool', 'compliment_funny', 'compliment_writer', 'compliment_photos', 'type']
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

with open('user_general.csv', 'wb+') as fout:
	csv_file = csv.writer(fout)
	csv_file.writerow(column_names)
	count = 0
	with open('yelp_academic_dataset_user.json') as fin:
		for line in fin:
			line_contents = json.loads(line)
			count = count + 1
			csv_file.writerow(get_row(line_contents, column_names))
	print(count)
	

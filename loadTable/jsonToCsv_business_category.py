import csv
import json

with open('user_business_categories.csv', 'wb+') as fout:
	csv_file = csv.writer(fout)
	csv_file.writerow(['business_id', 'categories'])
	count = 0
	with open('yelp_academic_dataset_business.json') as fin:
		for line in fin:
			line_contents = json.loads(line)
			business_id = line_contents['business_id']
			categories = line_contents['categories']
			if categories is None: continue
			for item in categories:
				csv_file.writerow([business_id, item])
				count = count + 1
		print(count)

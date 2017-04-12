import csv
import json

with open('user_business_attribute.csv', 'wb+') as fout:
	csv_file = csv.writer(fout)
	csv_file.writerow(['business_id', 'attributes'])
	count = 0
	with open('yelp_academic_dataset_business.json') as fin:
		for line in fin:
			line_contents = json.loads(line)
			business_id = line_contents['business_id']
			attributes = line_contents['attributes']
			if attributes is None: continue
			for attribute in attributes:
				csv_file.writerow([business_id, attribute])
				count = count + 1
		print(count)

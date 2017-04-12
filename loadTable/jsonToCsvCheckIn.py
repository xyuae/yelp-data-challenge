import csv
import json

with open('checkin.csv', 'wb+') as fout:
	csv_file = csv.writer(fout)
	csv_file.writerow(['business_id', 'time', 'type'])
	count = 0
	with open('yelp_academic_dataset_checkin.json') as fin:
		for line in fin:
			line_contents = json.loads(line)
			business_id = line_contents['business_id']
			times = line_contents['time']
			type = line_contents['type']
			for time in times:
				csv_file.writerow([business_id, time, type])
				count = count + 1
		print(count)

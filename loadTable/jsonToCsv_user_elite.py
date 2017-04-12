import csv
import json

with open('user_elite.csv', 'wb+') as fout:
	csv_file = csv.writer(fout)
	csv_file.writerow(['user_id', 'elite'])
	count = 0
	with open('yelp_academic_dataset_user.json') as fin:
		for line in fin:
			line_contents = json.loads(line)
			user_id = line_contents['user_id']
			elites = line_contents['elite']
			for elite in elites:
				csv_file.writerow([user_id, elite])
				count = count + 1
		print(count)

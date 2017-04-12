import csv
import json

with open('user_friends.csv', 'wb+') as fout:
	csv_file = csv.writer(fout)
	csv_file.writerow(['user_id', 'friend_id', 'type'])
	count = 0
	with open('yelp_academic_dataset_user.json') as fin:
		for line in fin:
			line_contents = json.loads(line)
			user_id = line_contents['user_id']
			friends = line_contents['friends']
			type = line_contents['type']
			for friend in friends:
				csv_file.writerow([user_id, friend, type])
				count = count + 1
		print(count)

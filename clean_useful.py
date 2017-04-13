import simplejson as json


def clean_user():
    """Drop columns that isn't used in the analysis"""
    with open("{0}.{1}".format('yelp_academic_dataset_user', 'json'), 'r') as f:
        with open("{0}.{1}".format('data/user_origin','json'), 'w') as out:
            for line in f:
                data = json.loads(line)
                data = {k:data[k] for k in data if k != "friends" and k != "fans"}
                json.dump(data, out)
                out.write('\n')


def clean_useful():
    """ Eliminate the un-useful user data and store the valid user data in user_useful.json"""
    useful_id = {}
    count = 0
    with open("{0}.{1}".format('data/user_origin', 'json'), 'r') as f:
        with open("{0}.{1}".format('data/user', 'json'), 'w') as out:
            for line in f:
                count += 1
                data = json.loads(line)
                if data['useful'] >= 1:
                    json.dump(data, out)
                    out.write('\n')
                    useful_id[data["user_id"]] = data["user_id"]
        print "raw entries of user_id: %d" % count
        print "after eliminated illegal user, number of user_id: %d" % len(useful_id)

    with open('data/useful_user_id.json', 'w') as user:
        json.dump(useful_id, user)


def enumerate_reveiw():
    """ Enumerate the text attribute in review into the length of review in review data"""
    with open("{0}.{1}".format('yelp_academic_dataset_review', 'json'), 'r') as f:
        with open("{0}.{1}".format('data/review', 'json'), 'w') as out:
            for line in f:
                data = json.loads(line)
                data['text'] = len(data['text'])
                json.dump(data, out)
                out.write('\n')


def main():

    print "drop un-useful user column"
    clean_user()
    print "done"

    print "start cleaning un-useful user"
    clean_useful()
    print "done"

if __name__ == '__main__':
    main()

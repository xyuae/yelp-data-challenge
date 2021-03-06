from multiprocessing import Pool

import simplejson as json


def clean_user():
    """ Eliminate the illegal elite data, eliminate the un-useful user data
    store the valid user data in user.json, user_id.json
    """
    elite = {}
    count = 0
    with open("{0}.{1}".format('yelp_academic_dataset_user', 'json'), 'r') as f:
        for line in f:
            count += 1
            data = json.loads(line)
            if eval(data['elite'][0]):
                big, small = max(data['elite']), min(data['elite'])
                yelp_since = data['yelping_since'].split('-')[0]
                # The user cannot be Elite before 2004, and big cannot exceed 2018
                if big <= str(2017) and small >= str(2004) and str(2004) <= yelp_since <= small:
                    elite[data['user_id']] = small
            else:
                elite[data['user_id']] = None
    print "raw data number of user_id: %d" % count
    print "after eliminated illegal elite, number of user_id: %d" % len(elite)
    final = {}
    with open("{0}.{1}".format('yelp_academic_dataset_review', 'json'), 'r') as f:
        for line in f:
            data = json.loads(line)
            year = data['date'].split('-')[0]
            try:
                if year <= elite[data['user_id']]:
                    final[data['user_id']] = data['user_id']
                elif not elite[data['user_id']]:
                    final[data['user_id']] = data['user_id']
            except:
                pass
    print "after eliminated illegal review time, number of user_id: %d" % len(final)

    # Store valid user in user.json
    with open("{0}.{1}".format('yelp_academic_dataset_user', 'json'), 'r') as f:
        with open('user.json', 'w') as res:
            for line in f:
                data = json.loads(line)
                if data['user_id'] in final:
                    json.dump(data, res)
                    res.write('\n')


def clean_business(file_name):
    """ Clean closed business and store the rest in business.json
    Store all valid business_id in business_id.json"""
    business_id = {}
    count = 0
    with open('{0}.{1}'.format(file_name, 'json'), 'r') as f:
        with open('{0}.{1}'.format('business', 'json'), 'w') as res:
            for line in f:
                count += 1
                data = json.loads(line)
                if data['is_open'] and data['hours']:
                    json.dump(data, res)
                    res.write('\n')
                    business_id[data['business_id']] = data['business_id']
    print "raw data number of business_id: %d" % count
    print "After eliminating invalid business data, number of entry: %d" % len(business_id)

    with open('{0}.{1}'.format('business_id', 'json'), 'w') as business:
        json.dump(business_id, business)


def user(file_name):
    """ Create user_id.json with user_id as key"""
    user_id = {}
    with open('{0}.{1}'.format(file_name, 'json'), 'r') as f:
        for line in f:
            data = json.loads(line)
            user_id[data['user_id']] = data['user_id']
    with open('user_id.json', 'w') as user:
        json.dump(user_id, user)


def del_missing(file_name, user_id, business_id):
    """ Clean the invalid entries in review, checkin, and tips file and store rest entries in json files"""
    print '{0} {1}'.format(file_name, 'updating!')
    count, final = 0, 0
    name = file_name.split('_')[3]
    with open("{0}.{1}".format(file_name, 'json'), 'r') as f:
        with open("{0}.{1}".format(name, 'json'), 'w') as res:
            for line in f:
                count += 1
                line = json.loads(line)
                try:
                    if line['user_id'] in user_id and line['business_id'] in business_id:
                        final += 1
                        json.dump(line, res)
                        res.write('\n')
                except:
                    if line['business_id'] in business_id:
                        final += 1
                        json.dump(line, res)
                        res.write('\n')
    print '{0} {1}'.format(name, 'updated!')
    print '{0}: {1}'.format('original number of %s' % name, count)
    print '{0}: {1}'.format('updated number of %s' % name, final)


def main():
    print "Start cleaning user data"
    clean_user()         # deal with user data, delete user with invalid elite attribute
    print "done"
    p = Pool()
    print "start clean business id"
    p.apply_async(clean_business, args=('yelp_academic_dataset_business', ))  # clean business_id
    print "done"
    print "create a dictionary of user_id"
    p.apply_async(user, args=('user', ))  # find user_list
    p.close()
    p.join()

    file_list = ['yelp_academic_dataset_review',
                 'yelp_academic_dataset_checkin',
                 'yelp_academic_dataset_tip']
    with open('business_id.json', 'r') as f:
        business_id = json.load(f)
    with open('user_id.json', 'r') as f:
        user_id = json.load(f)
    # second process
    p1 = Pool()
    print "delete missing data"
    for item in file_list:
        p1.apply_async(del_missing, args=(item, user_id, business_id))
    p1.close()
    p1.join()


if __name__ == '__main__':
    main()

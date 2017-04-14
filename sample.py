from sanity_check import user, del_missing
import simplejson as json
from multiprocessing import Pool


def sample():
    """ Sample user data such that only user with at least one useful data is sampled"""
    count = 0
    final = set()
    with open("{0}.{1}".format('data/user', 'json'), 'r') as f:
        with open("{0}.{1}".format('data/sample_user', 'json'), 'w') as out:
            for line in f:
                count += 1
                data = json.loads(line)
                if data['useful'] > 0:
                    json.dump(data, out)
                    out.write('\n')
                    final.add(data['user_id'])
    print "Number of entry in original data: %d" % count
    print "After sampling: %d" % len(final)


def main():
    print "start sampling"
    sample()
    print "Done"
    user('data/sample_user')

    p1 = Pool()
    file_list = ['yelp_academic_dataset_review',
                 'yelp_academic_dataset_checkin',
                 'yelp_academic_dataset_tip']
    with open('business_id.json', 'r') as f:
        business_id = json.load(f)
    with open('user_id.json', 'r') as f:
        user_id = json.load(f)
    print "delete missing data"
    for item in file_list:
        p1.apply_async(del_missing, args=(item, user_id, business_id))
    p1.close()
    p1.join()

if __name__ == '__main__':
    main()

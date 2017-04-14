import simplejson as json


def sample():
    """ Drop all columns in user starting with compliment"""

    columns = ['user_id',
                'yelping_since',
                'name',
                'review_count',
                'friends',
                'useful',
                'funny',
                'cool',
                'fans',
                'elite',
                'average_stars',]
    with open("{0}.{1}".format('data/sample_user', 'json'), 'r') as fin:
        with open("{0}.{1}".format('data/clean_sample_user', 'json'), 'w') as fout:
            for line in fin:
                data = json.loads(line)
                res = {k:data[k] for k in data if k in columns}
                json.dump(res, fout)
                fout.write('\n')
    # print "Number of entry in original data: %d" % count
    # print "After sampling: %d" % len(final)

if __name__ == '__main__':
    sample()

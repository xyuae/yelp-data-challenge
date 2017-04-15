import simplejson as json


def dropUserColumns():
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


def dropReviewColumns():
    """ Drop all columns in user starting with compliment"""
    columns = 'funny,user_id,review_id,text,business_id,stars,useful,cool'.split(',')
    with open("{0}.{1}".format('data/sample_review', 'json'), 'r') as fin:
        with open("{0}.{1}".format('data/clean_sample_review', 'json'), 'w') as fout:
            for line in fin:
                data = json.loads(line)
                res = {k:data[k] for k in data if k in columns}
                json.dump(res, fout)
                fout.write('\n')

def dropBusinessColumns():
    """ Drop all columns in user starting with compliment"""
    columns = 'business_id,postal_code,address,attributes,categories,city,review_count,name,longitude,state,stars,latitude,is_open'.split(',')
    with open("{0}.{1}".format('data/sample_review', 'json'), 'r') as fin:
        with open("{0}.{1}".format('data/clean_sample_review', 'json'), 'w') as fout:
            with open("{0}.{1}".format('data/reveiw_hour', 'json'), 'w') as fout2:
                for line in fin:
                    data = json.loads(line)
                    hour = data['hours']
                    res = {k:data[k] for k in data if k in columns}
                    json.dump(res, fout)
                    fout.write('\n')


if __name__ == '__main__':
    print "start"
    dropReviewColumns()
    print "done"

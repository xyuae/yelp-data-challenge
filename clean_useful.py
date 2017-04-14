import simplejson as json


def enumerate_user():
    """ Enumerate the text attribute in review into the length of review in review data"""
    with open("{0}.{1}".format('user', 'json'), 'r') as f:
        with open("{0}.{1}".format('data/user', 'json'), 'w') as out:
            for line in f:
                data = json.loads(line)
                data['friends'] = len(data['friends'])
                data['elite'] = len(data['elite'])
                json.dump(data, out)
                out.write('\n')


def enumerate_reveiw():
    """ Enumerate the text attribute in review into the length of review in review data"""
    with open("{0}.{1}".format('review', 'json'), 'r') as f:
        with open("{0}.{1}".format('data/sample_review', 'json'), 'w') as out:
            for line in f:
                data = json.loads(line)
                data['text'] = len(data['text'])
                json.dump(data, out)
                out.write('\n')


def main():
    # print "enumerate user data"
    # enumerate_user()
    # print "done"

    print "enumeate review data"
    enumerate_reveiw()
    print "done"


if __name__ == '__main__':
    main()

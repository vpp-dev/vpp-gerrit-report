#!/usr/bin/env python3

import sys
import json
import argparse
import requests

def getjson(url, request):
    '''Given a URL return the received JSON'''
    r = requests.get(url+request)
    if r.status_code != 200:
        raise IOError('Downloading from Gerrit failed')
    return json.loads(r.text[5:])

def get_changes_from_gerrit():
    URL = 'https://gerrit.fd.io/r'
    request = '/changes/?q=project:vpp+status:open+-is:wip&o=LABELS&o=CURRENT_REVISION&o=CURRENT_FILES&o=DETAILED_ACCOUNTS&o=CHECK&o=SUBMITTABLE'
    changes = getjson(URL, request)

    # We can only fetch 500 entries at the time, limit this to two tries
    last = changes[-1]
    try:
        if last['_more_changes'] == True:
            remaining = getjson(URL, request+'&S=500')
            changes += remaining
    except:
        pass
    return changes

def main():
    parser = argparse.ArgumentParser(description='VPP Gerrit changes download')
    parser.add_argument('outfile', type=argparse.FileType('w'))
    args = parser.parse_args()

    changes = get_changes_from_gerrit()
    json.dump(changes, args.outfile)
    args.outfile.close()

if __name__ == '__main__':
    sys.exit(main())

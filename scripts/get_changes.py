#!/usr/bin/env python3
#
# Copyright (c) 2022 Cisco and/or its affiliates.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import sys
import json
import argparse
import requests


def getjson(url, request):
    """Given a URL return the received JSON"""
    r = requests.get(url + request)
    if r.status_code != 200:
        raise IOError("Downloading from Gerrit failed")
    return json.loads(r.text[5:])


def get_changes_from_gerrit(branch):
    URL = "https://gerrit.fd.io/r"
    request = f"/changes/?q=project:vpp+status:open+branch:{branch}+-is:wip&o=LABELS&o=CURRENT_REVISION&o=CURRENT_FILES&o=DETAILED_ACCOUNTS&o=CHECK&o=SUBMITTABLE"
    changes = getjson(URL, request)
    last = changes[-1]
    batch_count = 500  # gerrit returns at most 500 entries at a time
    try:
        while last["_more_changes"] == True:
            remaining = getjson(URL, f"{request}&S={batch_count}")
            changes += remaining
            last = remaining[-1]
            batch_count += 500  # gerrit returns at most 500 entries at a time
    except:
        pass
    return changes


def main():
    parser = argparse.ArgumentParser(description="VPP Gerrit changes download")
    parser.add_argument("outfile", type=argparse.FileType("w"))
    parser.add_argument("-branch", default="master")
    args = parser.parse_args()

    changes = get_changes_from_gerrit(args.branch)
    json.dump(changes, args.outfile)
    args.outfile.close()


if __name__ == "__main__":
    sys.exit(main())

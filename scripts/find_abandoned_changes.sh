#! /usr/bin/env bash
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
set -euo pipefail

usage()
{
    echo -e "\nUsage: $0 <email address>"
    exit 1
}

if [ "$#" -ne "1" ] ; then
    usage
fi

email="$1"
if ! grep -qF '@' <<< "$email" ; then
    echo "ERROR: invalid email address: '$email'"
    usage
fi
report="VPP-GERRIT-REPORT.rst"

if [ ! -f "$report" ] ; then
    echo "ERROR: script must be run in vpp-gerrit-report workspace root directory!"
    usage
fi

# shellcheck disable=SC2046
abandon_report_ids="$(git grep 'Abandoned:' $(git rev-list --all -- $report) -- $report | cut -d':' -f1)"

trap 'git checkout main >& /dev/null' INT TERM EXIT
author_heading=""
for git_id in $abandon_report_ids ; do
    git checkout "$git_id" >& /dev/null
    abandon_report="$(sed '1,/Abandoned:/ {/Abandoned:/!d;}' $report | sed "1,/$email/ {/$email/!d}")"
    found_author=$(grep "$email" <<< "$abandon_report" | head -1)
    if [ -n "$found_author" ] ; then
        if [ -z "$author_heading" ] ; then
            author_heading="$found_author"
            echo -e "\n$author_heading\n"
        fi
        echo "Found in $report at git id: $git_id"
        sed '1,/Abandoned:/ {/Abandoned:/!d;}' $report | sed "1,/$email/ {/$email/!d}" | sed -n '3,/^$/ {/.*/p}' | sed 's/^$//g'
    fi
done
if [ -z "$author_heading" ] ; then
    echo -e "\nNo abandoned changes found for '$email'"
fi

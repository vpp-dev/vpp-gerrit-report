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

# Deactivate python virtual environment on termination
trap 'command -v deactivate >/dev/null && deactivate' INT TERM EXIT

script_dir="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
ws_root="$(dirname "$script_dir")"
indent="==> "
line="\n============================="

# Create the build dir
build_dir="$ws_root"/_build
mkdir -p "$build_dir"

# Create report directory
REPORT_DATE=${REPORT_DATE:-"$(date -u +%Y-%m-%d-%H%M%S)"}
export REPORT_DATE
report_dir="$build_dir"/report.$REPORT_DATE
rm -rf "$report_dir"    # ensure empty report directory
mkdir -p "$report_dir"

# Build and activate the python virtual environment
venv_dir="$build_dir"/venv
venv_activate_file="$venv_dir"/bin/activate
venv_build_log="$report_dir"/venv_build.log
echo -e "\n${indent}Building and Activating the python virtual environment...\n"
if ! "$script_dir"/venv_builder.py "$venv_dir" | tee "$venv_build_log"; then
    exit 1
fi
if [ ! -f "$venv_activate_file" ] ; then
    echo "ERROR: Missing venv activate file: '$venv_activate_file'"
    exit 1
fi
# shellcheck disable=SC1090
source "$venv_activate_file"

# Get MAINTAINERS file
echo -e "\n${indent}Retrieving MAINTAINERS file...\n"
maintainers_file="$report_dir"/MAINTAINERS
curl -o "$maintainers_file" https://git.fd.io/vpp/plain/MAINTAINERS

# Get gerrit changes in JSON
echo -e "\n${indent}Retrieving gerrit changes...\n"
changes_file="$report_dir"/gerrit-changes.json
"$script_dir"/get_changes.py "$changes_file"

# Generate Report
echo -e "${indent}Generating report...\n"
report_file="$report_dir/$REPORT_DATE-vpp-gerrit-report.rst"
"$script_dir"/review.py --maintainers-file "$maintainers_file" --changes-file "$changes_file" >"$report_file"

echo -e "$line"
echo -e "\nVPP Gerrit Report Generation Complete!\n"
echo "$report_dir:"
ls -l "$report_dir"
echo -e "$line"

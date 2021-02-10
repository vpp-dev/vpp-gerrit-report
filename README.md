# Gerrit open patches processing tool

To run:

Get maintainers file with: ./get_maintainers MAINTAINERS
Get the changeset from Gerrit with: ./get_changes.py CHANGES.json
Produce report: ./review.py --maintainers-file MAINTAINERS --changes-file CHANGES.json > report.txt

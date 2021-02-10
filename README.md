# Gerrit open patches processing tool

To run:

```
./get_maintainers MAINTAINERS
./get_changes.py CHANGES.json
./review.py --maintainers-file MAINTAINERS --changes-file CHANGES.json > report.txt

```

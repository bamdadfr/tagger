#!/bin/bash
source bin-configure.sh
for i in $(pip list -o | awk 'NR > 2 {print $1}'); do pip install -U $i; done
./bin-freeze.sh
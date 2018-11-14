#!/usr/bin/env bash

for j in `seq 1 201`; do echo  "\nRunning for Image: $j.jpg\n" ; python core.py $j + '.jpg'; done
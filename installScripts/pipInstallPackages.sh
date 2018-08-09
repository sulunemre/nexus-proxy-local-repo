#!/usr/bin/env bash

for i in {1..10}
do
    read p;
    pip download $p
done < pipAllPackagesList.txt
echo "Pip packages installed."

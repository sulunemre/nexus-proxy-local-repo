#!/usr/bin/env bash

apt update
for i in {1..10}
do
    read p;
    apt install $p -y --download-only
done < debianAllPackagesList.txt
echo "Debian packages installed."
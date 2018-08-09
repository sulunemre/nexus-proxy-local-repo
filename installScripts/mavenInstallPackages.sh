#!/usr/bin/env bash

for i in {1..10}
do
    read p;
    mvn dependency:get -Dartifact=$p
done < mavenAllPackagesList.txt
echo "Maven packages installed."

#!/usr/bin/env bash

src=/home/jcfr/Projects/Slicer-Release/Slicer-build
dest=/home/jcfr/Projects/sandbox/Notebooks/05_data

mkdir -p $dest

for file in Modules.json StartupTimes.json StartupTimesExcludingOneModule.json; do
  echo "Importing $file"
  cp $src/$file $dest
done
 

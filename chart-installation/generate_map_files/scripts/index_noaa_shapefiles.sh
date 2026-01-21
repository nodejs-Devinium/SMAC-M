#!/bin/bash

# IMPORTANT!
#
# This script should be executed ONLY from the Docker container and ONLY for the shapefiles generated
# using `noaa/config.enc.noaa.*.toml` config files!

for level in {1..6}; do
  for file in /data/generated/shp/${level}/*.shp; do
    shptree $file 1>/dev/null
  done
done

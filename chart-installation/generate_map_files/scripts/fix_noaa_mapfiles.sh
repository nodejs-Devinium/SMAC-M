#!/bin/bash

# IMPORTANT!
#
# This script should be executed ONLY from the Docker container and ONLY for the mapfiles generated
# using `noaa/config.enc.noaa.toml` or `noaa/config.enc.noaa.noarea.toml` config files!

# update absolute paths with the relative ones
sed -i 's/\/app\/noaa_enc\/generated\/shp/..\/shp/g' /app/noaa_enc/generated/map/*.map
sed -i 's/\/app\/noaa_enc\/generated\/map\///g' /app/noaa_enc/generated/map/*.map
sed -i 's/\/app\/noaa_enc\/generated\/map\///g' /app/noaa_enc/generated/map/legends/*.map

# fix some invalid relative paths
sed -i 's/..\/data/..\/shp/g' /app/noaa_enc/generated/map/legends/*.map
sed -i 's/FONTSET '\''.\//FONTSET '\''..\//g' /app/noaa_enc/generated/map/legends/*.map

# fix a variable that links to the folder with `proj.db` file (as seen in dockerized version of MapServer)
sed -i 's/CONFIG "PROJ_LIB" '\''.\/epsg'\''/CONFIG "PROJ_LIB" "\/usr\/local\/share\/proj"/g' /app/noaa_enc/generated/map/*.map
sed -i 's/CONFIG "PROJ_LIB" "..\/epsg"/CONFIG "PROJ_LIB" "\/usr\/local\/share\/proj"/g' /app/noaa_enc/generated/map/legends/*.map

# "GeomType." prefix leads to parsing errors
sed -i 's/GeomType.//g' /app/noaa_enc/generated/map/includes/*.map

# MINDISTANCE must be greater than 0
sed -i 's/MINDISTANCE 0/MINDISTANCE 1/g' /app/noaa_enc/generated/map/includes/*.map

# replace OP.XX construction with regular operators
sed -i 's/OP.LT/</g' /app/noaa_enc/generated/map/includes/*.map
sed -i 's/OP.LE/<=/g' /app/noaa_enc/generated/map/includes/*.map
sed -i 's/OP.GT/>/g' /app/noaa_enc/generated/map/includes/*.map
sed -i 's/OP.GE/>=/g' /app/noaa_enc/generated/map/includes/*.map
sed -i 's/OP.EQ/=/g' /app/noaa_enc/generated/map/includes/*.map
sed -i 's/OP.NE/!=/g' /app/noaa_enc/generated/map/includes/*.map
sed -i 's/OP.RE/~/g' /app/noaa_enc/generated/map/includes/*.map
sed -i 's/OP.IRE/~*/g' /app/noaa_enc/generated/map/includes/*.map

#!/usr/bin/env bash
set -e

mkdir -p data/raw

# Placeholder: replace with real data source commands
echo "date,close" > data/raw/nymex_ng.csv
echo "2020-01-01,2.50" >> data/raw/nymex_ng.csv

echo "date,close" > data/raw/ttf_ng.csv
echo "2020-01-01,15.00" >> data/raw/ttf_ng.csv

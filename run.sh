#!/bin/bash
echo
echo "<<<"
date
echo ${USER}

docker run \
  --rm \
  --mount source=housing-scraper-vol,target=/code/data/ \
  housing-scraper

echo ">>>"
echo

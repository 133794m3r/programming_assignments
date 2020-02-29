#!/bin/bash
# Macarthur Inbody
# 2020 -
# AGPLv3 
# This program will sort all words in the file words.txt And then sort them with frequency counts.
# Then it'll print the words followed by a single space.
cat words.txt | sed -e 's/\ /\n/g' | sort | uniq -cd | sort -n | sed -n 's/\([0-9]\{1,3\}\)/\1/p' | sed -e 's/[ ]\{4,6\}//g' -e 's/\([0-9]\{1,\}\)\ \([^0-9]\+\)/\2 \1/g'
 

#!/bin/env python

import csv, json, sys

if len(sys.argv) != 3:
   print "Usage: " + sys.argv[0] + " <input_json_file> <output_csv_file"
   print " Ex  : " + sys.argv[0] + " input.json output.csv"
   sys.exit(1)

# Input json file
fileInput = sys.argv[1]

# output csv file
fileOutput = sys.argv[2]

#open json file
inputFile = open(fileInput)

#load csv file
outputFile = open(fileOutput, 'w')

#load json content
data = json.load(inputFile)

#close the input file
inputFile.close()

#create a csv file
output = csv.writer(outputFile)

# Write Headers
output.writerow(data['results'][0].keys())

# Write all rows one by one
for row in data['results']:
    output.writerow(row.values()) #values row

print fileOutput + " file is written"

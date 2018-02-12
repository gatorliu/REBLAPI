#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import csv

def main():
    csv_path = sys.argv[1]
    print (readCSV(csv_path))

def readCSV(csv_path):
    ret = []
    with open(csv_path, 'rt') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
           ret.append(row)

    return ret


__ARGV_NUMBER = 2
def usage():
    if __ARGV_NUMBER == len(sys.argv):
        return True
    print("Usage: " + sys.argv[0] + " CSV_FILENAME")
    print()


if __name__ == "__main__":
    if usage():
        main()


#!/usr/bin/env python


import csv, sys

'''
reload(sys)
sys.setdefaultencoding('cp1250')
with open('ws_pr_koszt.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row
'''


 
ifile  = open('ws_pr_koszt.csv', "rb")
reader = csv.reader(ifile)
ofile  = open('ttest.csv', "wb")
writer = csv.writer(ofile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
 
for row in reader:
    writer.writerow(row)
 
ifile.close()
ofile.close()
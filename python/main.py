#!/usr/bin/env python
import urllib
import os
import re

def main():
    ads_list_temp = 'ads_list_temp.txt'
    ads_list = 'ads_list.txt'
    data = getData()
    writeToTempFile(data, ads_list_temp)
    generateCleanFile( ads_list, ads_list_temp)

# Generating a clean file
def generateCleanFile(ads_list, ads_list_temp):
    source = open(ads_list_temp,'r')
    if os.path.exists(ads_list):
        print('Deleted the build file')
        os.remove(ads_list)
    ads_list_file = open(ads_list,'w+')
    print('Generating clean file')
    for line in source.readlines():
        x = re.findall("^#", line)
        if not x:
            ads_list_file.write(line)

    if os.path.exists(ads_list):
        print('Delete the temp file')
        os.remove(ads_list_temp)


# Write to file the sources data
def writeToTempFile(data, ads_list_temp):
    if os.path.exists(ads_list_temp):
        print('Deleted the temp file')
        os.remove(ads_list_temp)
    print('fetched all content writing')
    f= open(ads_list_temp,"w+")
    f.write(data)
    f.close()
    print('Finished')

# Get the content
def getData():
    data = ''
    for source in getSources():
        print('Fetching {}!'.format(source))

        f = urllib.urlopen(source)
        data += "\n"
        data += f.read()

    return data

# Get sources
def getSources():
    sources = []
    with open('../sources.txt') as my_file:
        for line in my_file:
            sources.append(line)

    return sources




if __name__ == "__main__":
    main()
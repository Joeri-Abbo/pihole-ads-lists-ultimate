#!/usr/bin/env python
import urllib
import os

def main():
    data = getData()
    ads_list = 'ads_list.txt'
    writeToFile(data, ads_list)
   
def writeToFile(data, ads_list):
    if os.path.exists(ads_list):
        print('Deleted the file')
        os.remove(ads_list)
    print('fetched all content writing')
    f= open(ads_list,"w+")
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
    return [
        'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts',
        'https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhosts.txt'
    ];




if __name__ == "__main__":
    main()
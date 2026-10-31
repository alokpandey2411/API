# importing the required modules
import csv
import requests
import xml.etree.ElementTree as ET

def parseXML(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    newsitems = []
    for item in root.findall('./channel/item'):
        news = {}
        for child in item:
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8') # append news dictionary to news items list
        newsitems.append(news)
    return newsitems
def savetoCSV(newsitems, filename):
    field_names = ['guid', 'title', 'pubDate', 'description', 'link', 'media'] # writing to csv file
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = field_names,extrasaction='ignore') # writing headers (field names)
        writer.writeheader() # writing data rows
        writer.writerows(newsitems)

def main():
    newsitems = parseXML('rssfeed.xml')
    print (newsitems)
# store news items in a csv file
    savetoCSV(newsitems, 'topnews.csv')


if __name__ == "__main__":
    main() # calling main function 


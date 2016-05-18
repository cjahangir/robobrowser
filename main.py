import re
from robobrowser import RoboBrowser
import csv

browser = RoboBrowser(history=True)

with open('input.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        link = ', '.join(row)
        browser.open(link)
        links = browser.get_links()
        with open('output.csv', 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(links)

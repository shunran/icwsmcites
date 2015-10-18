from files.reader import Reader
from files.writer import Writer
from parsers.citecollector import CiteCollector

import requests

def collect_cites(infile, outfile):
    reader = Reader(infile)
    writer = Writer(outfile)
    cites = CiteCollector()
    for row in reader.readline():
        title =  reader.stripTitle(row)
        encoded = reader.encodeTitle(title)
        print(reader.encodeTitle(row))
        r = requests.get('https://scholar.google.com/scholar?hl=en&q=' + encoded)
        cites.feed(r.text)
        writer.write("%s;%s" % (cites.cites, title))

if __name__ == "__main__":
        collect_cites("2012.txt", "2012_cites.txt")


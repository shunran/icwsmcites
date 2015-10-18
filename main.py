from files.reader import Reader
from files.writer import Writer
from parsers.seleniumcitecollector import SeleniumCiteCollector


def collect_cites(infile, outfile):
    reader = Reader(infile)
    writer = Writer(outfile)
    request = SeleniumCiteCollector()
    for row in reader.readline():
        title =  reader.stripTitle(row)
        encoded = reader.encodeTitle(title)
        request.get('https://scholar.google.com/scholar?hl=en&q=' + encoded)
        cites = request.findCites()
        writer.write("%s;%s" % (cites, title))
    writer.close()

if __name__ == "__main__":
        collect_cites("2015.txt", "2015_cites.txt")

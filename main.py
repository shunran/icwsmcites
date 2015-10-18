from files.reader import Reader
from files.writer import Writer
from parsers.seleniumcitecollector import SeleniumCiteCollector
import pandas as pd


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

def draw_pd(infile, outfile):
    ser = pd.read_csv(infile, sep=";")
    print(ser)
    '''
    reader = Reader(infile)
    for line in reader.readline():
        print(line)
        ser.put(line.split(";")[0])
    '''
    plot = ser.plot()
    fig = plot.get_figure()
    fig.savefig(outfile)


if __name__ == "__main__":
    #collect_cites("2015.txt", "2015_cites.txt")
    draw_pd("2014_cites.txt", "2014")
    pass

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

def draw_pd(infile, outfilename, outcsv="outfile.csv"):
    #pd.set_option('max_colwidth',140)
    dCites = pd.read_csv(infile, sep=";", header=None, names=("cite count", "title", "OK"))
    dCites.drop('OK', 1, inplace=True)
    dSorted = dCites.sort_values("cite count", axis=0, ascending=False)
    plot = dCites.plot(kind="bar", title=outfilename, xticks=[])
    print("Keskmine %.2f ja mediaan %.2f kõigist %d ettekandest" % (dSorted.mean(axis=0), dSorted.median(axis=0),
                                                                    len(dSorted.index)))
    print("%s TOP 10" % outfilename)
    #mean = dCites.mean(axis=0,numeric_onyl=True)
    #print(mean)
    #return
    print(dSorted[0:10])
    dSorted[0:10].to_csv(outfilename + "_topstats.csv", sep=";")
    fig = plot.get_figure()
    fig.savefig(outfilename)


if __name__ == "__main__":
    #collect_cites("2015.txt", "2015_cites.txt")
    draw_pd("2015_cites.txt", "2015")
    pass

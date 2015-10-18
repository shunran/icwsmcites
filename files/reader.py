import re
import urllib


class Reader:
    def __init__(self, infilename):
        self.infile = open(infilename, 'r', encoding='utf-8')

    def readline(self):
        for line in self.infile:
            yield line

    def stripTitle(self, row):
        words = row.split(";")[0].strip()
        match = re.match("^\d+:\s?(.*)$", words)
        if not match:
            print("NO MATCH: %s" % words)
            return None
        else:
            return match.group(1)

    def encodeTitle(self, title):
        return urllib.parse.quote_plus(title)

    def close(self):
        self.infile.close()


class Writer:
    def __init__(self, outfilename):
        self.outfile = open(outfilename, 'w', encoding='utf-8')

    def write(self, file_strings):
        self.outfile.write("%s\n" % file_strings)

    def close(self):
        self.outfile.close()

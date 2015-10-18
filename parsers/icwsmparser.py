from html.parser import HTMLParser

import requests

from files.writer import Writer


class IcwsmParser(HTMLParser):
    '''
    #wrapper > div.container_12.bodyContainer > div.grid_8.textContent > div > p:nth-child(13) > b:nth-child(1)
    #/*[@id="wrapper"]/div[6]/div[1]/div/p[2]/b[1]
    '''
    in_area = False
    started = False
    title = False
    div = 0
    prog_topic = ""

    def __init__(self, url='http://www.icwsm.org/2015/program/program/', filename='2015.txt'):
        super().__init__()
        self.url = url
        self.writer = Writer(filename)

    def run(self):
        r = requests.get(self.url)
        self.feed(r.text)

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            self.div += 1
            for attr in attrs:
                if attr[0] == 'class' and attr[1] == 'textContentWrapper':
                    self.in_area = True
        if tag == 'p' and not self.started:
            self.started = True
        if self.started and tag == 'b':
            self.title = True

    def handle_endtag(self, tag):
        if tag == 'div':
            self.div -= 1
            if self.div < 4: self.in_area = False
        if self.in_area and self.started and tag == 'p':
            print("P ended")
            self.started = False
        if self.in_area and self.started and self.title and tag == 'b':
            self.title = False
            print("Encountered an end tag :", tag)

    def handle_data(self, data):
        if self.in_area and self.started and self.title:
            self.prog_topic = data
            print("Topic was:", data)
            self.title = False
            return
        if self.in_area and self.started and data.strip():
            print("Authors were:", data.strip())
            self.writer.write("%s; %s" % (self.prog_topic, data.strip()))
            self.prog_topic = ""

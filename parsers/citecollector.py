from html.parser import HTMLParser
import re


class CiteCollector(HTMLParser):
    '''
    <div class="gs_fl">
    <a href="/scholar?cites=2555323274695215522&amp;as_sdt=2005&amp;sciodt=0,5&amp;hl=en&amp;oe=ASCII">Cited by 59</a>
    '''
    cites = None
    in_area = False
    in_tag = False

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            for attr in attrs:
                if attr[0] == 'class' and attr[1] == 'gs_fl':
                    self.in_area = True
        if self.in_area and tag == 'a':
            for attr in attrs:
                if attr[0] == 'href' and re.match("^/scholar\?cites", attr[1]):
                    self.in_tag = True
                    break


    def handle_data(self, data):
        if self.in_tag:
            match = re.match('Cited by (\d+)', data)
            if match:
                self.cites = match.group(1)
            self.in_tag = False

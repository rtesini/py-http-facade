"""This module is the core of the HttpFacade."""
import re,json

REGEX_NO_BASIC = r"^(?P<protocol>https*)\:\/\/(?P<domain>[\w|\.]+)\:*(?P<port>\d*)\/(?P<path>[\w|\/]*)\?(?P<query>[\w|\/|\=\&]*)"
REGEX_BASIC = r"^(?P<protocol>https*)\:\/\/(?P<user>[\w|\s]+)\:(?P<pass>[\w|\s]+)\@(?P<domain>[\w|\.]+)\:*(?P<port>\d*)\/(?P<path>[\w|\/]*)\?(?P<query>[\w|\/|\=\&]*)"

class UrlParserUtil(object):
    """Url Parser Util"""
    protocol = 'http'
    domain = None
    port = 80
    user = None
    password = None
    path = None
    url = None
    query = None
    pattern = None
    
    def __init__(self, url):
        self.url = url
        self.pattern = re.compile(REGEX_NO_BASIC)
        if(re.search(REGEX_NO_BASIC, url)):
            matches = re.search(REGEX_NO_BASIC, url)
            self.protocol = matches.group('protocol')
            self.domain = matches.group('domain')
            self.port = matches.group('port')
            self.path = matches.group('path')
            self.query = matches.group('query')

        if(re.search(REGEX_BASIC, url)):
            matches = re.search(REGEX_BASIC, url)
            self.protocol = matches.group('protocol')
            self.domain = matches.group('domain')
            self.port = matches.group('port')
            self.path = matches.group('path')
            self.query = matches.group('query')
            self.user = matches.group('user')
            self.password = matches.group('pass')
            


        




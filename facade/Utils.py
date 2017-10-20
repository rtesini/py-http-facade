"""This module is the core of the HttpFacade."""
import re

REGEX_PROTOCOL_NO_BASIC = r"^(?P<protocol>https*)\:\/\/(?P<domain>[\w|\.]+)\:*(?P<port>\d*)\/(?P<path>[\w|\/|\.]*)\?(?P<query>[\w|\/|\=\&]*)"
REGEX_PROTOCOL_BASIC = r"^(?P<protocol>https*)\:\/\/(?P<user>[\w|\s]+)\:(?P<pass>[\w|\s]+)\@(?P<domain>[\w|\.]+)\:*(?P<port>\d*)\/(?P<path>[\w|\/|\.]*)\?(?P<query>[\w|\/|\=\&]*)"

REGEX_NO_PROTOCOL_NO_BASIC = r"^(?P<domain>[\w|\.]+)\:*(?P<port>\d*)\/(?P<path>[\w|\/|\.]*)\?(?P<query>[\w|\/|\=\&]*)"
REGEX_NO_PROTOCOL_BASIC = r"^(?P<user>[\w|\s]+)\:(?P<pass>[\w|\s]+)\@(?P<domain>[\w|\.]+)\:*(?P<port>\d*)\/(?P<path>[\w|\/|\.]*)\?(?P<query>[\w|\/|\=\&]*)"

REGEX_NO_PROTOCOL_NO_BASIC_NO_QUERY = r"^(?P<domain>[\w|\.]+)\:*(?P<port>\d*)\/(?P<path>[\w|\/|\.]*)"

REGEX_NO_PROTOCOL_NO_BASIC_NO_QUERY_NO_PORT = r"^(?P<domain>[\w|\.]+)"

class UrlParserUtil(object):
    """Url Parser Util"""
    # pylint: disable=too-many-instance-attributes, too-few-public-methods
    # all attributes are reasonable in this case.
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
        
        if(re.search(REGEX_NO_PROTOCOL_NO_BASIC_NO_QUERY_NO_PORT, url)):
            matches = re.search(REGEX_NO_PROTOCOL_NO_BASIC_NO_QUERY_NO_PORT, url)
            self.domain = matches.group('domain')

        if(re.search(REGEX_NO_PROTOCOL_NO_BASIC_NO_QUERY, url)):
            matches = re.search(REGEX_NO_PROTOCOL_NO_BASIC_NO_QUERY, url)
            self.domain = matches.group('domain')
            if(matches.group('port')):
                self.port = matches.group('port')
            self.path = matches.group('path')

        if(re.search(REGEX_NO_PROTOCOL_NO_BASIC, url)):
            matches = re.search(REGEX_NO_PROTOCOL_NO_BASIC, url)
            self.domain = matches.group('domain')
            if(matches.group('port')):
                self.port = matches.group('port')
            self.path = matches.group('path')
            self.query = matches.group('query')

        if(re.search(REGEX_PROTOCOL_NO_BASIC, url)):
            matches = re.search(REGEX_PROTOCOL_NO_BASIC, url)
            self.protocol = matches.group('protocol')
            self.domain = matches.group('domain')
            if(matches.group('port')):
                self.port = matches.group('port')
            self.path = matches.group('path')
            self.query = matches.group('query')

        if(re.search(REGEX_PROTOCOL_BASIC, url)):
            matches = re.search(REGEX_PROTOCOL_BASIC, url)
            self.protocol = matches.group('protocol')
            self.domain = matches.group('domain')
            if(matches.group('port')):
                self.port = matches.group('port')
            self.path = matches.group('path')
            self.query = matches.group('query')
            self.user = matches.group('user')
            self.password = matches.group('pass')
        
        if(re.search(REGEX_NO_PROTOCOL_BASIC, url)):
            matches = re.search(REGEX_NO_PROTOCOL_BASIC, url)
            self.domain = matches.group('domain')
            if(matches.group('port')):
                self.port = matches.group('port')
            self.path = matches.group('path')
            self.query = matches.group('query')
            self.user = matches.group('user')
            self.password = matches.group('pass')


        




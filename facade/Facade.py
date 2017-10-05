"""This module is the core of the HttpFacade."""
import urllib,httplib
import re
import base64
from facade.Utils import UrlParserUtil

def matches(value, pattern_to_match):
    pattern = re.compile(pattern_to_match)
    return pattern.match(value)

class Url(object):
    url = None
    method  = None
    protocol = 'http'
    domain = None
    port = 80
    user = None
    password = None
    path = None
    def __init__(self, url):
        self.url = url
        http_util = UrlParserUtil("https://aaaa:bbbb@regex101.com:8080/blablabla/blebleble?bli=blo&blu=hgfhgf")
        self.protocol = http_util.protocol
        

class HttpFacade(object):
    """Http Facade Class"""
    headers = {}
    queries = {}
    formParams = {}
    _body = None
    _body_arr = None
    is_gzip = False
    time_out = 3 * 60 * 1000
    follow_redirects = False

    def __init__(self, url):
        self.headers = {}
        self.queries = {}
        self.url = url

    def header(self, key, header):
        """add header to facade."""
        if not key in self.headers :
            self.headers[key] = []
        self.headers[key].append(header)
        return self
    
    def timeout(self, time):
        """set timeout for request."""
        self.time_out = time
        return self

    def notimeout(self):
        """remove timeout from request."""
        self.time_out = None
        return self

    def cookies(self,cookies):
        """add cookies to request."""
        cookies_str = ""
        for k in cookies.keys :
            cookies_str += k + '=' + cookies[k]
        return self.header("Cookie", cookies_str)

    def gzip(self, accept_content):
        """set GZIP to request."""
        self.is_gzip = True
        return self.header("Accept-Encoding", accept_content)
    
    def query(self, key, query):
        """add header to facade."""
        if not key in self.queries :
            self.queries[key] = []
        self.queries[key].append(query)
        return self

    def body(self, body):
        """add body to facade."""
        self._body = body
        self._body_arr = bytearray()
        self._body_arr.extend(self._body)
        return self

    def user(self, user, password):
        """add user and password to request."""
        token = user + ":" + password;
        re.split("([a-z0-9A-Z]*)://(.*)", self.url)
        if not matches(self.url, "([a-z0-9A-Z]*)://(.*)") :
            self.url = token + "@" + self.url
        else:
            splited = re.split("([a-z0-9A-Z]*)://(.*)", self.url)
            self.url = splited[1] + "://" + token + "@" + splited[2]

        basic = "Basic " + base64.b64encode(token)
        return self.header("Authentication", basic)
    
    # def __get_url(self):
    #     """retreive url from parameters."""
    #     query = ""
    #     if self.queries:
    #         query = "?" + urllib.urlencode(self.queries)
    #     return self.base_url + query

    # def __generate_connection(self):
    #     """the actual connection."""
    #     http = httplib.HTTPConnection(self.__get_url())
    #     http.follow_redirects = self.follow_redirects
    #     if self.time_out:
    #         http.timeout = self.time_out
        

    


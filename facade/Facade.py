"""This module is the core of the HttpFacade."""
import urllib,httplib

class HttpFacade(object):
    """Http Facade Class"""
    headers = {}
    queries = {}
    formParams = {}
    url = None
    method  = None
    protocol = None
    domain = None
    port = 80
    user = None
    password = None
    path = None
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
    
    def __get_url(self):
        """retreive url from parameters."""
        query = ""
        if self.queries:
            query = "?" + urllib.urlencode(self.queries)
        return self.base_url + query

    def __generate_connection(self):
        """the actual connection."""
        http = httplib.HTTPConnection(self.__get_url())
        http.follow_redirects = self.follow_redirects
        if self.time_out:
            http.timeout = self.time_out
        

    


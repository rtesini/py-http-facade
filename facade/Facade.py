"""This module is the core of the HttpFacade."""
import urllib, httplib
import re
import base64
from facade.Utils import UrlParserUtil

def matches(value, pattern_to_match):
    """RE for pattern"""
    pattern = re.compile(pattern_to_match)
    return pattern.match(value)

class Url(object):
    """URL T.O."""
    # pylint: disable=too-many-instance-attributes, too-few-public-methods
    # all attributes are reasonable in this case.
    protocol = 'http'
    domain = None
    port = 80
    user = None
    password = None
    path = None
    query = None
    url = None

    def __init__(self, url):
        self.url = url
        http_util = UrlParserUtil(url)
        self.protocol = http_util.protocol
        self.domain = http_util.domain
        self.path = http_util.path
        self.port = http_util.port
        self.query = http_util.query
        self.user = http_util.user
        self.password = http_util.password


class HttpFacade(object):
    """Http Facade Class"""
    headers = {}
    queries = {}
    form_params = {}
    url = None
    url_to = None
    _body = None
    _body_arr = None
    is_gzip = False
    time_out = 3 * 60 * 1000
    follow_redirects = False

    def __init__(self, url):
        self.headers = {}
        self.queries = {}
        self.url = url
        self.url_to = Url(self.url)

    def protocol(self, protocol):
        """set protocol for request."""
        setattr(self.url_to, 'protocol', protocol)
        return self
    
    def domain(self, domain):
        """set domain for request."""
        setattr(self.url_to, 'domain', domain)
        return self

    def port(self, port):
        """set port for request."""
        setattr(self.url_to, 'port', port)
        return self

    def path(self, path):
        """set path for request."""
        setattr(self.url_to, 'path', path)
        return self

    def url_query(self, query):
        """set query for request."""
        setattr(self.url_to, 'query', query)
        return self

    def timeout(self, time):
        """set timeout for request."""
        self.time_out = time
        return self

    def notimeout(self):
        """remove timeout from request."""
        self.time_out = None
        return self

    def query(self, key, query):
        """add query parameter to facade."""
        if not key in self.queries:
            self.queries[key] = []
        self.queries[key].append(query)
        return self

    def header(self, key, header):
        """add header to facade."""
        if not key in self.headers:
            self.headers[key] = []
        self.headers[key].append(header)
        return self

    def param(self, key, param):
        """add parameters to facade."""
        if not key in self.form_params:
            self.form_params[key] = []
        self.form_params[key].append(param)
        return self

    def cookies(self, cookies):
        """add cookies to request."""
        cookies_str = ""
        for k in cookies.keys:
            cookies_str += k + '=' + cookies[k]
        return self.header("Cookie", cookies_str)

    def gzip(self, accept_content):
        """set GZIP to request."""
        self.is_gzip = True
        return self.header("Accept-Encoding", accept_content)

    def body(self, body):
        """add body to facade."""
        self._body = body
        self._body_arr = bytearray()
        self._body_arr.extend(self._body)
        return self

    def user(self, user, password):
        """add user and password to request."""
        setattr(self.url_to, 'user', user)
        setattr(self.url_to, 'password', password)
        token = user + ":" + password
        regex_for_http = "([a-z0-9A-Z]*)://(.*)"
        if not matches(self.url, regex_for_http):
            self.url = token + "@" + self.url
        else:
            splited = re.split(regex_for_http, self.url)
            self.url = splited[1] + "://" + token + "@" + splited[2]

        basic = "Basic " + base64.b64encode(token)
        return self.header("Authentication", basic)
    
    def __generate_connection(self):
        """the actual connection."""
        http = None
        print "DOMAIN "
        domain = self.url_to.domain
        
        if self.url_to.port != 80 :
            domain = domain + ":" + str(self.url_to.port)

        print domain
        if self.url_to.protocol == 'http':
            print "HTTP"
            http = httplib.HTTPConnection(domain)
        else:
            print "HTTPS"
            http = httplib.HTTPSConnection(domain)

        http.follow_redirects = self.follow_redirects
        if self.time_out:
            http.timeout = self.time_out

        return http

    def get(self):
        """GET HTTP Method"""
        conn = self.__generate_connection()
        print conn
        print self.url_to.path
        path = self.url_to.path
        if len(self.queries) > 0 :
            params = urllib.urlencode(self.queries)
            path = path + '?'+params
        conn.request("GET", path,'',self.headers)
        r1 = conn.getresponse()
        r1.content = r1.read()
        print r1.status, r1.reason
        r1.close()
        return r1
"""This module Tests HttpFacade."""

import unittest
from facade.Utils import UrlParserUtil

class UrlParserUtilTest(unittest.TestCase):
    """UrlParserUtil Class Tests"""
    def test_url_full(self):
        """Test Base"""
        http_util = UrlParserUtil("https://regex101.com:8080/blablabla/blebleble?bli=blo&blu=hgfhgf")
        self.assertEquals("https", http_util.protocol)
        self.assertEquals("regex101.com", http_util.domain)
        self.assertEquals("blablabla/blebleble", http_util.path)
        self.assertEquals("bli=blo&blu=hgfhgf", http_util.query)

    def test_url_no_protocol(self):
        """Test Base"""
        http_util = UrlParserUtil("www.regex101.com:8080/blablabla/blebleble?bli=blo&blu=hgfhgf")
        self.assertEquals("http", http_util.protocol)
        self.assertEquals("www.regex101.com", http_util.domain)
        self.assertEquals("blablabla/blebleble", http_util.path)
        self.assertEquals("bli=blo&blu=hgfhgf", http_util.query)

    def test_url_basic_full(self):
        """Test Base"""
        http_util = UrlParserUtil("aaaa:bbbb@www.regex101.com:8080/blablabla/blebleble?bli=blo&blu=hgfhgf")
        self.assertEquals("http", http_util.protocol)
        self.assertEquals("www.regex101.com", http_util.domain)
        self.assertEquals("blablabla/blebleble", http_util.path)
        self.assertEquals("bli=blo&blu=hgfhgf", http_util.query)
        self.assertEquals("aaaa", http_util.user)
        self.assertEquals("bbbb", http_util.password)
        
    def test_url_no_port(self):
        """Test Base"""
        http_util = UrlParserUtil("https://regex101.com/blablabla/blebleble?bli=blo&blu=hgfhgf")
        self.assertEquals("https", http_util.protocol)
        self.assertEquals("regex101.com", http_util.domain)
        self.assertEquals("blablabla/blebleble", http_util.path)
        self.assertEquals("bli=blo&blu=hgfhgf", http_util.query)
        self.assertEquals(80, http_util.port)
        
    
    
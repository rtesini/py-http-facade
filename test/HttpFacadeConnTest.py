"""This module Tests HttpFacade."""

import unittest
import json
from facade.Facade import HttpFacade

class HttpFacadeTest(unittest.TestCase):
    """Http Facade Class Tests"""
    
    def test_localhost(self):
        """Test Base"""
        http_facade = HttpFacade("localhost")
        http_facade.port(8000).path("static/hello.html")
        res = http_facade.get()
        self.assertEquals(200, res.status)
        self.assertEquals("HELLO", res.content)

    def test_localhost_query(self):
        """Test GET with params"""
        http_facade = HttpFacade("localhost")
        http_facade.port(8000).path("static/variables.html").query("tst","tst")
        http_facade.header("hdr_1", "hdr_1")
        res = http_facade.get()
        self.assertEquals(200, res.status)
        self.assertEquals('VARIABLES:{"tst": ["[\'tst\']"]}', res.content)
        self.assertTrue('hdr_1' in json.dumps(res.getheaders()))
        
    def test_localhost_first_post(self):
        """Test POST"""
        http_facade = HttpFacade("localhost")
        http_facade.port(8000).path("client").param("tst","tst")
        http_facade.header("hdr_1", "hdr_1")
        res = http_facade.post()
        self.assertEquals(200, res.status)
        self.assertEquals('tst=%5B%27tst%27%2C+%27tst2%27%2C+%27tst%27%5D', res.read())
        self.assertTrue('hdr_1' in json.dumps(res.getheaders()))
    
    def test_localhost_first_put(self):
        """Test POST"""
        http_facade = HttpFacade("localhost")
        http_facade.port(8000).path("client").param("tst","tst")
        http_facade.header("hdr_1", "hdr_1")
        res = http_facade.put()
        self.assertEquals(200, res.status)
        self.assertEquals('tst=%5B%27tst%27%2C+%27tst2%27%2C+%27tst%27%5D', res.read())
        self.assertTrue('hdr_1' in json.dumps(res.getheaders()))
        
        
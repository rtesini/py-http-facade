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
        """Test Base"""
        http_facade = HttpFacade("localhost")
        http_facade.port(8000).path("static/variables.html").query("tst","tst")
        http_facade.header("hdr_1", "hdr_1")
        res = http_facade.get()
        self.assertEquals(200, res.status)
        self.assertEquals('VARIABLES:{"tst": ["[\'tst\']"]}', res.content)
        self.assertTrue('hdr_1' in json.dumps(res.getheaders()))
        
        
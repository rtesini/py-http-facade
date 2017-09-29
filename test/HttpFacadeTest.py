"""This module Tests HttpFacade."""

import unittest
from facade.Facade import HttpFacade

class HttpFacadeTest(unittest.TestCase):
    """Http Facade Class Tests"""
    
    def test_base(self):
        """Test Base"""
        http_facade = HttpFacade("tst")
        self.assertEquals("tst", http_facade.url)
    
    def test_headers_queries(self):
        """Test Headers"""
        http_facade = HttpFacade("tst")
        http_facade.header("tst", "tst").header("tst", "tst2")
        self.assertEquals({"tst": ["tst", "tst2"]}, http_facade.headers)
        http_facade.query("tst", "tst").query("tst", "tst2")
        self.assertEquals({"tst": ["tst", "tst2"]}, http_facade.queries)
    
        
    

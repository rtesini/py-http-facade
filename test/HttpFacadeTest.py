"""This module Tests HttpFacade."""

import unittest
from facade.Facade import HttpFacade

class HttpFacadeTest(unittest.TestCase):
    """Http Facade Class Tests"""
    def test_base(self):
        """Test Base"""
        a = HttpFacade("tst")
        self.assertEquals("tst", a.base_url)
    
    def test_headers_queries(self):
        """Test Headers"""
        a = HttpFacade("tst")
        a.header("tst", "tst").header("tst", "tst2")
        self.assertEquals({"tst": ["tst", "tst2"]}, a.headers)
        a.query("tst", "tst").query("tst", "tst2")
        self.assertEquals({"tst": ["tst", "tst2"]}, a.queries)
        

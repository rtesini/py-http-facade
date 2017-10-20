"""This module Tests HttpFacade."""

import unittest
from facade.Facade import HttpFacade

class HttpFacadeTest(unittest.TestCase):
    """Http Facade Class Tests"""
    
    def test_localhost(self):
        """Test Base"""
        http_facade = HttpFacade("localhost")
        http_facade.port(8000).path("/test/static/hello.html")
        res = http_facade.get()
        self.assertEquals(200, res.status)

    # def test_localhost1(self):
    #     """Test Base"""
    #     http_facade = HttpFacade("localhost:8000/test/static/hello.html")
    #     res = http_facade.get()
    #     self.assertEquals(200, res.status)
    
    
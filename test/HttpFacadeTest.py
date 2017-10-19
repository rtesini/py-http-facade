"""This module Tests HttpFacade."""

import unittest
from facade.Facade import HttpFacade

class HttpFacadeTest(unittest.TestCase):
    """Http Facade Class Tests"""
    
    def test_base(self):
        """Test Base"""
        http_facade = HttpFacade("tst")
        self.assertEquals("tst", http_facade.url)
        self.assertEquals("tst", http_facade.url_to.domain)

        http_facade = HttpFacade("www.uol.com.br")
        self.assertEquals("www.uol.com.br", http_facade.url_to.domain)
    
    def test_headers_queries(self):
        """Test Headers"""
        http_facade = HttpFacade("tst")
        http_facade.header("tst", "tst").header("tst", "tst2")
        self.assertEquals({"tst": ["tst", "tst2"]}, http_facade.headers)
        http_facade.query("tst", "tst").query("tst", "tst2")
        self.assertEquals({"tst": ["tst", "tst2"]}, http_facade.queries)

    def test_params(self):
        """Test Params"""
        http_facade = HttpFacade("tst")
        http_facade.param("tst", "tst").param("tst", "tst2")
        self.assertEquals({"tst": ["tst", "tst2"]}, http_facade.form_params)
        
    def test_user_no_http(self):
        """User Test"""
        http_facade = HttpFacade("luan.xyz")
        http_facade.user("danilo", "xptopass")
        self.assertEquals("danilo:xptopass@luan.xyz", http_facade.url)
        self.assertTrue("Authentication" in http_facade.headers.keys())

    def test_user_http(self):
        """User Test 2"""
        http_facade = HttpFacade("https://luan.xyz")
        http_facade.user("danilo", "xptopass")
        self.assertEquals("https://danilo:xptopass@luan.xyz", http_facade.url)
        self.assertTrue("Authentication" in http_facade.headers.keys())

    def test_user_to(self):
        """UserTo Test"""
        http_facade = HttpFacade("https://regex101.com:8080/blablabla/blebleble?bli=blo&blu=hgfhgf")
        self.assertEquals("regex101.com", http_facade.url_to.domain)
        self.assertEquals("http", http_facade.protocol('http').url_to.protocol)
        
        
        
    
        
    

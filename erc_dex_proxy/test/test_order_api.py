# coding: utf-8

"""
    ERC dEX Proxy Service

    Command line app for ERC dEX Trading Automation  # noqa: E501

    OpenAPI spec version: 1.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import erc_dex_proxy
from erc_dex_proxy.api.order_api import OrderApi  # noqa: E501
from erc_dex_proxy.rest import ApiException


class TestOrderApi(unittest.TestCase):
    """OrderApi unit test stubs"""

    def setUp(self):
        self.api = erc_dex_proxy.api.order_api.OrderApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cancel_order(self):
        """Test case for cancel_order

        """
        pass

    def test_create_order(self):
        """Test case for create_order

        """
        pass

    def test_fill_order(self):
        """Test case for fill_order

        """
        pass


if __name__ == '__main__':
    unittest.main()

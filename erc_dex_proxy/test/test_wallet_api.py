# coding: utf-8

"""
    ERC dEX Proxy Service

    Command line app for ERC dEX Trading Automation  # noqa: E501

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import erc_dex_proxy
from erc_dex_proxy.api.wallet_api import WalletApi  # noqa: E501
from erc_dex_proxy.rest import ApiException


class TestWalletApi(unittest.TestCase):
    """WalletApi unit test stubs"""

    def setUp(self):
        self.api = erc_dex_proxy.api.wallet_api.WalletApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_account(self):
        """Test case for get_account

        """
        pass

    def test_get_balance(self):
        """Test case for get_balance

        """
        pass

    def test_get_ether_balance(self):
        """Test case for get_ether_balance

        """
        pass

    def test_unwrap_ether(self):
        """Test case for unwrap_ether

        """
        pass

    def test_wrap_ether(self):
        """Test case for wrap_ether

        """
        pass


if __name__ == '__main__':
    unittest.main()
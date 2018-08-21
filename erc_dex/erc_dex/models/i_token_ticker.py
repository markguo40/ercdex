# coding: utf-8

"""
    ERC dEX REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1-alpha
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ITokenTicker(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'symbol': 'str',
        'usd_price': 'str',
        'daily_percentage_change': 'str',
        'daily_volume': 'str',
        'price_eth': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'usd_price': 'usdPrice',
        'daily_percentage_change': 'dailyPercentageChange',
        'daily_volume': 'dailyVolume',
        'price_eth': 'priceEth'
    }

    def __init__(self, symbol=None, usd_price=None, daily_percentage_change=None, daily_volume=None, price_eth=None):  # noqa: E501
        """ITokenTicker - a model defined in Swagger"""  # noqa: E501

        self._symbol = None
        self._usd_price = None
        self._daily_percentage_change = None
        self._daily_volume = None
        self._price_eth = None
        self.discriminator = None

        self.symbol = symbol
        self.usd_price = usd_price
        self.daily_percentage_change = daily_percentage_change
        self.daily_volume = daily_volume
        self.price_eth = price_eth

    @property
    def symbol(self):
        """Gets the symbol of this ITokenTicker.  # noqa: E501


        :return: The symbol of this ITokenTicker.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this ITokenTicker.


        :param symbol: The symbol of this ITokenTicker.  # noqa: E501
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def usd_price(self):
        """Gets the usd_price of this ITokenTicker.  # noqa: E501


        :return: The usd_price of this ITokenTicker.  # noqa: E501
        :rtype: str
        """
        return self._usd_price

    @usd_price.setter
    def usd_price(self, usd_price):
        """Sets the usd_price of this ITokenTicker.


        :param usd_price: The usd_price of this ITokenTicker.  # noqa: E501
        :type: str
        """
        if usd_price is None:
            raise ValueError("Invalid value for `usd_price`, must not be `None`")  # noqa: E501

        self._usd_price = usd_price

    @property
    def daily_percentage_change(self):
        """Gets the daily_percentage_change of this ITokenTicker.  # noqa: E501


        :return: The daily_percentage_change of this ITokenTicker.  # noqa: E501
        :rtype: str
        """
        return self._daily_percentage_change

    @daily_percentage_change.setter
    def daily_percentage_change(self, daily_percentage_change):
        """Sets the daily_percentage_change of this ITokenTicker.


        :param daily_percentage_change: The daily_percentage_change of this ITokenTicker.  # noqa: E501
        :type: str
        """
        if daily_percentage_change is None:
            raise ValueError("Invalid value for `daily_percentage_change`, must not be `None`")  # noqa: E501

        self._daily_percentage_change = daily_percentage_change

    @property
    def daily_volume(self):
        """Gets the daily_volume of this ITokenTicker.  # noqa: E501


        :return: The daily_volume of this ITokenTicker.  # noqa: E501
        :rtype: str
        """
        return self._daily_volume

    @daily_volume.setter
    def daily_volume(self, daily_volume):
        """Sets the daily_volume of this ITokenTicker.


        :param daily_volume: The daily_volume of this ITokenTicker.  # noqa: E501
        :type: str
        """
        if daily_volume is None:
            raise ValueError("Invalid value for `daily_volume`, must not be `None`")  # noqa: E501

        self._daily_volume = daily_volume

    @property
    def price_eth(self):
        """Gets the price_eth of this ITokenTicker.  # noqa: E501


        :return: The price_eth of this ITokenTicker.  # noqa: E501
        :rtype: str
        """
        return self._price_eth

    @price_eth.setter
    def price_eth(self, price_eth):
        """Sets the price_eth of this ITokenTicker.


        :param price_eth: The price_eth of this ITokenTicker.  # noqa: E501
        :type: str
        """
        if price_eth is None:
            raise ValueError("Invalid value for `price_eth`, must not be `None`")  # noqa: E501

        self._price_eth = price_eth

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ITokenTicker):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
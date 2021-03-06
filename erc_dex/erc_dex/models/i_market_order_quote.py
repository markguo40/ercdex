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

from erc_dex.models.market_quote import MarketQuote  # noqa: F401,E501


class IMarketOrderQuote(object):
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
        'quote': 'MarketQuote',
        'is_partial': 'bool'
    }

    attribute_map = {
        'quote': 'quote',
        'is_partial': 'isPartial'
    }

    def __init__(self, quote=None, is_partial=None):  # noqa: E501
        """IMarketOrderQuote - a model defined in Swagger"""  # noqa: E501

        self._quote = None
        self._is_partial = None
        self.discriminator = None

        self.quote = quote
        self.is_partial = is_partial

    @property
    def quote(self):
        """Gets the quote of this IMarketOrderQuote.  # noqa: E501


        :return: The quote of this IMarketOrderQuote.  # noqa: E501
        :rtype: MarketQuote
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this IMarketOrderQuote.


        :param quote: The quote of this IMarketOrderQuote.  # noqa: E501
        :type: MarketQuote
        """
        if quote is None:
            raise ValueError("Invalid value for `quote`, must not be `None`")  # noqa: E501

        self._quote = quote

    @property
    def is_partial(self):
        """Gets the is_partial of this IMarketOrderQuote.  # noqa: E501

        Can only provide a partial quote  # noqa: E501

        :return: The is_partial of this IMarketOrderQuote.  # noqa: E501
        :rtype: bool
        """
        return self._is_partial

    @is_partial.setter
    def is_partial(self, is_partial):
        """Sets the is_partial of this IMarketOrderQuote.

        Can only provide a partial quote  # noqa: E501

        :param is_partial: The is_partial of this IMarketOrderQuote.  # noqa: E501
        :type: bool
        """
        if is_partial is None:
            raise ValueError("Invalid value for `is_partial`, must not be `None`")  # noqa: E501

        self._is_partial = is_partial

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
        if not isinstance(other, IMarketOrderQuote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

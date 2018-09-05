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

from erc_dex.models.market_quote_fill import MarketQuoteFill  # noqa: F401,E501
from erc_dex.models.order import Order  # noqa: F401,E501


class MarketQuote(object):
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
        'id': 'float',
        'date_created': 'datetime',
        'date_updated': 'datetime',
        'salt': 'str',
        'hex': 'str',
        'taker_address': 'str',
        'price': 'str',
        'taker_amount': 'str',
        'maker_amount': 'str',
        'taker_asset_address': 'str',
        'expiration': 'float',
        'fee_token_symbol': 'str',
        'fee_amount': 'str',
        'network_fee_amount': 'str',
        'state': 'float',
        'fee_order_id': 'float',
        'fee_order': 'Order',
        'fills': 'list[MarketQuoteFill]'
    }

    attribute_map = {
        'id': 'id',
        'date_created': 'dateCreated',
        'date_updated': 'dateUpdated',
        'salt': 'salt',
        'hex': 'hex',
        'taker_address': 'takerAddress',
        'price': 'price',
        'taker_amount': 'takerAmount',
        'maker_amount': 'makerAmount',
        'taker_asset_address': 'takerAssetAddress',
        'expiration': 'expiration',
        'fee_token_symbol': 'feeTokenSymbol',
        'fee_amount': 'feeAmount',
        'network_fee_amount': 'networkFeeAmount',
        'state': 'state',
        'fee_order_id': 'feeOrderId',
        'fee_order': 'feeOrder',
        'fills': 'fills'
    }

    def __init__(self, id=None, date_created=None, date_updated=None, salt=None, hex=None, taker_address=None, price=None, taker_amount=None, maker_amount=None, taker_asset_address=None, expiration=None, fee_token_symbol=None, fee_amount=None, network_fee_amount=None, state=None, fee_order_id=None, fee_order=None, fills=None):  # noqa: E501
        """MarketQuote - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._date_created = None
        self._date_updated = None
        self._salt = None
        self._hex = None
        self._taker_address = None
        self._price = None
        self._taker_amount = None
        self._maker_amount = None
        self._taker_asset_address = None
        self._expiration = None
        self._fee_token_symbol = None
        self._fee_amount = None
        self._network_fee_amount = None
        self._state = None
        self._fee_order_id = None
        self._fee_order = None
        self._fills = None
        self.discriminator = None

        self.id = id
        self.date_created = date_created
        self.date_updated = date_updated
        self.salt = salt
        self.hex = hex
        self.taker_address = taker_address
        self.price = price
        self.taker_amount = taker_amount
        self.maker_amount = maker_amount
        self.taker_asset_address = taker_asset_address
        self.expiration = expiration
        self.fee_token_symbol = fee_token_symbol
        self.fee_amount = fee_amount
        self.network_fee_amount = network_fee_amount
        self.state = state
        if fee_order_id is not None:
            self.fee_order_id = fee_order_id
        if fee_order is not None:
            self.fee_order = fee_order
        self.fills = fills

    @property
    def id(self):
        """Gets the id of this MarketQuote.  # noqa: E501

        Unique Identifier  # noqa: E501

        :return: The id of this MarketQuote.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MarketQuote.

        Unique Identifier  # noqa: E501

        :param id: The id of this MarketQuote.  # noqa: E501
        :type: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this MarketQuote.  # noqa: E501

        Date of creation  # noqa: E501

        :return: The date_created of this MarketQuote.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this MarketQuote.

        Date of creation  # noqa: E501

        :param date_created: The date_created of this MarketQuote.  # noqa: E501
        :type: datetime
        """
        if date_created is None:
            raise ValueError("Invalid value for `date_created`, must not be `None`")  # noqa: E501

        self._date_created = date_created

    @property
    def date_updated(self):
        """Gets the date_updated of this MarketQuote.  # noqa: E501

        Date of updated  # noqa: E501

        :return: The date_updated of this MarketQuote.  # noqa: E501
        :rtype: datetime
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """Sets the date_updated of this MarketQuote.

        Date of updated  # noqa: E501

        :param date_updated: The date_updated of this MarketQuote.  # noqa: E501
        :type: datetime
        """
        if date_updated is None:
            raise ValueError("Invalid value for `date_updated`, must not be `None`")  # noqa: E501

        self._date_updated = date_updated

    @property
    def salt(self):
        """Gets the salt of this MarketQuote.  # noqa: E501

        Unique salt  # noqa: E501

        :return: The salt of this MarketQuote.  # noqa: E501
        :rtype: str
        """
        return self._salt

    @salt.setter
    def salt(self, salt):
        """Sets the salt of this MarketQuote.

        Unique salt  # noqa: E501

        :param salt: The salt of this MarketQuote.  # noqa: E501
        :type: str
        """
        if salt is None:
            raise ValueError("Invalid value for `salt`, must not be `None`")  # noqa: E501

        self._salt = salt

    @property
    def hex(self):
        """Gets the hex of this MarketQuote.  # noqa: E501

        Pre-calculated hex to sign  # noqa: E501

        :return: The hex of this MarketQuote.  # noqa: E501
        :rtype: str
        """
        return self._hex

    @hex.setter
    def hex(self, hex):
        """Sets the hex of this MarketQuote.

        Pre-calculated hex to sign  # noqa: E501

        :param hex: The hex of this MarketQuote.  # noqa: E501
        :type: str
        """
        if hex is None:
            raise ValueError("Invalid value for `hex`, must not be `None`")  # noqa: E501

        self._hex = hex

    @property
    def taker_address(self):
        """Gets the taker_address of this MarketQuote.  # noqa: E501

        Order taker  # noqa: E501

        :return: The taker_address of this MarketQuote.  # noqa: E501
        :rtype: str
        """
        return self._taker_address

    @taker_address.setter
    def taker_address(self, taker_address):
        """Sets the taker_address of this MarketQuote.

        Order taker  # noqa: E501

        :param taker_address: The taker_address of this MarketQuote.  # noqa: E501
        :type: str
        """
        if taker_address is None:
            raise ValueError("Invalid value for `taker_address`, must not be `None`")  # noqa: E501

        self._taker_address = taker_address

    @property
    def price(self):
        """Gets the price of this MarketQuote.  # noqa: E501

        Computed average price  # noqa: E501

        :return: The price of this MarketQuote.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this MarketQuote.

        Computed average price  # noqa: E501

        :param price: The price of this MarketQuote.  # noqa: E501
        :type: str
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def taker_amount(self):
        """Gets the taker_amount of this MarketQuote.  # noqa: E501

        Total taker amount  # noqa: E501

        :return: The taker_amount of this MarketQuote.  # noqa: E501
        :rtype: str
        """
        return self._taker_amount

    @taker_amount.setter
    def taker_amount(self, taker_amount):
        """Sets the taker_amount of this MarketQuote.

        Total taker amount  # noqa: E501

        :param taker_amount: The taker_amount of this MarketQuote.  # noqa: E501
        :type: str
        """
        if taker_amount is None:
            raise ValueError("Invalid value for `taker_amount`, must not be `None`")  # noqa: E501

        self._taker_amount = taker_amount

    @property
    def maker_amount(self):
        """Gets the maker_amount of this MarketQuote.  # noqa: E501

        Total maker amount  # noqa: E501

        :return: The maker_amount of this MarketQuote.  # noqa: E501
        :rtype: str
        """
        return self._maker_amount

    @maker_amount.setter
    def maker_amount(self, maker_amount):
        """Sets the maker_amount of this MarketQuote.

        Total maker amount  # noqa: E501

        :param maker_amount: The maker_amount of this MarketQuote.  # noqa: E501
        :type: str
        """
        if maker_amount is None:
            raise ValueError("Invalid value for `maker_amount`, must not be `None`")  # noqa: E501

        self._maker_amount = maker_amount

    @property
    def taker_asset_address(self):
        """Gets the taker_asset_address of this MarketQuote.  # noqa: E501

        Address of taker token  # noqa: E501

        :return: The taker_asset_address of this MarketQuote.  # noqa: E501
        :rtype: str
        """
        return self._taker_asset_address

    @taker_asset_address.setter
    def taker_asset_address(self, taker_asset_address):
        """Sets the taker_asset_address of this MarketQuote.

        Address of taker token  # noqa: E501

        :param taker_asset_address: The taker_asset_address of this MarketQuote.  # noqa: E501
        :type: str
        """
        if taker_asset_address is None:
            raise ValueError("Invalid value for `taker_asset_address`, must not be `None`")  # noqa: E501

        self._taker_asset_address = taker_asset_address

    @property
    def expiration(self):
        """Gets the expiration of this MarketQuote.  # noqa: E501

        Expiration - unix timestamp in seconds  # noqa: E501

        :return: The expiration of this MarketQuote.  # noqa: E501
        :rtype: float
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this MarketQuote.

        Expiration - unix timestamp in seconds  # noqa: E501

        :param expiration: The expiration of this MarketQuote.  # noqa: E501
        :type: float
        """
        if expiration is None:
            raise ValueError("Invalid value for `expiration`, must not be `None`")  # noqa: E501

        self._expiration = expiration

    @property
    def fee_token_symbol(self):
        """Gets the fee_token_symbol of this MarketQuote.  # noqa: E501

        Symbol of the token used to pay fees  # noqa: E501

        :return: The fee_token_symbol of this MarketQuote.  # noqa: E501
        :rtype: str
        """
        return self._fee_token_symbol

    @fee_token_symbol.setter
    def fee_token_symbol(self, fee_token_symbol):
        """Sets the fee_token_symbol of this MarketQuote.

        Symbol of the token used to pay fees  # noqa: E501

        :param fee_token_symbol: The fee_token_symbol of this MarketQuote.  # noqa: E501
        :type: str
        """
        if fee_token_symbol is None:
            raise ValueError("Invalid value for `fee_token_symbol`, must not be `None`")  # noqa: E501

        self._fee_token_symbol = fee_token_symbol

    @property
    def fee_amount(self):
        """Gets the fee_amount of this MarketQuote.  # noqa: E501

        Amount of fees paid in wei  # noqa: E501

        :return: The fee_amount of this MarketQuote.  # noqa: E501
        :rtype: str
        """
        return self._fee_amount

    @fee_amount.setter
    def fee_amount(self, fee_amount):
        """Sets the fee_amount of this MarketQuote.

        Amount of fees paid in wei  # noqa: E501

        :param fee_amount: The fee_amount of this MarketQuote.  # noqa: E501
        :type: str
        """
        if fee_amount is None:
            raise ValueError("Invalid value for `fee_amount`, must not be `None`")  # noqa: E501

        self._fee_amount = fee_amount

    @property
    def network_fee_amount(self):
        """Gets the network_fee_amount of this MarketQuote.  # noqa: E501

        Amount of fees paid to cover network fees in wei  # noqa: E501

        :return: The network_fee_amount of this MarketQuote.  # noqa: E501
        :rtype: str
        """
        return self._network_fee_amount

    @network_fee_amount.setter
    def network_fee_amount(self, network_fee_amount):
        """Sets the network_fee_amount of this MarketQuote.

        Amount of fees paid to cover network fees in wei  # noqa: E501

        :param network_fee_amount: The network_fee_amount of this MarketQuote.  # noqa: E501
        :type: str
        """
        if network_fee_amount is None:
            raise ValueError("Invalid value for `network_fee_amount`, must not be `None`")  # noqa: E501

        self._network_fee_amount = network_fee_amount

    @property
    def state(self):
        """Gets the state of this MarketQuote.  # noqa: E501

        State of the quote (Open [0], Expired [1], Invalid [2], Redeemed [3])  # noqa: E501

        :return: The state of this MarketQuote.  # noqa: E501
        :rtype: float
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this MarketQuote.

        State of the quote (Open [0], Expired [1], Invalid [2], Redeemed [3])  # noqa: E501

        :param state: The state of this MarketQuote.  # noqa: E501
        :type: float
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def fee_order_id(self):
        """Gets the fee_order_id of this MarketQuote.  # noqa: E501

        ID of order used to pay fees  # noqa: E501

        :return: The fee_order_id of this MarketQuote.  # noqa: E501
        :rtype: float
        """
        return self._fee_order_id

    @fee_order_id.setter
    def fee_order_id(self, fee_order_id):
        """Sets the fee_order_id of this MarketQuote.

        ID of order used to pay fees  # noqa: E501

        :param fee_order_id: The fee_order_id of this MarketQuote.  # noqa: E501
        :type: float
        """

        self._fee_order_id = fee_order_id

    @property
    def fee_order(self):
        """Gets the fee_order of this MarketQuote.  # noqa: E501

        Order used to pay fees  # noqa: E501

        :return: The fee_order of this MarketQuote.  # noqa: E501
        :rtype: Order
        """
        return self._fee_order

    @fee_order.setter
    def fee_order(self, fee_order):
        """Sets the fee_order of this MarketQuote.

        Order used to pay fees  # noqa: E501

        :param fee_order: The fee_order of this MarketQuote.  # noqa: E501
        :type: Order
        """

        self._fee_order = fee_order

    @property
    def fills(self):
        """Gets the fills of this MarketQuote.  # noqa: E501

        Collection of fills  # noqa: E501

        :return: The fills of this MarketQuote.  # noqa: E501
        :rtype: list[MarketQuoteFill]
        """
        return self._fills

    @fills.setter
    def fills(self, fills):
        """Sets the fills of this MarketQuote.

        Collection of fills  # noqa: E501

        :param fills: The fills of this MarketQuote.  # noqa: E501
        :type: list[MarketQuoteFill]
        """
        if fills is None:
            raise ValueError("Invalid value for `fills`, must not be `None`")  # noqa: E501

        self._fills = fills

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
        if not isinstance(other, MarketQuote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other